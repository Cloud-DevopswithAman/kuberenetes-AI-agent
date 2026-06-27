import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 py-16 text-white">
      <section className="w-full max-w-3xl rounded-3xl border border-slate-800 bg-slate-900/90 p-10 shadow-2xl shadow-slate-950/40">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.35em] text-cyan-400">
          AI Kubernetes Agent
        </p>
        <h1 className="text-4xl font-semibold sm:text-5xl">Kubernetes Troubleshooting for SREs</h1>
        <p className="mt-5 max-w-2xl text-lg text-slate-300">
          Sign in to investigate cluster issues, track evidence, and receive AI-powered diagnosis from a Senior Kubernetes SRE experience.
        </p>

        <div className="mt-8 flex flex-col gap-4 sm:flex-row">
          <Link
            href="/login"
            className="inline-flex items-center justify-center rounded-full bg-cyan-500 px-6 py-3 text-base font-semibold text-slate-950 transition hover:bg-cyan-400"
          >
            Sign In
          </Link>
          <Link
            href="http://localhost:8000/health"
            className="inline-flex items-center justify-center rounded-full border border-slate-700 px-6 py-3 text-base font-medium text-slate-200 transition hover:border-cyan-400 hover:text-cyan-300"
          >
            Backend Health
          </Link>
        </div>
      </section>
    </main>
  );
}
