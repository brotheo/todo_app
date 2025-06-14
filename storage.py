
import json
import os

# Path to the file for saving tasks
FILE_NAME = "tasks.json"

# Load tasks from a JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error loading tasks. Starting with empty list.")
    return []

# Save tasks to a JSON file
def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=2)
    except IOError:
        print("Failed to save tasks.")
