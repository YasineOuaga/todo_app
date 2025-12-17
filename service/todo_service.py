from domain.todo import Todo
from data.todo_repository import save_todo, get_all_todos, delete_todo

def add_todo(text):
    if text == "":
        return False

    todo = Todo(text)
    save_todo(todo)
    return True

def list_todos():
    return get_all_todos()

def remove_todo(number):
    return delete_todo(number - 1)
