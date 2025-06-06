import React from "react";

interface MindTreeProps {
  data: number[];
}

export function MindTree({ data }: MindTreeProps) {
  // Mock vizualizácia: jednoduchý horizontálny bar chart
  if (!data || !Array.isArray(data)) return null;
  const max = Math.max(...data, 1);
  return (
    <div className="bg-zinc-900 rounded-2xl p-6 shadow-glass border border-white/10">
      <div className="text-lg font-semibold mb-2 text-aethero-blue">MindTree – Vektor zámeru</div>
      <div className="space-y-2">
        {data.map((v, i) => (
          <div key={i} className="flex items-center">
            <div className="w-24 text-xs text-white/60">Intent {i + 1}</div>
            <div className="flex-1 h-3 bg-gradient-to-r from-aethero-blue to-aethero-purple rounded-full mx-2">
              <div
                className="h-3 rounded-full bg-aethero-pink shadow-neon"
                style={{ width: `${(v / max) * 100}%` }}
              />
            </div>
            <div className="w-10 text-right text-xs text-white/80">{v.toFixed(2)}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
