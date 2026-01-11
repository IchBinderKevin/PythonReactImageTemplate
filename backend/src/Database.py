import os
import aiosqlite

DEFAULT_DB_PATH = "./db/db.db"

class Database:
    def __init__(self):
        self.db_path = os.getenv("DB_PATH", DEFAULT_DB_PATH)

    async def check_for_db(self):
        does_db_exist = os.path.exists(self.db_path)
        if does_db_exist:
            print("DB exists")
            return
        async with aiosqlite.connect(self.db_path) as db:
            # Could place migrations here (or more like the base db state) or use an orm completely decoupled from this, load sql files, etc.
            # This is after all just a simple template
            await db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
            await db.execute("INSERT INTO users (name, email) VALUES ('John', 'john@test.com')")
            await db.commit()

    async def get_user_data(self):
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT id, name, email FROM users")
            rows = await cursor.fetchall()
            return [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]
