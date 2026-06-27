type StatusCardProps = {
  title: string;
  value: string;
  tone?: 'neutral' | 'success';
};

export function StatusCard({ title, value, tone = 'neutral' }: StatusCardProps) {
  const toneClasses = tone === 'success' ? 'text-emerald-400' : 'text-slate-100';

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-5">
      <p className="text-sm text-slate-400">{title}</p>
      <p className={`mt-2 text-xl font-semibold ${toneClasses}`}>{value}</p>
    </div>
  );
}
