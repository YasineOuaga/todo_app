from service.todo_service import add_todo, list_todos

def start():
    while True:
        print("1. Add todo")
        print("2. Show todos")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Enter a todo: ")
            add_todo(text)
        elif choice == "2":
            todos = list_todos()
            print("Todos:")
            for t in todos:
                print(t.strip())
        elif choice == "3":
            break
        else:
            print("Invalid choice")
