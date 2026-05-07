import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import { useEffect } from 'react'

// Internal component: triggers flyTo when center/zoom props change
function MapController({ center, zoom }) {
  const map = useMap()
  useEffect(() => {
    if (center && zoom) {
      map.flyTo(center, zoom, { duration: 1.5 })
    }
  }, [center, zoom, map])
  return null
}

// Custom marker icon setup
delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png'
})

function getMarkerColor(type) {
  const colors = {
    church: '#ef4444',
    monument: '#f59e0b',
    building: '#3b82f6',
    fort: '#78716c',
    museum: '#a855f7',
    statue: '#10b981'
  }
  return colors[type] || '#64748b'
}

function createCustomIcon(color, selected = false) {
  return L.divIcon({
    className: 'custom-marker',
    html: `<div style="
      background-color: ${color};
      width: ${selected ? '32px' : '24px'};
      height: ${selected ? '32px' : '24px'};
      border-radius: 50% 50% 50% 0;
      transform: rotate(-45deg) ${selected ? 'scale(1.2)' : ''};
      border: ${selected ? '4px solid #2563eb' : '3px solid white'};
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      transition: all 0.2s;
    "></div>`,
    iconSize: selected ? [40, 56] : [30, 42],
    iconAnchor: selected ? [20, 56] : [15, 42],
    popupAnchor: [1, -34],
    tooltipAnchor: [16, -28]
  })
}

export default function MapView({ sites, selectedId, onSelect, flyTo }) {
  const center = [-30.5595, 22.9375] // SA center default

  const validSites = sites.filter(site => site.lat != null && site.lng != null)

  if (validSites.length === 0) {
    return (
      <div className="h-full w-full flex items-center justify-center bg-slate-100">
        <p className="text-slate-500">No sites with valid coordinates.</p>
      </div>
    )
  }

  return (
    <MapContainer
      center={center}
      zoom={5}
      className="h-full w-full"
      scrollWheelZoom
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {/* Fly to location on double-click */}
      <MapController center={flyTo?.center} zoom={flyTo?.zoom} />
      {validSites.map(site => {
        const color = getMarkerColor(site.type)
        const isSelected = selectedId === site.id
        return (
          <Marker
            key={site.id}
            position={[site.lat, site.lng]}
            icon={createCustomIcon(color, isSelected)}
            eventHandlers={{ click: () => onSelect(site) }}
          >
            <Popup maxWidth={320} minWidth={280} open={selectedId === site.id}>
              <div className="p-2">
                <h3 className="font-bold text-slate-900 mb-1 text-base">{site.name}</h3>
                <div className="flex flex-wrap gap-1.5 mb-2">
                  <span className="px-2 py-0.5 bg-blue-100 text-blue-800 rounded text-xs font-medium uppercase">
                    {site.type}
                  </span>
                  {site.year_built && (
                    <span className="px-2 py-0.5 bg-slate-100 text-slate-700 rounded text-xs">
                      {site.year_built}
                    </span>
                  )}
                  <span className="px-2 py-0.5 bg-green-100 text-green-800 rounded text-xs">
                    {site.location}
                  </span>
                </div>
                {site.image_url ? (
                  <img
                    src={site.image_url}
                    alt={site.name}
                    className="w-full h-32 object-cover rounded mb-2"
                    loading="lazy"
                    onError={(e) => { e.target.style.display = 'none' }}
                  />
                ) : (
                  <div className={`w-full h-32 rounded mb-2 flex items-center justify-center text-white font-bold text-2xl ${getMarkerColor(site.type).replace(')', '/20)').replace('rgb', 'rgba')}`}>
                    {site.name.charAt(0).toUpperCase()}
                  </div>
                )}
                <p className="text-sm text-gray-600 leading-snug">{site.description}</p>
              </div>
            </Popup>
          </Marker>
        )
      })}
    </MapContainer>
  )
}
