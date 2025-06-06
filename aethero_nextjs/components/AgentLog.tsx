import React from "react";

interface AgentLogProps {
  entries: Array<{ agent: string; message: string; timestamp?: number }>;
}

export function AgentLog({ entries }: AgentLogProps) {
  if (!entries || !entries.length) return null;
  return (
    <div className="bg-zinc-900 rounded-2xl p-6 shadow-glass border border-white/10">
      <div className="text-lg font-semibold mb-2 text-aethero-purple">Agent Log</div>
      <ul className="space-y-2">
        {entries.map((entry, i) => (
          <li key={i} className="flex items-start gap-3">
            <span className="font-bold text-aethero-blue">{entry.agent}:</span>
            <span className="text-white/90">{entry.message}</span>
            {entry.timestamp && (
              <span className="ml-auto text-xs text-white/40">{new Date(entry.timestamp).toLocaleTimeString()}</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
