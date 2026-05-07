# Monumentaal — Development Journal

## Project Overview
Modern travel web app to discover historic points of interest in South Africa (monuments, churches, buildings pre-1940).

**Tech Stack:** React + Vite + Tailwind CSS + Leaflet
**Deadline:** Presentation tomorrow at 9:00 AM
**Scope:** MVP with search, filters, map, and visual wow factor (photos)

---

## Decision Log

### 2026-05-06 — Initial Scaffold

**Requirements from stakeholder:**
- App name: Monumentaal
- Web-based (mobile-ready)
- Show historic sites (pre-1940) in South Africa
- Must include photos for visual impact
- Each site needs a brief description/history
- AI features: natural language search (fuzzy matching)
- No chat interface (just search + filters)
- Present tomorrow 9 AM live from laptop

**Architecture decisions:**
- React + Vite for fast dev and build
- Tailwind CSS for modern, clean UI
- Leaflet for interactive map (no API key needed)
- Static JSON dataset (curated ~50 sites)
- No backend (fully client-side for easy demo)
- Images sourced from Wikimedia Commons (free, reliable)

**Trade-offs:**
- No real AI (too complex for deadline). We'll use fuzzy search
- Limited site list (50) for demo quality; can expand later
- No user accounts/persistence

**Next steps:**
1. Create Vite + React project
2. Set up Tailwind
3. Build site dataset with Wikimedia image URLs
4. Create map component (Leaflet)
5. Build list view with cards
6. Implement search + filters
7. Polish UI and mobile responsiveness

---

*End of Journal Entry*
