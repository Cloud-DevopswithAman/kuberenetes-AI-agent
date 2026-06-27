import { getApiClient } from './api';

export type ProgressStep = {
  name: string;
  status: 'pending' | 'running' | 'completed';
};

export async function startInvestigation(token: string, namespace?: string) {
  const response = await getApiClient(token).post('/investigate', { namespace });
  return response.data;
}

export async function getProgress(token: string, progressId: string) {
  const response = await getApiClient(token).get(`/progress/${progressId}`);
  return response.data;
}

export async function getHistory(token: string) {
  const response = await getApiClient(token).get('/history');
  return response.data;
}
