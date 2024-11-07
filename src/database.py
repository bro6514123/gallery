import sqlite3

import aiosqlite


class database():
    @staticmethod
    def create_DB_and_table():
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `photos` (name TEXT, url TEXT)")
        cursor.close()
        connection.commit()
        connection.close()

    @staticmethod
    async def select_all():
        result = []
        try:
            db = await aiosqlite.connect("database.db")
            result = await db.execute_fetchall("SELECT * FROM `photos`")
        except Exception as error:
            print(error)
        finally:
            await db.close()
            return result
        
    @staticmethod
    async def select_all_names():
        result = []
        try:
            db = await aiosqlite.connect("database.db")
            result = await db.execute_fetchall("SELECT `name` FROM `photos`")
        except Exception as error:
            print(error)
        finally:
            await db.close()
            return result

    @staticmethod
    async def insert(name, url):
        try:
            db = await aiosqlite.connect("database.db")
            await db.execute("INSERT INTO `photos` VALUES (?, ?)", (name, url))
            await db.commit()
        except Exception as error:
            print(error)
        finally:
            await db.close()
