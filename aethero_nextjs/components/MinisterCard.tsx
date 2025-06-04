import React from "react";

type Minister = {
  name: string;
  intent_vector: string;
  ethical_index: number;
  activity: string;
};

export default function MinisterCard({ minister }: { minister: Minister }) {
  return (
    <div className="bg-aethero-glass rounded-xl shadow-glass p-6 border border-white/10 flex flex-col items-center text-center min-w-[220px]">
      <h2 className="text-2xl font-bold text-aethero-blue mb-2">{minister.name}</h2>
      <div className="text-sm text-white/80 mb-1">Intent: <span className="font-mono">{minister.intent_vector}</span></div>
      <div className="text-sm text-aethero-neon mb-1">Etický index: {minister.ethical_index}</div>
      <div className="text-xs text-white/60 italic">{minister.activity}</div>
    </div>
  );
}
