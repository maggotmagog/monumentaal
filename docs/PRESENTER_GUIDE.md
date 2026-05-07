# Monumentaal — Presenter Guide

## Quick Demo Script (2-3 minutes)

1. **Start**: Open browser to `http://localhost:5173` (fullscreen with F11)
2. **Landing**: Show header "Monumentaal" and subtitle "Historic Sites of South Africa (pre-1940)"
3. **Search demo**:
   - Type "cathedral" → results filter instantly
   - Clear search
4. **Filter demo**:
   - Change Type dropdown to "Church" → only churches remain
   - Note: no year filter needed — all sites are pre-1940 by design
5. **Cards interaction**:
   - Hover over cards to see subtle elevation lift
   - Click any card → it gets a blue ring, map marker highlights
6. **Map demo**:
   - Show colored markers (each type has its own color)
   - Click a marker → popup shows details (even without images we have colored placeholders)
   - Zoom/pan to explore
7. **Responsive**: Resize to mobile width → sidebar becomes scrollable above map
8. **Closing pitch**: "Built with React + Vite + Tailwind + Leaflet in ~10 hours. Data curated from Wikimedia, UI designed Airbnb-style for a clean, modern experience."

## Tech Stack
- **React + Vite**: Fast HMR, instant dev
- **Tailwind CSS**: Modern, responsive design
- **Leaflet**: Open-source maps, no API key
- **88 pre-1940 sites**: Accurate coordinates, placeholder color scheme by type

## Architecture
```
App.jsx (state, filters) → SiteCard + MapView + SearchBar + FilterBar
sites.json (static data) → filtered → rendered in list & map simultaneously
```

## Build & Run
```bash
cd ~/Desktop/Projects/Monumentaal
npm install
npm run dev      # → http://localhost:5173
npm run build    # production in dist/
```

## Design Choices
- Airbnb-inspired: generous whitespace, rounded-xl cards, subtle shadows, soft color palette
- Type-specific accent colors for quick visual identification
- Placeholder "badge" with type initial replaces unreliable external images
- Mobile-first layout (sidebar width responsive)
- Selection ring sync between list and map

## Presentation Tips
- Demo first (under 60 sec), then show code.
- Emphasize that image placeholders are intentional for reliability; can be re-enabled if images work.
- Explain the split-pane pattern: list on left, map on right, both filtered in real-time.
- Show the responsive behavior by resizing.

## Checklist
- [ ] Dev server running
- [ ] Test search: "church", "fort", "cave"
- [ ] Test type filter: "Museum"
- [ ] Click a card, see marker highlight
- [ ] Resize to mobile width
- [ ] Have `docs/architecture.svg` ready to explain structure
