'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../../hooks/useAuth';
import { startInvestigation, getHistory, getProgress, ProgressStep } from '../../services/investigation';
import { DiagnosisCard } from '../../components/DiagnosisCard';
import { HistoryTable } from '../../components/HistoryTable';
import { ProgressList } from '../../components/ProgressList';

const initialSteps: ProgressStep[] = [
  { name: 'Checking Pods', status: 'pending' },
  { name: 'Reading Logs', status: 'pending' },
  { name: 'Analyzing Events', status: 'pending' },
  { name: 'Inspecting Deployments', status: 'pending' },
  { name: 'Checking Networking', status: 'pending' },
  { name: 'AI Reasoning', status: 'pending' },
  { name: 'Diagnosis Complete', status: 'pending' },
];

export default function DashboardPage() {
  const router = useRouter();
  const { token, loading, logout } = useAuth();
  const [investigationState, setInvestigationState] = useState<any>(null);
  const [steps, setSteps] = useState<ProgressStep[]>(initialSteps);
  const [history, setHistory] = useState<any[]>([]);
  const [statusMessage, setStatusMessage] = useState('Ready');
  const [running, setRunning] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!loading && !token) {
      router.replace('/login');
    }
  }, [loading, token, router]);

  useEffect(() => {
    if (!token) {
      return;
    }

    async function loadHistory() {
      try {
        const response = await getHistory(token);
        setHistory(response.history ?? []);
      } catch {
        setHistory([]);
      }
    }

    loadHistory();
  }, [token]);

  async function fetchProgress(progressId: string) {
    if (!token) {
      return;
    }

    try {
      const response = await getProgress(token, progressId);
      const progress = response.progress;
      if (progress?.steps) {
        setSteps(progress.steps);
      }
      if (progress?.completed) {
        setRunning(false);
      }
    } catch (err) {
      console.error(err);
    }
  }

  async function handleInvestigate() {
    if (!token) {
      return;
    }

    setError('');
    setRunning(true);
    setStatusMessage('Starting investigation...');
    setSteps(initialSteps);
    setInvestigationState(null);

    try {
      const response = await startInvestigation(token, 'default');
      setInvestigationState(response);
      setStatusMessage('Investigation complete. Fetching diagnosis...');

      if (response.investigation_id) {
        await fetchProgress(response.investigation_id);
        const interval = setInterval(() => {
          fetchProgress(response.investigation_id);
        }, 1200);

        setTimeout(() => {
          clearInterval(interval);
        }, 12000);
      }
    } catch (err) {
      setError('Investigation failed. Please try again.');
      setStatusMessage('Error during investigation.');
    } finally {
      setRunning(false);
    }
  }

  function handleLogout() {
    logout();
    router.replace('/login');
  }

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-10 text-white">
      <div className="mx-auto max-w-6xl">
        <header className="mb-10 flex flex-col gap-4 rounded-3xl border border-slate-800 bg-slate-900/90 p-6 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-cyan-400">AI Kubernetes Agent</p>
            <h1 className="mt-3 text-4xl font-semibold">Kubernetes Investigation Dashboard</h1>
          </div>
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
            <button
              onClick={handleInvestigate}
              disabled={running}
              className="rounded-full bg-cyan-500 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-50"
            >
              {running ? 'Investigating…' : 'Investigate Cluster'}
            </button>
            <button
              onClick={handleLogout}
              className="rounded-full border border-slate-700 px-6 py-3 text-slate-200 transition hover:border-cyan-400 hover:text-cyan-300"
            >
              Logout
            </button>
          </div>
        </header>

        <div className="grid gap-6 xl:grid-cols-[1.4fr_0.9fr]">
          <section className="space-y-6">
            <div className="rounded-3xl border border-slate-800 bg-slate-900/90 p-6">
              <p className="text-sm uppercase tracking-[0.35em] text-slate-400">Status</p>
              <p className="mt-3 text-2xl font-semibold text-white">{statusMessage}</p>
              {error ? <p className="mt-3 text-sm text-rose-400">{error}</p> : null}
            </div>

            <ProgressList steps={steps} />

            <DiagnosisCard diagnosis={investigationState?.diagnosis ?? null} />
          </section>

          <section className="space-y-6">
            <div className="rounded-3xl border border-slate-800 bg-slate-900/90 p-6">
              <p className="text-sm uppercase tracking-[0.35em] text-slate-400">Recent Investigations</p>
              <p className="mt-3 text-sm text-slate-300">Latest history is shown below after investigations complete.</p>
            </div>
            <HistoryTable history={history} />
          </section>
        </div>
      </div>
    </main>
  );
}
