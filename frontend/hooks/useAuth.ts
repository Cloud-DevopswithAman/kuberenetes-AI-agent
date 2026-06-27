'use client';

import { useEffect, useState } from 'react';

export function useAuth() {
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const stored = window.localStorage.getItem('ai-kubernetes-token');
    setToken(stored);
    setLoading(false);
  }, []);

  function saveToken(value: string) {
    window.localStorage.setItem('ai-kubernetes-token', value);
    setToken(value);
  }

  function logout() {
    window.localStorage.removeItem('ai-kubernetes-token');
    setToken(null);
  }

  return { token, loading, saveToken, logout };
}
