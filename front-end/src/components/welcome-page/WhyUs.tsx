import "../../styles/whyUs.css"

const WhyUs = () => {
  return (
    <section className="why__us">
        <div className="why__us__container">
            <div className="why__us__title__container">
                <h1 className="why__us__title">BRIGADIR.com</h1>
                <h2 className="why__us__subtitle">Якісні послуги <span>професіоналів</span> – швидко та надійно. Без зайвих турбот та незручностей для вас.</h2>
            </div>
            <div className="why__us__content__container">
                <div className="why__us__txt__container">
                    <div className="why__us__txt__grp">
                        <div className="why__us__cart">
                            <div className="why__us__cart__img"></div>
                            <h3>Безпека</h3>
                            <p>Кожен виконавець підтверджує свою особу 
                            з нашим працівником </p>
                        </div>
                        <div className="why__us__cart">
                            <div className="why__us__cart__img"></div>
                            <h3>Простота</h3>
                            <p>Замовте будь якого майстра  
                            в декілька кліків просто та швидко</p>
                        </div>
                    </div>
                    <div className="why__us__txt__grp">
                        <div className="why__us__cart">
                            <div className="why__us__cart__img"></div>
                            <h3>Функціонал</h3>
                            <p>У нас ви точно знайдете майстра який виконає 
                            будь яку вашу поломку чи роботу</p>
                        </div>
                        <div className="why__us__cart">
                            <div className="why__us__cart__img"></div>
                            <h3>Якість</h3>
                            <p>З системою оцінювання ви зможете 
                            самі обрати кваліфікованого виконавця </p>
                        </div>
                    </div>
                </div>
                <div className="why__us__img__container">
                    <div className="why__us__img"></div>
                </div>
            </div>
        </div>
    </section>
  )
}

export default WhyUs
