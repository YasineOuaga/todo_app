def save_todo(todo):
    file = open("todos.txt", "a")
    file.write(todo.text )
    file.close()

def get_all_todos():
    try:
        file = open("todos.txt", "r")
        todos = file.readlines()
        return todos
    except FileNotFoundError:
        return []
