import React from 'react'
import { NavLink } from 'react-router-dom'
import "../../styles/registration.css"

const RegistrationEmployer = () => {
  return (
    <section className='reg__employer'>
      <div className="reg__employer__container">
        <h1 className='reg__employer__title'>Знайдіть найкращого майстра!</h1>
        <form method='get' className='form__registration'>
          <div className="name__grp">
            <div className="input__container">
              <label htmlFor="username">Ім'я</label>
              <input type="text" className='small__input'/>
            </div>
            <div className="input__container">
              <label htmlFor="usersurname">Прізвище</label>
              <input type="text" className='small__input'/>
            </div>
          </div>
          <div className="input__container">
            <label htmlFor="useremail">Електронна пошта чи номер телефону</label>
            <input type="text" className="large__input" />
          </div>
          <div className="input__container">
            <label htmlFor="useremail">Пароль</label>
            <input type="text" className="large__input" />
          </div>
          <div className="input__container">
            <label htmlFor="useremail">Підтвердіть пароль</label>
            <input type="text" className="large__input" />
          </div>
          <button className='btn__resume'>Продовжити</button>
          <NavLink to={'/log-in'} className="link__login">У вас вже є акаунт? <span>Увійдіть</span></NavLink>
        </form>
      </div>
    </section>
  )
}

export default RegistrationEmployer
