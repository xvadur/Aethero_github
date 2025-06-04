module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ["Inter", "sans-serif"],
        sf: ["SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", "sans-serif"]
      },
      colors: {
        aethero: {
          blue: "#00CFFF",
          purple: "#7B61FF",
          pink: "#FF61D2",
          neon: "#39FF14",
          glass: "rgba(255,255,255,0.15)",
          dark: "#18181B"
        }
      },
      boxShadow: {
        glass: "0 8px 32px 0 rgba(31, 38, 135, 0.37)",
        neon: "0 0 8px #39FF14, 0 0 16px #00CFFF"
      },
      backdropBlur: {
        xs: '2px',
      },
      backgroundImage: {
        'hero-gradient': 'linear-gradient(135deg, #00CFFF 0%, #7B61FF 100%)',
        'glass-gradient': 'linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(123,97,255,0.15) 100%)'
      }
    }
  },
  plugins: [require('@tailwindcss/forms'), require('@tailwindcss/typography')],
};
