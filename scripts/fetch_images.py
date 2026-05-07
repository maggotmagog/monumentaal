#!/usr/bin/env python3
"""
Fetch Wikimedia Commons image URLs for Monumentaal sites.
Uses Wikipedia API to search for images by site name.
"""

import json
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load sites
with open('src/data/sites.json', 'r') as f:
    sites = json.load(f)

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"

def search_image_for_site(site):
    """Find an image URL for a given site name."""
    query = site['name']
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'pageimages',
        'pithumbsize': 800,
        'redirects': 1,
        'titles': query,
        'origin': '*'
    }
    try:
        resp = requests.get(WIKIPEDIA_API, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        pages = data.get('query', {}).get('pages', {})
        for page_id, page in pages.items():
            if page_id != '-1':
                thumbnail = page.get('thumbnail', {})
                if thumbnail and 'source' in thumbnail:
                    return thumbnail['source']
        # Fallback: search Commons directly
        commons_params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srsearch': f'{query} filetype:bitmap',
            'srnamespace': '6',  # File namespace
            'srlimit': 1,
            'origin': '*'
        }
        commons_resp = requests.get(COMMONS_API, params=commons_params, timeout=10)
        commons_resp.raise_for_status()
        commons_data = commons_resp.json()
        results = commons_data.get('query', {}).get('search', [])
        if results:
            file_title = results[0]['title']
            # Get image info
            img_params = {
                'action': 'query',
                'format': 'json',
                'titles': file_title,
                'prop': 'imageinfo',
                'iiprop': 'url',
                'origin': '*'
            }
            img_resp = requests.get(COMMONS_API, params=img_params, timeout=10)
            img_resp.raise_for_status()
            img_data = img_resp.json()
            img_pages = img_data.get('query', {}).get('pages', {})
            for img_page in img_pages.values():
                info = img_page.get('imageinfo', [{}])[0]
                if 'url' in info:
                    return info['url']
    except Exception as e:
        print(f"Error for {query}: {e}")
    return None

def fetch_all_images(max_workers=10):
    updated = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_site = {executor.submit(search_image_for_site, site): site for site in sites}
        for future in as_completed(future_to_site):
            site = future_to_site[future]
            try:
                img_url = future.result(timeout=15)
                if img_url:
                    site['image_url'] = img_url
                    updated += 1
                    print(f"✓ {site['name']}")
                else:
                    print(f"✗ {site['name']} (no image)")
            except Exception as e:
                print(f"✗ {site['name']} (error: {e})")
            time.sleep(0.1)  # be nice to APIs
    return updated

if __name__ == '__main__':
    print(f"Fetching images for {len(sites)} sites...")
    updated = fetch_all_images()
    # Save back
    with open('src/data/sites.json', 'w') as f:
        json.dump(sites, f, indent=2)
    print(f"\nDone. Updated {updated}/{len(sites)} sites with image URLs.")
