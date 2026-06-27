import { getApiClient } from './api';

export type LoginResponse = {
  access_token: string;
  token_type: string;
  user: { username: string };
};

export async function login(username: string, password: string) {
  const response = await getApiClient().post('/auth/login', { username, password });
  return response.data as LoginResponse;
}

export async function getProfile(token: string | null) {
  if (!token) {
    return null;
  }
  const response = await getApiClient(token).get('/auth/me');
  return response.data;
}
