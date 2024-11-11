import psycopg2


class Database():
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="database",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
    
    def select_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM names;")
        result = cursor.fetchall()
        cursor.close()
        return result
        
if __name__ == "__main__":
    database = Database()

