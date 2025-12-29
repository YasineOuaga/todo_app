from settings import DB_PATH
from data.db import init_db
from ui.cli import start

if __name__ == "__main__":
    init_db(DB_PATH)
    start()
