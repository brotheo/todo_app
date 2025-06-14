from task_manager import TaskManager
from storage import load_tasks, save_tasks

# Function to display the main menu options
def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

# Main function to control app flow
def main():
    tasks = load_tasks()  # Load existing tasks from file
    manager = TaskManager(tasks)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            manager.view_tasks()

        elif choice == "2":
            desc = input("Enter task description: ")
            manager.add_task(desc)

        elif choice == "3":
            try:
                index = int(input("Enter task number to mark done: ")) - 1
                manager.mark_done(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            try:
                index = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            save_tasks(manager.tasks)  # Save before exiting
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run only if this script is executed directly
if __name__ == "__main__":
    main()

