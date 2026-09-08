import { useEffect, useState } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { Link } from 'react-router-dom'
import L from 'leaflet'
import client from '../api/client'
import LoadingState, { ErrorState } from '../components/LoadingState'

// Swap this for your actual city center
const DEFAULT_CENTER = [23.2599, 77.4126]

// One entry per detection type: pin color, the glyph drawn inside the pin,
// and the label shown in the legend. Add a new type here and it
// automatically gets its own marker style + legend row.
const TYPE_STYLES = {
  pothole: {
    color: '#F5A623',
    label: 'Pothole',
    glyph: '<circle cx="12" cy="10" r="2.6" fill="white"/>',
  },
  road_crack: {
    color: '#E74C3C',
    label: 'Road Damage',
    glyph: '<path d="M12 6 L16 13.5 H8 Z" fill="none" stroke="white" stroke-width="1.3" stroke-linejoin="round"/><rect x="11.4" y="9" width="1.2" height="2.4" fill="white"/><circle cx="12" cy="12.2" r="0.7" fill="white"/>',
  },
  waterlogging: {
    color: '#3B82F6',
    label: 'Waterlogging',
    glyph: '<path d="M12 5.5c-1.9 2.3-3 4-3 5.5a3 3 0 0 0 6 0c0-1.5-1.1-3.2-3-5.5z" fill="white"/>',
  },
  missing_divider: {
    color: '#1F2937',
    label: 'Missing Divider',
    glyph: '<line x1="8" y1="7" x2="12" y2="13" stroke="white" stroke-width="1.3"/><line x1="16" y1="7" x2="12" y2="13" stroke="white" stroke-width="1.3"/><line x1="12" y1="13" x2="12" y2="16" stroke="white" stroke-width="1.3"/>',
  },
  missing_zebra_crossing: {
    color: '#8B5CF6',
    label: 'Missing Zebra Crossing',
    glyph: '<line x1="8" y1="7.5" x2="16" y2="7.5" stroke="white" stroke-width="1.2"/><line x1="8" y1="10" x2="16" y2="10" stroke="white" stroke-width="1.2"/><line x1="8" y1="12.5" x2="16" y2="12.5" stroke="white" stroke-width="1.2"/>',
  },
  missing_signage: {
    color: '#10B981',
    label: 'Damaged Signboard',
    glyph: '<line x1="12" y1="8.5" x2="12" y2="17" stroke="white" stroke-width="1.2"/><rect x="9" y="5.5" width="6" height="3.4" fill="none" stroke="white" stroke-width="1.1" transform="rotate(-18 12 7.2)"/>',
  },
  incident: {
    color: '#EC4899',
    label: 'Incident',
    glyph: '<rect x="11.4" y="6.5" width="1.2" height="4" fill="white"/><circle cx="12" cy="12" r="1" fill="white"/>',
  },
}

const FALLBACK_STYLE = { color: '#94A3B8', label: 'Other', glyph: '<circle cx="12" cy="10" r="2" fill="white"/>' }

// Markers render at ~60% of the previous size to cut down on clutter
// when many detections cluster close together.
function pinIcon(type) {
  const style = TYPE_STYLES[type] || FALLBACK_STYLE
  const html = `
    <svg width="17" height="22" viewBox="0 0 24 32" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 1px 1.5px rgba(0,0,0,0.5));">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 8.5 12 20 12 20s12-11.5 12-20c0-6.63-5.37-12-12-12z" fill="${style.color}"/>
      ${style.glyph}
    </svg>
  `
  return L.divIcon({
    className: 'detection-pin',
    html,
    iconSize: [17, 22],
    iconAnchor: [8.5, 22],
    popupAnchor: [0, -19],
  })
}

function Legend() {
  return (
    <div className="map-legend">
      {Object.entries(TYPE_STYLES).map(([type, style]) => (
        <div key={type} className="map-legend-row">
          <svg width="14" height="14" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="11" fill={style.color} />
          </svg>
          <span>{style.label}</span>
        </div>
      ))}
    </div>
  )
}

export default function LiveTracking() {
  const [detections, setDetections] = useState([])
  const [status, setStatus] = useState('loading')

  useEffect(() => {
    client.get('/detections')
      .then(res => { setDetections(res.data); setStatus('ready') })
      .catch(() => setStatus('error'))
  }, [])

  if (status === 'loading') return <LoadingState label="Loading detections…" />
  if (status === 'error') return <ErrorState message="Could not load detections." />

  return (
    <div className="page">
      <h1>Road Condition &amp; Infrastructure Map</h1>
      <div className="map-frame">
        <MapContainer center={DEFAULT_CENTER} zoom={13} style={{ height: '75vh', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; OpenStreetMap contributors"
          />
          {detections.map(d => (
            <Marker key={d.id} position={[d.lat, d.lng]} icon={pinIcon(d.type)}>
              <Popup>
                <strong>{(TYPE_STYLES[d.type] || FALLBACK_STYLE).label}</strong><br />
                Confidence: {(d.confidence * 100).toFixed(0)}%<br />
                Bus: {d.busId} · Route: {d.routeId}<br />
                {d.type === 'incident' && (
                  <Link to={`/incidents/${d.id}`}>View incident</Link>
                )}
              </Popup>
            </Marker>
          ))}
        </MapContainer>
        <Legend />
      </div>
    </div>
  )
}