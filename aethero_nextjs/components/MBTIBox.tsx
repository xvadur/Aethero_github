import React from "react";

interface MBTIBoxProps {
  type: string;
}

const mbtiColors: Record<string, string> = {
  INFJ: "from-purple-500 via-blue-500 to-pink-400",
  ENTP: "from-green-400 via-blue-500 to-purple-500",
  INTJ: "from-indigo-600 via-purple-600 to-pink-500",
  // ...pridať ďalšie typy podľa potreby
};

export function MBTIBox({ type }: MBTIBoxProps) {
  const gradient = mbtiColors[type] || "from-gray-700 via-gray-800 to-gray-900";
  return (
    <div
      className={`rounded-2xl p-6 shadow-glass border border-white/10 bg-gradient-to-br ${gradient} flex flex-col items-center justify-center max-w-xs mx-auto`}
    >
      <div className="text-4xl font-extrabold tracking-widest text-white drop-shadow-neon mb-2">
        {type}
      </div>
      <div className="uppercase text-xs text-white/70 tracking-wider">MBTI odhad</div>
    </div>
  );
}
