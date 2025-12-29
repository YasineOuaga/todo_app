from domain.todo import Todo
from data.todo_repository import save_todo, get_all_todos, delete_todo, clear_all, toggle_done

def add_todo(text):
    if text == "":
        return False

    todo = Todo(text)
    save_todo(todo)
    return True

def list_todos():
    return get_all_todos()

def remove_todo(number):
    return delete_todo(number)

def toggle_todo(number):
    return toggle_done(number)



def clear_todos():
    clear_all()
