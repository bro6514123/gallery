from flask import Flask

from database import Database


app = Flask(__name__)


try:
    database = Database()
except:
    database = None


@app.get("/")
def main():
    global database
    if not database:
        database = Database()

    return database.select_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
