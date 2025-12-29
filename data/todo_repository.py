import sqlite3
from settings import DB_PATH


def save_todo(todo):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO todos(text, done) VALUES(?, ?)", (todo.text, 0))

    connection.commit()
    connection.close()


def get_all_todos():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, text, done FROM todos ORDER BY id")
    rows = cursor.fetchall()

    connection.close()
    return rows


def delete_todo(todo_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    connection.commit()

    deleted = cursor.rowcount > 0
    connection.close()
    return deleted


def toggle_done(todo_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT done FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()

    if row is None:
        connection.close()
        return False

    current_done = row[0]
    new_done = 0 if current_done == 1 else 1

    cursor.execute("UPDATE todos SET done = ? WHERE id = ?", (new_done, todo_id))
    connection.commit()
    connection.close()
    return True


def clear_all():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM todos")
    connection.commit()
    connection.close()
