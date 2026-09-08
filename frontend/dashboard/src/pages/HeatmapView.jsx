import { useEffect, useState } from 'react'
import { MapContainer, TileLayer, useMap } from 'react-leaflet'
import L from 'leaflet'
import 'leaflet.heat'
import client from '../api/client'
import LoadingState, { ErrorState } from '../components/LoadingState'

const DEFAULT_CENTER = [23.2599, 77.4126]

// react-leaflet has no built-in heat layer, so this small wrapper
// mounts leaflet.heat directly onto the underlying map instance.
function HeatLayer({ points }) {
  const map = useMap()
  useEffect(() => {
    if (!points.length) return
    const heat = L.heatLayer(
      points.map(p => [p.lat, p.lng, p.weight || 1]),
      { radius: 25 }
    )
    heat.addTo(map)
    return () => map.removeLayer(heat)
  }, [points, map])
  return null
}

export default function HeatmapView() {
  const [points, setPoints] = useState([])
  const [type, setType] = useState('pothole')
  const [status, setStatus] = useState('loading')

  useEffect(() => {
    setStatus('loading')
    client.get(`/heatmap?type=${type}`)
      .then(res => { setPoints(res.data); setStatus('ready') })
      .catch(() => setStatus('error'))
  }, [type])

  return (
    <div className="page">
      <h1>Heatmap</h1>
      <div className="controls">
        {['pothole', 'congestion', 'waterlogging'].map(t => (
          <button
            key={t}
            className={t === type ? 'active' : ''}
            onClick={() => setType(t)}
          >
            {t}
          </button>
        ))}
      </div>
      {status === 'loading' && <LoadingState label="Loading heatmap…" />}
      {status === 'error' && <ErrorState message="Could not load heatmap data." />}
      {status === 'ready' && (
        <MapContainer center={DEFAULT_CENTER} zoom={13} style={{ height: '70vh', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; OpenStreetMap contributors"
          />
          <HeatLayer points={points} />
        </MapContainer>
      )}
    </div>
  )
}
