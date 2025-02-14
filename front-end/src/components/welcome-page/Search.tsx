import '../../styles/search.css'

const Search = () => {
  return (
    <section className='search'>
        <div className="search__worker">
            <h1 className="title__search">Знайдіть Професіонала своєї справи</h1>
            <div className="search__worker__grp">
                <input type="text" placeholder='Знайдіть послугу...'/>
                <button><div className="btn__img"></div></button>
            </div>
        </div>
        <div className="search__services">
            <div className="search__services__cart">
                <div className="services__cart__img1"></div>
                <h3 className="services__cart__title"> Кухня &
                Сантехніка</h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img2"></div>
                <h3 className="services__cart__title"> Ванна  &
                Туалети</h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img3"></div>
                <h3 className="services__cart__title"> Сад </h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img4"></div>
                <h3 className="services__cart__title"> Будинок</h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img5"></div>
                <h3 className="services__cart__title"> Квартира</h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img6"></div>
                <h3 className="services__cart__title"> Техніка</h3>
            </div>
            <div className="search__services__cart">
                <div className="services__cart__img7"></div>
                <h3 className="services__cart__title"> Техніка</h3>
            </div>
        </div>
    </section>
  )
}

export default Search
