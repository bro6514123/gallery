from flask import Flask

from database import Database


app = Flask(__name__)


@app.get("/")
def main():
    database = Database()
    return "<h1>Hello World</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
