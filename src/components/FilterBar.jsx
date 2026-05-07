const TYPES = ['all', 'church', 'monument', 'building', 'fort', 'museum', 'statue']
const PROVINCES = [
  'all',
  'Western Cape',
  'Eastern Cape',
  'Northern Cape',
  'KwaZulu-Natal',
  'Free State',
  'Gauteng',
  'North West'
]

export default function FilterBar({ typeFilter, onTypeChange, provinceFilter, onProvinceChange }) {
  return (
    <div className="flex flex-col sm:flex-row flex-wrap items-start sm:items-center gap-3">
      <div className="flex items-center gap-2">
        <label className="text-sm font-medium text-slate-700">Type:</label>
        <select
          className="px-3 py-2 rounded-lg border border-slate-300 bg-white text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm shadow-sm"
          value={typeFilter}
          onChange={e => onTypeChange(e.target.value)}
        >
          <option value="all">All Types</option>
          {TYPES.filter(t => t !== 'all').map(t => (
            <option key={t} value={t}>{t.charAt(0).toUpperCase() + t.slice(1)}</option>
          ))}
        </select>
      </div>
      <div className="flex items-center gap-2">
        <label className="text-sm font-medium text-slate-700">Province:</label>
        <select
          className="px-3 py-2 rounded-lg border border-slate-300 bg-white text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm shadow-sm"
          value={provinceFilter}
          onChange={e => onProvinceChange(e.target.value)}
        >
          <option value="all">All Provinces</option>
          {PROVINCES.filter(p => p !== 'all').map(p => (
            <option key={p} value={p}>{p}</option>
          ))}
        </select>
      </div>
    </div>
  )
}
