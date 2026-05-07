import { useState } from 'react'
import MapView from './components/MapView'
import SiteCard from './components/SiteCard'
import SearchBar from './components/SearchBar'
import FilterBar from './components/FilterBar'
import sites from './data/sites.json'

function App() {
  const [query, setQuery] = useState('')
  const [typeFilter, setTypeFilter] = useState('all')
  const [provinceFilter, setProvinceFilter] = useState('all')
  const [selectedSite, setSelectedSite] = useState(null)
  const [flyTo, setFlyTo] = useState(null)

  // Filtering logic
  const filteredSites = sites.filter(site => {
    const matchesQuery = query === '' ||
      site.name.toLowerCase().includes(query.toLowerCase()) ||
      site.description.toLowerCase().includes(query.toLowerCase()) ||
      site.location.toLowerCase().includes(query.toLowerCase())
    const matchesType = typeFilter === 'all' || site.type === typeFilter
    const matchesProvince = provinceFilter === 'all' || site.province === provinceFilter
    return matchesQuery && matchesType && matchesProvince
  })

  const handleDoubleClick = (site) => {
    setFlyTo({
      center: [site.lat, site.lng],
      zoom: 14
    })
    // Also select the site
    setSelectedSite(site)
  }

  return (
    <div className="h-screen flex flex-col bg-slate-50">
      <header className="bg-gradient-to-r from-indigo-600 to-purple-600 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 py-5">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="flex items-center gap-4">
              {/* Logo SVG */}
              <svg className="w-10 h-10 text-white flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                {/* Simple church silhouette */}
                <path d="M12 3L3 10v4l9 7 9-7v-4L12 3z" />
                <path d="M12 13v8" />
                <path d="M8 21v-2" />
                <path d="M16 21v-2" />
              </svg>
              <div>
                <h1 className="text-2xl font-bold text-white tracking-tight">Monumentaal</h1>
                <p className="text-indigo-100 text-sm mt-0.5">Historic Sites of South Africa (pre-1940)</p>
              </div>
            </div>
            <div className="flex flex-col sm:flex-row gap-3">
              <SearchBar query={query} onQueryChange={setQuery} />
              <FilterBar
                typeFilter={typeFilter}
                onTypeChange={setTypeFilter}
                provinceFilter={provinceFilter}
                onProvinceChange={setProvinceFilter}
              />
            </div>
          </div>
        </div>
      </header>
      <main className="flex-1 flex flex-col md:flex-row overflow-hidden">
        <div className="w-full md:w-96 lg:w-[420px] overflow-y-auto bg-white border-r border-slate-200 order-2 md:order-1">
          <div className="p-4 sticky top-0 bg-white z-10 border-b border-slate-100">
            <span className="text-sm font-medium text-slate-600">
              {filteredSites.length} of {sites.length} sites
            </span>
          </div>
          <div className="p-4 space-y-4">
            {filteredSites.map(site => (
              <SiteCard
                key={site.id}
                site={site}
                onClick={setSelectedSite}
                onDoubleClick={handleDoubleClick}
                isSelected={selectedSite?.id === site.id}
              />
            ))}
          </div>
        </div>
        <div className="flex-1 min-h-0 h-96 md:h-full w-full order-1 md:order-2">
          <MapView sites={filteredSites} selectedId={selectedSite?.id} onSelect={setSelectedSite} flyTo={flyTo} />
        </div>
      </main>
    </div>
  )
}

export default App
