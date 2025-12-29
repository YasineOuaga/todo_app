import csv
from service.todo_service import list_todos

def export_to_csv(filename="todos.csv"):
    todos = list_todos()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "text", "done"])

        for row in todos:
            writer.writerow(row)
