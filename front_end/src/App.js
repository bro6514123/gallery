import Header from "./components/Header/Header"
import Input from "./components/UI/Input/Input";
import Photo from "./components/Photo/Photo";
import Photos from "./API/Photos";
import {useMemo, useState} from "react";

function App() {
  const photos = Photos.getPhotos()
  const [search, setSearch] = useState("")
  
  const filterPhotos = useMemo(() => {
    return photos.filter(photo => photo[0].includes(search))
  }, [photos, search])

  return (
    <>  
        <Header>
            <Input value={search} setValue={setSearch} placeholder="search..." className="search_box" />
        </Header>
        <div className="App">
            {filterPhotos.map(photo => (
                <Photo name={photo[0]} url={photo[1]} />
            ))}           
        </div>
    </>
  );
}

export default App;
