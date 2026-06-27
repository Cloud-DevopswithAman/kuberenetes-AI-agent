import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 py-16 text-white">
      <section className="w-full max-w-3xl rounded-2xl border border-slate-800 bg-slate-900/80 p-10 shadow-2xl shadow-slate-950/40">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.35em] text-cyan-400">
          AI Kubernetes Agent
        </p>
        <h1 className="text-4xl font-semibold sm:text-5xl">
          Troubleshoot Kubernetes with AI
        </h1>
        <p className="mt-5 max-w-2xl text-lg text-slate-300">
          An on-demand troubleshooting workflow that investigates cluster issues and presents a clear diagnosis with suggested next steps.
        </p>

        <div className="mt-8 flex flex-wrap gap-4">
          <button className="rounded-full bg-cyan-500 px-6 py-3 font-medium text-slate-950 transition hover:bg-cyan-400">
            Investigate Cluster
          </button>
          <Link
            href="http://localhost:8000/health"
            className="rounded-full border border-slate-700 px-6 py-3 font-medium text-slate-200 transition hover:border-cyan-400 hover:text-cyan-300"
          >
            Check Backend Health
          </Link>
        </div>

        <div className="mt-10 grid gap-4 sm:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-5">
            <p className="text-sm text-slate-400">System Status</p>
            <p className="mt-2 text-xl font-semibold text-emerald-400">Ready</p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-5">
            <p className="text-sm text-slate-400">Current Mode</p>
            <p className="mt-2 text-xl font-semibold text-slate-100">Foundation Setup</p>
          </div>
        </div>
      </section>
    </main>
  );
}
