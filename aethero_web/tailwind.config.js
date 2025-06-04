/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './data/**/*.{md,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        spacegrey: '#1E1E1E',
        cream: '#F5F5DC',
        electricgreen: '#39FF14',
        energeticyellow: '#FFD700',
        aetherorange: '#FF6F00',
        white: '#FFFFFF',
        black: '#000000',
      },
    },
  },
  plugins: [],
}
