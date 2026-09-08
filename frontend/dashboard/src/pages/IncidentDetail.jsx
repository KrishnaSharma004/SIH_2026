import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import client from '../api/client'
import LoadingState, { ErrorState } from '../components/LoadingState'

export default function IncidentDetail() {
  const { id } = useParams()
  const [incident, setIncident] = useState(null)
  const [status, setStatus] = useState('loading')
  const [workOrderStatus, setWorkOrderStatus] = useState('idle')

  useEffect(() => {
    client.get(`/incidents/${id}`)
      .then(res => { setIncident(res.data); setStatus('ready') })
      .catch(() => setStatus('error'))
  }, [id])

  const createWorkOrder = () => {
    setWorkOrderStatus('creating')
    client.post('/workorders', { incidentId: id })
      .then(() => setWorkOrderStatus('created'))
      .catch(() => setWorkOrderStatus('error'))
  }

  if (status === 'loading') return <LoadingState label="Loading incident…" />
  if (status === 'error' || !incident) return <ErrorState message="Incident not found." />

  return (
    <div className="page">
      <Link to="/">&larr; Back to map</Link>
      <h1>Incident {incident.id}</h1>
      <div className="incident-card">
        <p><strong>Type:</strong> {incident.type}</p>
        <p><strong>Plate:</strong> {incident.plateNumber}</p>
        <p><strong>Confidence:</strong> {(incident.confidence * 100).toFixed(0)}%</p>
        <p><strong>Timestamp:</strong> {incident.timestamp}</p>
        <p><strong>Location:</strong> {incident.lat}, {incident.lng}</p>
        {incident.evidenceImageUrl && (
          <img src={incident.evidenceImageUrl} alt="Evidence" className="evidence-img" />
        )}
        <button onClick={createWorkOrder} disabled={workOrderStatus === 'creating'}>
          {workOrderStatus === 'created' ? 'Work order created ✓' : 'Create work order'}
        </button>
        {workOrderStatus === 'error' && <ErrorState message="Could not create work order." />}
      </div>
    </div>
  )
}
