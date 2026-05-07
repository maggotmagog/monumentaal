# Monumentaal — Demo Script (9:00 AM Presentation)

## Opening (30 seconds)
"Monumentaal is a React web app I built with my wife to explore historic South African sites — specifically monuments, churches, and buildings constructed before 1940."

## Tech Stack (15 seconds)
- React + Vite for fast dev
- Tailwind CSS for styling
- Leaflet maps (no API key, free tiles)
- Local JSON data — fast, offline-capable

## Live Demo (3 minutes)

### 1. Start with the map
- App opens centered on South Africa
- 89 sites plotted across all 9 provinces
- Color-coded markers: churches (red), forts (stone), museums (purple), etc.

### 2. Click Castle of Good Hope
- Popup shows name, year 1666, type, location
- Card highlights in sidebar
- Demonstrates map/list sync

### 3. Filter by Type → "Church"
- List narrows to 24 churches
- Show St. George's Cathedral (Desmond Tutu's church)
- Mention: all sites pre-1940 as requirement

### 4. Search: "Durban"
- Instantly filters to KwaZulu-Natal sites
- Shows diversity: Hindu temple, cathedral, railway station

### 5. Mobile view (optional)
- Resize browser to 375px
- Layout stacks: list on top, map below
- All interactive elements still work

### 6. Wrap-up
"Built in two sessions, ~10 hours. Data curated from heritage registers. All coordinates verified. Ready to scale with real images and backend."

## Key Talking Points
- Pre-1940 filter enforced by data
- Province distribution shows historical settlement patterns
- Responsive design for future mobile app
- Zero external dependencies beyond map tiles

## If Questions Arise
- Codebase is ~500 lines total, components are modular
- Could add images from Wikimedia/SAHRA later
- Search is fuzzy (matches name, description, location)
