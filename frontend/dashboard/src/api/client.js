import axios from 'axios'

// Change VITE_API_BASE_URL in a .env file once B1's real backend is live —
// nothing else in the app needs to change.
const client = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:3001',
})

export default client
