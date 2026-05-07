#!/usr/bin/env python3
"""
Batch import South African statues from Wikipedia to Monumentaal sites.json.
"""
import json, requests, time, re
from urllib.parse import quote

SITES_PATH = "src/data/sites.json"

WIKI_API = "https://en.wikipedia.org/w/api.php"

CITY_CATEGORIES = [
    "Statues_in_Cape_Town",
    "Statues_in_Johannesburg",
    "Statues_in_Pretoria",
    "Statues_in_Durban",
    "Statues_in_Bloemfontein",
    "Statues_in_Port_Elizabeth",
    "Statues_in_Pietermaritzburg"
]

EXISTING_STATUE_NAMES = set()

def load_sites():
    with open(SITES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_sites(sites):
    with open(SITES_PATH, "w", encoding="utf-8") as f:
        json.dump(sites, f, indent=2, ensure_ascii=False)

def normalize_name(name):
    return name.lower().strip()

def wiki_get(params):
    try:
        r = requests.get(WIKI_API, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Wiki API error: {e}")
        return None

def get_category_members(category):
    members = []
    cmcontinue = None
    while True:
        params = {
            "action": "query",
            "format": "json",
            "list": "categorymembers",
            "cmtitle": f"Category:{category}",
            "cmlimit": "500"
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
        data = wiki_get(params)
        if not data or "query" not in data:
            break
        for page in data["query"]["categorymembers"]:
            if "Statue" in page["title"] or "monument" in page["title"].lower():
                members.append(page["title"])
        if "continue" in data:
            cmcontinue = data["continue"]["cmcontinue"]
        else:
            break
        time.sleep(0.1)
    return members

def get_page_coordinates(title):
    params = {
        "action": "query",
        "format": "json",
        "prop": "coordinates|pageprops",
        "titles": title,
        "redirects": True
    }
    data = wiki_get(params)
    if not data or "query" not in data:
        return None
    pages = data["query"]["pages"]
    for page in pages.values():
        if "coordinates" in page:
            return float(page["coordinates"][0]["lat"]), float(page["coordinates"][0]["lon"])
    return None

def get_page_extract(title):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explimit": 1,
        "titles": title
    }
    data = wiki_get(params)
    if not data or "query" not in data:
        return ""
    pages = data["query"]["pages"]
    for page in pages.values():
        if "extract" in page:
            html = page["extract"]
            text = re.sub('<[^<]+?>', '', html)
            return text.strip()
    return ""

def infer_province_from_coords(lat, lng):
    # Rough province mapping by coordinates
    if -35 <= lat <= -30 and 17 <= lng <= 24:
        return "Western Cape"
    if -34 <= lat <= -30 and 24 <= lng <= 30:
        return "Eastern Cape"
    if -29 <= lat <= -26 and 21 <= lng <= 30:
        return "Free State"
    if -27 <= lat <= -22 and 22 <= lng <= 32:
        return "Northern Cape"
    if -27 <= lat <= -24 and 25 <= lng <= 33:
        return "North West"
    if -26 <= lat <= -22 and 29 <= lng <= 33:
        return "Mpumalanga"
    if -26 <= lat <= -22 and 28 <= lng <= 32:
        return "Gauteng"
    if -31 <= lat <= -26 and 28 <= lng <= 33:
        return "KwaZulu-Natal"
    if -24 <= lat <= -22 and 29 <= lng <= 32:
        return "Limpopo"
    return None

def main():
    sites = load_sites()
    next_id = max(s["id"] for s in sites) + 1
    
    # Build set of existing statue names
    for s in sites:
        if s.get("type") == "statue":
            EXISTING_STATUE_NAMES.add(normalize_name(s["name"]))
    
    added = 0
    for category in CITY_CATEGORIES:
        print(f"\n=== Category: {category} ===")
        titles = get_category_members(category)
        print(f"Found {len(titles)} potential statues")
        for title in titles:
            norm_name = normalize_name(title)
            if norm_name in EXISTING_STATUE_NAMES:
                continue
            latlng = get_page_coordinates(title)
            if not latlng:
                continue
            lat, lng = latlng
            province = infer_province_from_coords(lat, lng) or "Unknown"
            desc = get_page_extract(title)
            entry = {
                "id": next_id,
                "name": title,
                "description": desc or f"Statue located in {province}.",
                "lat": lat,
                "lng": lng,
                "province": province,
                "type": "statue",
                "year_built": None,
                "image_url": None
            }
            sites.append(entry)
            EXISTING_STATUE_NAMES.add(norm_name)
            next_id += 1
            added += 1
            print(f"Added: {title} ({province}) [{lat}, {lng}]")
            time.sleep(0.2)
    
    # Reassign IDs sequentially
    for idx, s in enumerate(sites, start=1):
        s["id"] = idx
    
    save_sites(sites)
    print(f"\nTotal added: {added}")
    print(f"New total sites: {len(sites)}")
    
    # Build
    print("\nBuilding...")
    import subprocess
    res = subprocess.run(["npm", "run", "build"], capture_output=True, text=True, timeout=120)
    print(res.stdout)
    if res.returncode != 0:
        print("Build failed:", res.stderr)
    else:
        print("Build succeeded")

if __name__ == "__main__":
    main()