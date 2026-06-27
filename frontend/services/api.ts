import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
});

export async function getHealthStatus() {
  const response = await api.get('/health');
  return response.data;
}
