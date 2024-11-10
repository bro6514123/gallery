import cl from "./Photo.module.css"

const Photo = ({name, url}) => {
    return (
        <section className={cl.Photo}>
            <img className={cl.img} src={url} />
            <h3>{name}</h3>
        </section>
    )
}

export default Photo;
