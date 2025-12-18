from service.todo_service import add_todo, list_todos, remove_todo, clear_todos

def start():
    while True:
        print("=================================")
        print("          TODO APP (CLI)         ")
        print("=================================")
        print("1) Add todo")
        print("2) Show todos")
        print("3) Delete todo")
        print("4) Clear all todos")
        print("5) Exit")
        print("---------------------------------")

        choice = input("Choose (1-5): ").strip()

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
            number = input("Todo number to delete: ")
            if number.isdigit():
                success = remove_todo(int(number))
                if success == True:
                    print("Todo deleted")
                else:
                    print("Invalid number")
            else:
                print("Please enter a number")

        elif choice == "4":
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == "y":
                clear_todos()
                print("All todos cleared")
            else:
                print("Cancelled")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice")

        print()
