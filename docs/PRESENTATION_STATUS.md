# Monumentaal — Pre-Presentation Status

**As of:** May 06, 2026 — Session 2
**Deadline:** May 07, 2026 at 9:00 AM

---

## Changes Made This Session

### UI/UX Polish
- **SiteCard hover**: lift effect (`-translate-y-1`), enhanced selection ring with offset, blue border on hover
- **Mobile layout**: Split view now stacks on mobile (list on top, map below) with proper height handling

### Filtering
- **Year filter REMOVED** — per user request; app now shows all 89 sites regardless of year
- Type and Province filters remain

### Data Corrections
- **Church Square**: Fixed coordinates — was Cape Town (-33.9, 18.4), corrected to Pretoria (-25.746, 28.187)
- **Dutch Reformed Church, Somerset East**: Province corrected from Western Cape to Eastern Cape
- **St. George's Grammar School**: Coordinates swapped from Cape Town to Makhenda/Grahamstown (-33.31, 26.52)

### Image Handling
- External image fetch abandoned (Wikipedia API 403)
- Fallback design implemented: colored header with site initial + type label
- Clean, consistent, no broken-image risk

### Documentation
- `docs/DEMO_SCRIPT.md` — 3-minute presentation walkthrough with talking points

---

## Current Data Summary

| Metric | Value |
|--------|-------|
| Total sites | 89 |
| Pre-1940 sites | 83 |
| Sites with null images | 89 (using fallback) |
| Sites with null coordinates | 0 |
| Coordinate anomalies (fixed) | 3 |

**Type breakdown:**
- buildings: 32
- churches: 24
- museums: 14
- monuments: 14
- forts: 5

**Province breakdown:**
- Western Cape: 47
- Gauteng: 12
- Free State: 10
- Eastern Cape: 10
- KwaZulu-Natal: 7
- North West: 2
- Northern Cape: 1

---

## What's Still Incomplete (by choice)

**Images** — All null. Reason: Wikipedia blocked. For demo, colored initials suffice.
**SAHRA sourcing** — Coordinates appear accurate but source attribution not in metadata. Unknown if originally from SAHRA or OpenStreetMap.

---

## What to Test Before Demo

1. Open `http://localhost:5173`
2. Verify map loads with 89 markers across SA
3. Click Castle of Good Hope — popup + card highlight
4. Filter by Type: Church — list reduces to 24
5. Search "Durban" — shows KZN sites
6. Resize to mobile width — layout stacks cleanly
7. Build for production: `npm run build` (already passes)

---

## Files Modified This Session

- `src/App.jsx` — removed year filter, added mobile stacking order
- `src/components/FilterBar.jsx` — removed year input
- `src/components/SiteCard.jsx` — hover/selection polish, simplified image area
- `src/components/MapView.jsx` — popup now shows site initial (not type letter)
- `src/data/sites.json` — coordinate/province corrections (3 sites)
- `docs/DEMO_SCRIPT.md` — new (presentation walkthrough)

---

## Final Verdict

**Ready for demo?** Yes.
- Core features work: search, type+province filters, map/list sync, selection highlighting
- Visuals are clean, responsive, and impressively colorful
- Data accuracy validated (spot-checked coordinates, fixed 3 errors)
- Only missing piece is real photos, but fallback is professional enough for a 10-minute presentation

**Showstopper risk:** Low. Dev server stable, build passes, data cleaner than before.

**If Wife Questions Images:** Explain Wikipedia API blocked, propose to manually add 20–30 key site images using web search post-deadline. For now, colored initials keep focus on Features, not missing media.
