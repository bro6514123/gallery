import psycopg2


class Database():
    def __init__(self):
        try:
            conn = psycopg2.connect(
                dbname="database",
                user="postgres",
                password="password",
                host="localhost",
                post="5432"
            )
            print("ok")
        except Exception as error:
            print(error)
        
if __name__ == "__main__":
    database = Database()

