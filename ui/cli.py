from service.todo_service import add_todo, list_todos, remove_todo, clear_todos, toggle_todo

def start():
    while True:
        print("=================================")
        print("          TODO APP (CLI)         ")
        print("=================================")
        print("1) Add todo")
        print("2) Show todos")
        print("3) Delete todo")
        

        print("4) Clear all todos")
        print("5) Toggle done/undone")
        print("6) Exit")
        print("---------------------------------")

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            text = input("Enter a todo: ").strip()
            success = add_todo(text)
            if success == False:
                print("Todo cannot be empty")

        elif choice == "2":
            print("---------------------------------")

            todos = list_todos()
            if len(todos) == 0:
                print("No todos yet")
            else:
                print("Todos:")
                for row in todos:
                    todo_id = row[0]
                    text = row[1]
                    done = row[2]
                    mark = "[x]" if done == 1 else "[ ]"
                    print(todo_id, "-", mark, text)
                print("Total todos:", len(todos))



        elif choice == "3":
            number = input("Todo number to delete: ").strip()
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
            number = input("Todo number to toggle: ").strip()
            if number.isdigit():
                success = toggle_todo(int(number))
                if success == False:
                    print("Invalid number")
            else:
                print("Please enter a number")

        elif choice == "6":
            print("Bye!")
            break

        else:
            print("Invalid choice")

        print()
