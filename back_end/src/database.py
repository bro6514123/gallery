import os
from typing import List, Dict

import psycopg2


class Database():
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT")
        )
    
    def select_all(self) -> List[Dict[str, str]]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM photos;")
        photos = cursor.fetchall()
        cursor.close()

        result = []
        for photo in photos:
            result.append({"name": photo[0], "url": photo[1]})

        return result

    def add(self, name: str, url: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO photos (name, url) VALUES (%s, %s)", (name, url))
        cursor.close()

        
if __name__ == "__main__":
    database = Database()

