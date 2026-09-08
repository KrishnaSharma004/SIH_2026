import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client'
import LoadingState, { ErrorState } from '../components/LoadingState'

export default function AdminPanel() {
  const [records, setRecords] = useState([])
  const [status, setStatus] = useState('loading')
  const [filterType, setFilterType] = useState('all')

  useEffect(() => {
    client.get('/detections')
      .then(res => { setRecords(res.data); setStatus('ready') })
      .catch(() => setStatus('error'))
  }, [])

  if (status === 'loading') return <LoadingState label="Loading records…" />
  if (status === 'error') return <ErrorState message="Could not load records." />

  const types = ['all', ...new Set(records.map(r => r.type))]
  const filtered = filterType === 'all' ? records : records.filter(r => r.type === filterType)

  return (
    <div className="page">
      <h1>Admin Panel</h1>
      <div className="controls">
        {types.map(t => (
          <button key={t} className={t === filterType ? 'active' : ''} onClick={() => setFilterType(t)}>
            {t}
          </button>
        ))}
      </div>
      <table className="admin-table">
        <thead>
          <tr><th>ID</th><th>Type</th><th>Confidence</th><th>Bus</th><th>Timestamp</th><th></th></tr>
        </thead>
        <tbody>
          {filtered.map(r => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.type}</td>
              <td>{(r.confidence * 100).toFixed(0)}%</td>
              <td>{r.busId}</td>
              <td>{r.timestamp}</td>
              <td>{r.type === 'incident' && <Link to={`/incidents/${r.id}`}>View</Link>}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
