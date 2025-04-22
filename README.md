# 📋 Task Manager (CLI-based)

A simple command-line task management application written in Python. This project allows users to create, view, and update programming tasks while tracking the workload assigned to each programmer.

## 🧠 Features

- Add new tasks with a description, programmer, and workload (in hours).
- Mark tasks as finished.
- List all tasks, only finished, or only unfinished tasks.
- Filter tasks by programmer.
- View task statistics and workload summary per programmer.

## 📁 Project Structure

```text
.
├── classes.py              # Contains the Task and OrderBook classes
├── main.py                 # Main entry point of the application
└── classes.cpython-312.pyc # Compiled Python file (can be ignored)
```

## ▶️ How to Run

1. Make sure you have Python 3.12 installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## 🛠️ Available Commands

Here are some sample commands that the user can input:

- `add Write unit tests Alice 5` → adds a task.
- `list all` → lists all tasks.
- `list finished` / `list unfinished` → filters tasks.
- `mark 1` → marks task with ID 1 as finished.
- `status Alice` → shows task and workload stats for Alice.
- `0` → exits the program.

## 👨‍💻 Example Usage

```text
command: add Write unit tests Alice 5
command: add Fix login bug Bob 3
command: list all
command: mark 1
command: status Alice
```

## 🚀 Future Improvements

- Graphical User Interface (GUI).
- Saving/loading tasks from a JSON or database.
- Task deletion functionality.


## 🖊️ Author
Marie-Caroline Bertheau 
