# run.py

import sys
# from src.todo_manager import load_list, get_todo_details, TodoNotFoundError
from src.ToDo_Manager import load_list,get_todo_details,TodoNotFoundError

def print_all_todos():
    todos = load_list()
    if not todos:
        print("No todos found.")
        return

    print("All todos:")
    for todo in todos:
        print("-" * 40)
        print(f"ID         : {todo.get('id')}")
        print(f"Title      : {todo.get('title')}")
        print(f"Description: {todo.get('description')}")
        print(f"Done Status: {todo.get('doneStatus')}")
    print("-" * 40)


def print_todo_by_id(todo_id: str):
    try:
        todo = get_todo_details(todo_id)
        print("Todo details:")
        print("-" * 40)
        print(f"ID         : {todo.get('id')}")
        print(f"Title      : {todo.get('title')}")
        print(f"Description: {todo.get('description')}")
        print(f"Done Status: {todo.get('doneStatus')}")
        print("-" * 40)
    except TodoNotFoundError as e:
        # In a real API this would be a 404 response; here we just print the message.
        print(str(e))


def main():
    """
    Usage:
      python run.py              -> lists all todos
      python run.py <todo_id>    -> shows details for that todo
    """
    if len(sys.argv) == 1:
        # No arguments: list all todos
        print_all_todos()
    else:
        # First argument is treated as todo_id
        todo_id = sys.argv[1]
        print_todo_by_id(todo_id)


if __name__ == "__main__":
    main()