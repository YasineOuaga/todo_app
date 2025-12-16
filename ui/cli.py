from service.todo_service import add_todo, list_todos

def start():
    text = input("Enter a todo: ")
    add_todo(text)

    todos = list_todos()
    print("Todos:")
    for t in todos:
        print(t)
