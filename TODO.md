# Monumentaal — Build Checklist

## Phase 1: Project Setup (1h)
- [x] Create project folder structure
- [ ] `npm create vite@latest Monumentaal -- --template react`
- [ ] `npm install`
- [ ] Install Tailwind CSS + @tailwindcss/vite
- [ ] Install Leaflet + react-leaflet
- [ ] Verify dev server runs

## Phase 2: Data Preparation (1.5h)
- [ ] Curate list of ~50 SA historic sites (pre-1940)
- [ ] For each: name, type, year_built, lat/lng, description, image_url (from Wikimedia)
- [ ] Save as `src/data/sites.json`
- [ ] Test map renders with sample markers

## Phase 3: Components (3h)
- [ ] Layout: header (search + filters), main (split map/list)
- [ ] Map component: Leaflet with popups
- [ ] SiteList component: scrollable cards with images
- [ ] SiteCard component: image, title, year, description snippet
- [ ] SearchBar component: text input + fuzzy results
- [ ] FilterBar component: type dropdown, era range slider

## Phase 4: Logic & Features (2h)
- [ ] State management: sites, search query, filters
- [ ] Filter function: by text, type, year range
- [ ] Map/list sync: clicking marker highlights card, vice versa
- [ ] Responsive layout (mobile-first)

## Phase 5: Polish (1.5h)
- [ ] Tailwind styling: modern colors, shadows, rounded corners
- [ ] Loading states, empty states
- [ ] Smooth transitions, hover effects
- [ ] Ensure images load reliably (fallback)
- [ ] Test on mobile viewport

## Phase 6: Documentation & Delivery (30m)
- [ ] Write README with features, how to run, data sources
- [ ] Export development journal to PDF for presentation backup
- [ ] Test presentation: open in browser, demo search and filters
- [ ] Verify all images display offline?

---

**Total estimated time:** ~10 hours (can compress if needed)

