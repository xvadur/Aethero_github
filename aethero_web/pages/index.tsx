import Hero from '../components/Hero'

console.log('🟢 Hero komponent sa pokúša renderovať')

const Home: React.FC = () => {
  return (
    <>
      <div>🧪 Debug: stránka beží</div>
      <Hero />
      {/* Ďalšie sekcie a komponenty môžu nasledovať tu */}
    </>
  )
}

export default Home
