import sqlite3

def init_db(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
    """)

    connection.commit()
    connection.close()
