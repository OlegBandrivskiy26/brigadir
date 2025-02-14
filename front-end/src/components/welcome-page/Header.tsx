import { NavLink } from 'react-router-dom'
import '../../styles/header.css'

const Header = () => {
  return (
    <header>
        <div className="header__container">
            <div className="logo"></div>
            <div className="nav__menu">
                <h4 className='nav__items'>Стати Виконавцем</h4>
                <h4 className='nav__items'>Знайти Виконавця</h4>
                <h4 className='nav__items'>Відгуки</h4>
                
            </div>
            <div className="search__grp">
                <input type="text" placeholder='Пошук...' className='search__input'/>
                <button className="btn__search"><div className="btn__icon"></div></button>
            </div>
            <div className="btn__grp__header">
                <NavLink to={'/log-in'}><button className='header__btn'>Log In</button></NavLink>
                <NavLink to={'/role-selection'}><button className='header__btn blue__btn'>Sign Up</button></NavLink>
            </div>
        </div>
    </header>
  )
}

export default Header
