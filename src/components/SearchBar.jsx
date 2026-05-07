import { useState, useEffect } from 'react'

export default function SearchBar({ query, onQueryChange }) {
  const [localQuery, setLocalQuery] = useState(query)

  useEffect(() => {
    setLocalQuery(query)
  }, [query])

  const handleChange = (e) => {
    const value = e.target.value
    setLocalQuery(value)
    onQueryChange(value)
  }

  return (
    <div className="relative flex-1">
      <input
        type="text"
        placeholder="Search historic sites…"
        className="w-full pl-10 pr-4 py-2.5 rounded-lg border border-slate-300 bg-white text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent shadow-sm transition-shadow"
        value={localQuery}
        onChange={handleChange}
      />
      <svg className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
    </div>
  )
}
