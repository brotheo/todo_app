# To-Do List Application

A simple command-line To-Do List application in Python to help you manage daily tasks efficiently.  
This project demonstrates modular programming by separating task management and data storage into different modules.

---

## Features

- Add new tasks  
- View all tasks with completion status  
- Mark tasks as completed  
- Delete tasks  
- Save and load tasks from a JSON file to keep your tasks persistent between sessions  

---

## Requirements

- Python 3.x  
- No external libraries needed (uses built-in `json` and `os` modules)  

---

## Project Structure





-----------------------------------------------------------------------------------------------------------------------------------------



![Screenshot 2025-06-14 070745](https://github.com/user-attachments/assets/933ad92b-e477-47a4-865f-fa894a848990)



---

## How to Run

1. Clone or download this repository.  
2. Open a terminal/command prompt in the project folder.  
3. Run the main script:

```bash
python main.py
--- To-Do List ---
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit
Choose an option: 2
Enter task description: Buy groceries
Task added.

Choose an option: 1
1. Buy groceries [❌]

Choose an option: 3
Enter task number to mark done: 1
Task marked as done.

Choose an option: 1
1. Buy groceries [✅]
