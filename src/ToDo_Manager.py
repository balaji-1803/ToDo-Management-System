import json
import logging
import os
from typing import List, Dict, Any

# File path
TODO_FILE_PATH = os.path.join("data", "todos.json")


class TodoNotFoundError(Exception):
    """Exception representing a 404 Not Found error for a todo."""

    def __init__(self, todo_id: str):
        super().__init__(f"Todo with id '{todo_id}' not found.")
        self.status_code = 404


def load_list() -> List[Dict[str, Any]]:
    """
    Load the list of todos from a JSON file.

    - Uses a hardcoded file path: data/todos.json
    - If the file is missing, returns an empty list and logs a warning
    - If there is an error reading or parsing the JSON, logs the error
      and returns an empty list
    """
    if not os.path.exists(TODO_FILE_PATH):
        logging.warning(
            "Todo file not found at '%s'. Returning empty list.",
            TODO_FILE_PATH
        )
        return []

    try:
        with open(TODO_FILE_PATH, "r", encoding="utf-8") as file:
            todos = json.load(file)

        if not isinstance(todos, list):
            logging.error("Invalid JSON format: expected a list.")
            return []

        return todos

    except json.JSONDecodeError as e:
        logging.error("JSON parsing error: %s", e)
        return []
    except OSError as e:
        logging.error("File read error: %s", e)
        return []


def get_todo_details(todo_id: str) -> Dict[str, Any]:
    """
    Retrieve details for a specific todo based on its unique identifier.

    - Loads all todos using load_list()
    - Searches for a todo matching the given todo_id
    - Returns the todo if found
    - Raises TodoNotFoundError (404) if not found
    """
    todos = load_list()

    for todo in todos:
        if todo.get("id") == todo_id:
            return todo

    raise TodoNotFoundError(todo_id)
