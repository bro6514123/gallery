from flask import Flask, request
from flask_cors import CORS

from database import Database


app = Flask(__name__)
CORS(app)


try:
    database = Database()
except:
    database = None


@app.route("/", methods=["GET", "POST"])
def main():
    global database
    if not database:
        database = Database()

    if request.method == "GET":
        return database.select_all(), 200
    elif request.method == "POST":
        data = request.json
        try:   
            if data["name"] and data["url"]:
                database.add(data["name"], data["url"])
                return f"{data}", 200
            return f"{data}", 201
        except:
            return f"{data}", 301
    
    print("its")
    return "no ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
