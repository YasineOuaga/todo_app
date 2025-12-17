from service.todo_service import add_todo, list_todos

def start():
    while True:
        print("1. Add todo")
        print("2. Show todos")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Enter a todo: ")
            success = add_todo(text)
            if success == False:
                print("Todo cannot be empty")

        elif choice == "2":
            todos = list_todos()
            if len(todos) == 0:
                print("No todos yet")
            else:
                print("Todos:")
                for i in range(len(todos)):
                    print(i + 1, "-", todos[i].strip())

        elif choice == "3":
            break

        else:
            print("Invalid choice")
