import React from 'react'

const Hero: React.FC = () => {
  console.log('🚀 Hero komponent sa vykresľuje')

  return (
    <section className="bg-spacegrey text-cream flex min-h-[60vh] flex-col items-center justify-center px-4 py-20">
      <h1 className="mb-6 animate-pulse text-5xl font-bold tracking-tight md:text-7xl">
        AetheroOS
      </h1>
      <p className="mb-8 max-w-2xl text-center text-xl italic opacity-90 md:text-2xl">
        „Vedomie je proces, nie stav. Syntéza je jeho prvý krok.“
      </p>
      <div className="flex gap-4">
        <a
          href="#about"
          className="bg-electricgreen hover:bg-energeticyellow rounded-lg px-6 py-3 font-semibold text-black shadow-lg transition"
        >
          Zisti viac
        </a>
        <a
          href="#timeline"
          className="bg-aetherorange hover:bg-electricgreen rounded-lg px-6 py-3 font-semibold text-white shadow-lg transition"
        >
          Pozri timeline
        </a>
      </div>
    </section>
  )
}

export default Hero
