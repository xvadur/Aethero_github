import React from "react";

interface EmotionChartProps {
  data: Record<string, number>;
}

const emotionColors: Record<string, string> = {
  joy: "bg-yellow-400",
  sadness: "bg-blue-400",
  anger: "bg-red-500",
  fear: "bg-purple-500",
  surprise: "bg-pink-400",
  disgust: "bg-green-500",
  // ...pridať ďalšie emócie podľa potreby
};

export function EmotionChart({ data }: EmotionChartProps) {
  if (!data) return null;
  const entries = Object.entries(data);
  const max = Math.max(...entries.map(([_, v]) => v), 1);
  return (
    <div className="bg-zinc-900 rounded-2xl p-6 shadow-glass border border-white/10">
      <div className="text-lg font-semibold mb-2 text-aethero-pink">Emotion Chart</div>
      <div className="space-y-2">
        {entries.map(([emotion, value]) => (
          <div key={emotion} className="flex items-center">
            <div className="w-24 text-xs text-white/60 capitalize">{emotion}</div>
            <div className="flex-1 h-3 bg-zinc-800 rounded-full mx-2">
              <div
                className={`h-3 rounded-full shadow-neon ${emotionColors[emotion] || 'bg-white/30'}`}
                style={{ width: `${(value / max) * 100}%` }}
              />
            </div>
            <div className="w-10 text-right text-xs text-white/80">{(value * 100).toFixed(0)}%</div>
          </div>
        ))}
      </div>
    </div>
  );
}
