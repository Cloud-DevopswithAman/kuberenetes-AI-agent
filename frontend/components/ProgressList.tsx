type ProgressStep = {
  name: string;
  status: 'pending' | 'running' | 'completed';
};

type Props = {
  steps: ProgressStep[];
};

export function ProgressList({ steps }: Props) {
  return (
    <div className="space-y-3 rounded-2xl border border-slate-800 bg-slate-950/80 p-5">
      <h2 className="text-lg font-semibold text-white">Investigation Status</h2>
      <div className="space-y-2 pt-3">
        {steps.map((step) => (
          <div key={step.name} className="flex items-center justify-between rounded-xl bg-slate-900 p-3">
            <span className="text-slate-200">{step.name}</span>
            <span
              className={`rounded-full px-3 py-1 text-xs font-semibold ${
                step.status === 'completed'
                  ? 'bg-emerald-500 text-slate-950'
                  : step.status === 'running'
                  ? 'bg-cyan-500 text-slate-950'
                  : 'bg-slate-700 text-slate-300'
              }`}
            >
              {step.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
