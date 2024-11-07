import os
from random import randint

from flask import Flask, request
from flask_cors import CORS

from database import database


app = Flask(__name__)
CORS(app)

upload_folder = "/static/img/"
server_host = "http://127.0.0.1"
server_port = "5000"

database.create_DB_and_table()

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)


@app.route("/", methods=["GET", "POST"])
async def categorie():
    if request.method == "GET":
        return await database.select_all()
    
    elif request.method == "POST":
        name = request.form.get("name")
        method = request.form.get("method")

        names= await database.select_all_names()
        if (name, ) in names:
            return "it's name ...", 403

        if method == "file":
            file = request.files.get("file")
            file_path = os.path.join(f".{upload_folder}", file.filename)
            file.save(file_path)
            await database.insert(name=name, url=f"{server_host}:{server_port}{upload_folder}{file.filename}")

        elif method == "url":
            url = request.form.get("url")
            await database.insert(name=name, url=url)
        
        else:
            return "undefined method", 301
        
        return "OK!!!", 200
    
@app.get("/temp")
def temp():
    return "<img src='./static/img/Google__G__logo.svg.png' />"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)