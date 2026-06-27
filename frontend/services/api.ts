import axios, { AxiosInstance } from 'axios';

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

export function getApiClient(token?: string): AxiosInstance {
  const headers: Record<string, string> = {};
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  return axios.create({
    baseURL: BASE_URL,
    timeout: 20000,
    headers,
  });
}

export async function getHealthStatus() {
  const response = await getApiClient().get('/health');
  return response.data;
}
