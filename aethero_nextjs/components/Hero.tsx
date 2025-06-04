import React from "react";

const slogans = [
  "AetheroOS – vedomý operačný systém novej civilizácie",
  "Modularita. Presnosť. Sebauvedomenie.",
  "Riadený Ústavou, poháňaný Introspekciou."
];

export default function Hero() {
  return (
    <section className="relative flex flex-col items-center justify-center min-h-[60vh] py-16 px-4 text-center bg-gradient-to-br from-aethero-blue via-aethero-purple to-aethero-pink">
      <div className="backdrop-blur-md bg-aethero-glass rounded-3xl shadow-glass p-10 max-w-3xl mx-auto border border-white/20">
        <h1 className="text-5xl md:text-6xl font-extrabold text-white drop-shadow-neon mb-6">
          Welcome to <span className="text-aethero-blue">AetheroOS</span>
        </h1>
        <div className="text-xl md:text-2xl text-white/80 font-light mb-8 space-y-2">
          {slogans.map((s, i) => (
            <div key={i}>{s}</div>
          ))}
        </div>
      </div>
    </section>
  );
}
