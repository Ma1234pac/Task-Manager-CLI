import json
from pathlib import Path
from typing import List, Dict, Optional


class TaskManager:
    """A simple task manager with JSON persistence."""

    def __init__(self, file_path: str = "data/tasks.json"):
        self.file_path = Path(file_path)
        self.tasks: List[Dict] = []
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from the JSON file."""
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self._save_tasks()
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                self.tasks = json.load(file)

        except (json.JSONDecodeError, OSError):
            self.tasks = []

    def _save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)

    def add_task(self, title: str) -> Dict:
        """Add a new task."""
        title = title.strip()

        if not title:
            raise ValueError("Task title cannot be empty.")

        new_id = max((task["id"] for task in self.tasks), default=0) + 1

        task = {
            "id": new_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self._save_tasks()

        return task

    def get_tasks(self, completed: Optional[bool] = None) -> List[Dict]:
        """
        Return tasks.

        If completed is None:
            return all tasks.

        If completed is True:
            return completed tasks.

        If completed is False:
            return pending tasks.
        """
        if completed is None:
            return self.tasks.copy()

        return [
            task for task in self.tasks
            if task["completed"] == completed
        ]

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                return True

        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self._save_tasks()
                return True

        return False


def display_tasks(tasks: List[Dict]) -> None:
    """Display tasks in a readable format."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nTasks")
    print("-" * 50)

    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")

    print()


def print_menu() -> None:
    """Display the application menu."""
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Show pending tasks")
    print("4. Show completed tasks")
    print("5. Complete task")
    print("6. Delete task")
    print("7. Exit")
    print("========================")


def main() -> None:
    """Run the command-line application."""
    manager = TaskManager()

    while True:
        print_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter task title: ")

            try:
                task = manager.add_task(title)
                print(f"Task added successfully: #{task['id']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            display_tasks(manager.get_tasks())

        elif choice == "3":
            display_tasks(manager.get_tasks(completed=False))

        elif choice == "4":
            display_tasks(manager.get_tasks(completed=True))

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID: "))

                if manager.complete_task(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "6":
            try:
                task_id = int(input("Enter task ID: "))

                if manager.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
