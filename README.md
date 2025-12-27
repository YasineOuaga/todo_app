## Todo App



Small CLI todo application :

\- git workflow

\- .gitignore

\- virtual environment (.venv)

\- packages/modules (ui, service, data, domain)

\- requirements.txt



## Setup

python -m venv .venv

.\\\\.venv\\\\Scripts\\\\Activate.ps1

pip install -r requirements.txt

## Features
- Add a todo
- Show all todos
- Delete a todo
- Clear all todos (with confirmation)

## Project structure
- `main.py` – entry point of the application
- `ui/` – user interface (CLI, input/output)
- `service/` – business logic
- `data/` – data access (file storage)
- `domain/` – domain objects

## Architecture
The project is structured in layers:
- UI layer depends on the Service layer
- Service layer depends on the Domain and Data layers
- Data layer only handles storage

## How the application works

The application is a simple command-line todo app.

- The user interacts with the app via a text-based menu.
- The UI layer (`ui`) handles user input and output.
- The service layer (`service`) contains the application logic.
- The data layer (`data`) reads and writes todos to a text file.
- Todos are stored in a file called `todos.txt`.

The application starts from `main.py`.






