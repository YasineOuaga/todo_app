from service.todo_service import add_todo, list_todos

def start():
    while True:
        print("1. Add todo")
        print("2. Show todos")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Enter a todo: ")
            if text != "":
                add_todo(text)
            else:
                print("Todo cannot be empty")

        elif choice == "2":
            todos = list_todos()
            print("Todos:")
            for i in range(len(todos)):
                print(i + 1, "-", todos[i].strip())

        elif choice == "3":
            break

        else:
            print("Invalid choice")
