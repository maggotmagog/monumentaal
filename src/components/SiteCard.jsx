import { useState } from 'react'

export default function SiteCard({ site, onClick, isSelected, onDoubleClick }) {
  const typeColors = {
    church: { bg: 'bg-red-50', border: 'border-red-200', text: 'text-red-800', accent: 'bg-red-500' },
    monument: { bg: 'bg-amber-50', border: 'border-amber-200', text: 'text-amber-800', accent: 'bg-amber-500' },
    building: { bg: 'bg-blue-50', border: 'border-blue-200', text: 'text-blue-800', accent: 'bg-blue-500' },
    fort: { bg: 'bg-stone-50', border: 'border-stone-200', text: 'text-stone-800', accent: 'bg-stone-500' },
    museum: { bg: 'bg-purple-50', border: 'border-purple-200', text: 'text-purple-800', accent: 'bg-purple-500' },
    statue: { bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-800', accent: 'bg-emerald-500' }
  }

  const colors = typeColors[site.type] || { bg: 'bg-gray-50', border: 'border-gray-200', text: 'text-gray-800', accent: 'bg-gray-500' }

  return (
    <div
      className={`rounded-xl overflow-hidden border transition-all duration-200 cursor-pointer hover:-translate-y-1 hover:shadow-lg ${isSelected ? 'ring-2 ring-blue-500 ring-offset-2 shadow-md' : 'hover:border-blue-300'} bg-white`}
      onClick={(e) => { e.stopPropagation(); onClick(site); }}
      onDoubleClick={(e) => { e.stopPropagation(); onDoubleClick?.(site); }}
      title="Click to select, double-click to zoom map"
    >
      {/* Image area */}
      {site.image_url ? (
        <img src={site.image_url} alt={site.name} className="w-full h-48 object-cover bg-slate-100" />
      ) : (
        <div className={`h-48 w-full flex items-center justify-center ${colors.accent}`}>
          <div className="text-center">
            <div className="text-6xl font-bold text-white/90 select-none mb-2">{site.name.charAt(0).toUpperCase()}</div>
            <div className="text-white/70 text-sm uppercase tracking-wider">{site.type}</div>
          </div>
        </div>
      )}

      <div className="p-5">
        <div className="flex items-center gap-2 mb-3">
          <span className={`px-2.5 py-1 rounded-full text-xs font-semibold ${colors.text} ${colors.bg}`}>
            {site.type.charAt(0).toUpperCase() + site.type.slice(1)}
          </span>
          {site.year_built && (
            <span className="px-2.5 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-700">
              {site.year_built}
            </span>
          )}
        </div>
        <h3 className="font-bold text-slate-900 text-lg leading-tight mb-2">{site.name}</h3>
        <div className="flex items-center text-slate-500 text-sm mb-3">
          <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span>{site.location}</span>
        </div>
        <p className="text-slate-600 text-sm leading-relaxed line-clamp-3">{site.description}</p>
      </div>
    </div>
  )
}
