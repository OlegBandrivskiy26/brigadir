import '../styles/main.css'
import Gallery from './welcome-page/Gallery'
import Header from './welcome-page/Header'
import Search from './welcome-page/Search'
import Services from './welcome-page/Services'
import WhyUs from './welcome-page/WhyUs'
import Footer from './welcome-page/footer' // Додаємо Footer

const WelcomePage = () => {
  return (
    <main className='welcome__page'>
        <Header/>
        <Search/>
        <Services/>
        <WhyUs/>
        <Gallery/>
        <Footer/> {/* Додаємо Footer в кінець сторінки */}
    </main>
  )
}

export default WelcomePage
