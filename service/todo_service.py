from domain.todo import Todo
from data.todo_repository import save_todo, get_all_todos

def add_todo(text):
    todo = Todo(text)
    save_todo(todo)

def list_todos():
    return get_all_todos()
