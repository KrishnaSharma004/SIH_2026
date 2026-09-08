export default function LoadingState({ label = 'Loading…' }) {
  return <div className="loading-state">{label}</div>
}

export function ErrorState({ message = 'Something went wrong.' }) {
  return <div className="error-state">{message}</div>
}
