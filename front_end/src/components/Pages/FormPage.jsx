import { useState } from "react";
import Input from "../UI/Input/Input";
import Photos from "../../API/Photos";

const FormPage = () => {
    const [name, setName] = useState("");
    const [url, setUrl] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();  // Перешкоджає перезавантаженню сторінки
        await Photos.addPhotos(name, url);  // Викликаємо метод з параметрами name і url
        setName("");
        setUrl("");
    };

    return (
        <form onSubmit={handleSubmit} style={{ margin: "auto" }}>
            <Input value={name} setValue={setName} placeholder="name" />
            <Input value={url} setValue={setUrl} placeholder="url" />
            <button type="submit">submit</button>
        </form>
    );
};

export default FormPage;