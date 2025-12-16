def save_todo(todo):
    file = open("todos.txt", "a")
    file.write(todo.text + "\n")
    file.close()

def get_all_todos():
    try:
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()
        return todos
    except FileNotFoundError:
        return []
