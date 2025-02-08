import '../../styles/gallery.css'

const Gallery = () => {
  return (
    <section className='gallery'>
        <div className="gallery__title__container">
            <h1>Зроблено за допомогою BRIGADIR</h1>
        </div>
        <div className="gallery__container">
            <div className="gallery__grp1">
                <div className="gallery__grp3">
                    <div className="gallery__img3"></div>
                    <div className="gallery__img4"></div>
                    <div className="gallery__img5"></div>
                </div>
                <div className="gallery__grp4">
                    <div className="gallery__grp5">
                        <div className="gallery__img6"></div>
                        <div className="gallery__img7"></div>
                    </div>
                    <div className="gallery__grp6">
                        <div className="gallery__img8"></div>
                        <div className="gallery__img9"></div>
                    </div>
                </div>
            </div>
            <div className="gallery__grp2">
                <div className="gallery__img1"></div>
                <div className="gallery__img2"></div>
            </div>
        </div>
    </section>
  )
}

export default Gallery
