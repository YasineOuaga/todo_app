def save_todo(todo):
    with open("todos.txt", "a") as file:
        file.write(todo.text + "\n")

def get_all_todos():
    try:
        with open("todos.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
