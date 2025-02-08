import '../styles/main.css'
import Gallery from './welcome-page/Gallery'
import Header from './welcome-page/Header'
import Search from './welcome-page/Search'
import Services from './welcome-page/Services'
import WhyUs from './welcome-page/WhyUs'

const WelcomePage = () => {
  return (
    <main className='welcome__page'>
        <Header/>
        <Search/>
        <Services/>
        <WhyUs/>
        <Gallery/>
    </main>
  )
}

export default WelcomePage
