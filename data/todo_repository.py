def save_todo(todo):
    with open("todos.txt", "a") as file:
        file.write(todo.text + "\n")

def get_all_todos():
    try:
        with open("todos.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def delete_todo(index):
    todos = get_all_todos()
    if index < 0 or index >= len(todos):
        return False

    del todos[index]

    with open("todos.txt", "w") as file:
        for t in todos:
            file.write(t)

    return True
