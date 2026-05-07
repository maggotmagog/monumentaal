import { Component } from 'react'

export default class MapErrorBoundary extends Component {
  state = { hasError: false }

  static getDerivedStateFromError() {
    return { hasError: true }
  }

  componentDidCatch(error, info) {
    console.error('MapErrorBoundary caught an error', error, info)
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="h-full w-full flex items-center justify-center bg-gray-100">
          <div className="text-center">
            <p className="text-gray-600 font-medium">Map temporarily unavailable</p>
            <p className="text-gray-400 text-sm mt-1">Use the list to browse sites</p>
          </div>
        </div>
      )
    }
    return this.props.children
  }
}
