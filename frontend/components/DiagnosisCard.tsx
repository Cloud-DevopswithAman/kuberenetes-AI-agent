type Diagnosis = {
  root_cause: string;
  explanation: string;
  fix: string;
  kubectl_command: string;
  confidence: number;
};

type Props = {
  diagnosis: Diagnosis | null;
};

export function DiagnosisCard({ diagnosis }: Props) {
  if (!diagnosis) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-5 text-slate-400">
        No diagnosis available yet.
      </div>
    );
  }

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-5">
      <h2 className="text-lg font-semibold text-white">Diagnosis</h2>
      <div className="mt-4 space-y-4 text-slate-200">
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Root Cause</p>
          <p className="mt-2 text-base text-white">{diagnosis.root_cause}</p>
        </div>
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Explanation</p>
          <p className="mt-2 text-base text-slate-200">{diagnosis.explanation}</p>
        </div>
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Suggested Fix</p>
          <p className="mt-2 text-base text-slate-200">{diagnosis.fix}</p>
        </div>
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Command</p>
          <p className="mt-2 text-base text-slate-200">{diagnosis.kubectl_command}</p>
        </div>
        <div className="rounded-xl bg-slate-900 p-4">
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Confidence</p>
          <p className="mt-2 text-2xl font-semibold text-emerald-400">{diagnosis.confidence}%</p>
        </div>
      </div>
    </div>
  );
}
