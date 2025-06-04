import React from 'react';
import Hero from '../components/Hero';
import MinisterCard from '../components/MinisterCard';
import ministers from '../data/ministers/sample.json';

export default function Home() {
  return (
    <main className="min-h-screen bg-[#0a0a0a] text-[#f5f5f5] font-[Inter,sans-serif] flex flex-col justify-center items-center">
      <Hero />
      {/* Ministers grid - dynamicky */}
      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 w-full max-w-5xl mb-16 mt-8">
        {ministers.map((minister, idx) => (
          <MinisterCard key={minister.name + idx} minister={minister} />
        ))}
      </section>
      {/* Footer */}
      <footer className="w-full text-center py-6 text-[#888] text-sm border-t border-white/10">
        &copy; 2025 AetheroOS – Orchestrated by Prezident | <a href="#" className="underline hover:text-[#39FF14]">Kontakt</a> | <a href="https://github.com/xvadur/Aethero_github" className="underline hover:text-[#FFD1DC]">GitHub</a>
      </footer>
      {/* Inter font import */}
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet" />
    </main>
  );
}
