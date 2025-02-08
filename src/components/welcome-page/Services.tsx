import "../../styles/services.css"

const Services = () => {
  return (
    <section className="services">
      <div className="services__container">
        <div className="services__title__container">
          <h1 className="services__title">Популярні Сервіси</h1>
        </div>
        <div className="services__cart__container">
          <div className="cart__services">
            <h3>Стрижка <br />
            газону</h3>
            <div className="cart__services__img cart__services__img1 "></div>
          </div>
          <div className="cart__services cart__red">
            <h3>Укладка  <br />
            бруківки</h3>
            <div className="cart__services__img cart__services__img2"></div>
          </div>
          <div className="cart__services cart__yellow">
            <h3>Ремонт <br /> шафи</h3>
            <div className="cart__services__img cart__services__img3"></div>
          </div>
          <div className="cart__services cart__blue">
            <h3>Шпаклювання  <br />
            стін</h3>
            <div className="cart__services__img cart__services__img4"></div>
          </div>
          <div className="cart__services cart__violet">
            <h3>Ремонт <br />
            техніки</h3>
            <div className="cart__services__img cart__services__img5"></div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Services
