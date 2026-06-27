type HistoryRecord = {
  timestamp: string;
  root_cause: string;
  namespace: string;
  confidence: number;
  status: string;
};

type Props = {
  history: HistoryRecord[];
};

export function HistoryTable({ history }: Props) {
  if (!history.length) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-5 text-slate-400">
        No previous investigations yet.
      </div>
    );
  }

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-5 overflow-x-auto">
      <h2 className="text-lg font-semibold text-white">Previous Investigations</h2>
      <table className="mt-4 w-full text-left text-sm text-slate-200">
        <thead>
          <tr className="border-b border-slate-800 text-slate-400">
            <th className="py-2">Timestamp</th>
            <th className="py-2">Root Cause</th>
            <th className="py-2">Namespace</th>
            <th className="py-2">Confidence</th>
            <th className="py-2">Status</th>
          </tr>
        </thead>
        <tbody>
          {history.map((item) => (
            <tr key={`${item.timestamp}-${item.root_cause}`} className="border-b border-slate-800">
              <td className="py-3 text-slate-300">{item.timestamp}</td>
              <td className="py-3 text-slate-300">{item.root_cause}</td>
              <td className="py-3 text-slate-300">{item.namespace}</td>
              <td className="py-3 text-slate-300">{item.confidence}%</td>
              <td className="py-3 text-slate-300">{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
