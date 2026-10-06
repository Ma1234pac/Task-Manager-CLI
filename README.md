# 📝 Python Task Manager

A simple command-line task manager built with Python.

The application allows users to create, manage, complete, and delete tasks. Tasks are stored locally in a JSON file, so they remain available after restarting the application.

## ✨ Features

* Add new tasks
* Display all tasks
* Display pending tasks
* Display completed tasks
* Mark tasks as completed
* Delete tasks
* Persistent JSON storage
* Input validation
* Automated tests with pytest

## 🛠️ Technologies

* Python 3
* JSON
* pathlib
* pytest

## 📁 Project Structure

```text
python-task-manager/
│
├── src/
│   ├── __init__.py
│   └── task_manager.py
│
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
│
├── data/
│   └── tasks.json
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-task-manager.git
```

Move into the project directory:

```bash
cd python-task-manager
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

From the project root directory, run:

```bash
python src/task_manager.py
```

You should see:

```text
===== TASK MANAGER =====
1. Add task
2. Show all tasks
3. Show pending tasks
4. Show completed tasks
5. Complete task
6. Delete task
7. Exit
========================
Choose an option:
```

## 🧪 Running the Tests

Run:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

Example:

```text
============================= test session starts =============================

tests/test_task_manager.py .........

============================== 9 passed ======================================
```

## 💡 Example

Adding a task:

```text
Choose an option: 1
Enter task title: Learn Python
Task added successfully: #1
```

Displaying tasks:

```text
Tasks
--------------------------------------------------
[ ] 1. Learn Python
[ ] 2. Learn Git
[✓] 3. Complete project
```

## 🧠 What I Learned

This project demonstrates several fundamental Python concepts:

* Object-Oriented Programming
* Classes and methods
* Lists and dictionaries
* File handling
* JSON serialization
* Exception handling
* Type hints
* Command-line interfaces
* Unit testing
* Project organization

## 🔮 Future Improvements

Possible future features include:

* Task priorities
* Due dates
* Categories
* Search functionality
* Task editing
* SQLite database support
* A graphical user interface
* REST API integration

## 📄 License

This project is available under the MIT License.
