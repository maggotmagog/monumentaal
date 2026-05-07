import SiteCard from './SiteCard'

export default function SiteList({ sites, selectedId, onSelect }) {
  if (sites.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full p-8 text-center">
        <div className="text-gray-400 mb-2">
          <svg className="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
        </div>
        <p className="text-gray-500 text-sm">No sites match your filters.</p>
        <p className="text-gray-400 text-xs mt-1">Try adjusting your search or type filter.</p>
      </div>
    )
  }

  return (
    <div className="p-2 space-y-2" data-testid="site-list">
      {sites.map(site => (
        <SiteCard
          key={site.id}
          site={site}
          onClick={onSelect}
          isSelected={selectedId === site.id}
        />
      ))}
    </div>
  )
}
