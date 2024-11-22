import { useEffect, useMemo, useState } from "react";
import Header from "../Header/Header";
import Input from "../UI/Input/Input";
import Photo from "../Photo/Photo";
import Photos from "../../API/Photos";

const MainPage = () => {
  const [photos, setPhotos] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    async function fetchPhotos() {
      const response = await Photos.getPhotos();
      setPhotos(response);
    }
    fetchPhotos();
  }, [])

  const filteredPhotos = useMemo(() => {
    return photos.filter(photo => photo.name.includes(search));
  }, [photos, search]);

  return (
    <>  
        <Header>
            <Input value={search} setValue={setSearch} placeholder="search..." className="search_box" />
        </Header>
        <div className="MainPage">
            {filteredPhotos.map(photo => (
                <Photo name={photo.name} url={photo.url} />
            ))}           
        </div>
    </>
  );
}

export default MainPage;