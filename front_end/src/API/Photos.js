import axios from "axios";

class Photos {
    static async getPhotos() {
        try {
            const resp = await axios.get("http://localhost:5000")
            return resp.data
        } catch (error) {
            console.log(error)
            return []
        }
    }
    static async addPhotos() {
        try {
            const response = await axios.post("http://localhost:5000", {
                name: "test",
                url: "url"
            }, {});
            console.log("Response:", response);
        } catch (error) {
            console.error("Error details:", error.toJSON());
        }
    }
    
}

export default Photos;
