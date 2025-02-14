import { NavLink } from "react-router-dom";
import "../styles/login.css";

const LogIn = () => {
  return (
    <section className="logIn">
      <form method="get" className="form__login">
        <div className="form__container__login">
          <h1 className="login__title">Увійдіть у BRIGADIR</h1>

          <div className="input-container">
            <div className="input-icon" ></div>
            <input type="text" placeholder="Електронна пошта" className="input__login" />
          </div>

          <div className="input-container">
            <div className="input-icon input__icon__password" ></div>
            <input type="password" placeholder="Пароль" className="input__login" />
          </div>
          <button className="btn__login">Продовжити</button>
          <NavLink to="/role-selection" className="link">
            Ще немає акаунта ? <span>Реєстрація</span>
          </NavLink>
          <NavLink className="remember__pasword" to="/">Забули пароль?</NavLink>
        </div>
      </form>
    </section>
  );
};

export default LogIn;
