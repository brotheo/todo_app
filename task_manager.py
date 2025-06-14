# TaskManager class handles task-related operations such as add, view, mark done, and delete
class TaskManager:
    def __init__(self, tasks=None):
        # Initialize with existing tasks or an empty list
        self.tasks = tasks if tasks else []

    def add_task(self, description):
        # Add a new task with description and set 'done' status to False
        self.tasks.append({"desc": description, "done": False})
        print("Task added.")

    def view_tasks(self):
        # Display all tasks with their status
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks, 1):
            # Show ✅ if task is done, ❌ if not
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['desc']} [{status}]")

    def mark_done(self, index):
        # Mark a task as completed by its index
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        # Delete a task by its index
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted: {removed['desc']}")
        else:
            print("Invalid task number.")


