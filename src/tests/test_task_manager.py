import json

import pytest

from src.task_manager import TaskManager


def test_add_task(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    task = manager.add_task("Learn Python")

    assert task["id"] == 1
    assert task["title"] == "Learn Python"
    assert task["completed"] is False


def test_add_multiple_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    manager.add_task("Task 1")
    manager.add_task("Task 2")

    tasks = manager.get_tasks()

    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2


def test_complete_task(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    task = manager.add_task("Learn Git")

    result = manager.complete_task(task["id"])

    assert result is True
    assert manager.get_tasks()[0]["completed"] is True


def test_complete_nonexistent_task(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    result = manager.complete_task(999)

    assert result is False


def test_delete_task(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    task = manager.add_task("Delete me")

    result = manager.delete_task(task["id"])

    assert result is True
    assert len(manager.get_tasks()) == 0


def test_filter_pending_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    task1 = manager.add_task("Pending task")
    task2 = manager.add_task("Completed task")

    manager.complete_task(task2["id"])

    pending = manager.get_tasks(completed=False)

    assert len(pending) == 1
    assert pending[0]["id"] == task1["id"]


def test_filter_completed_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")

    manager.complete_task(task2["id"])

    completed = manager.get_tasks(completed=True)

    assert len(completed) == 1
    assert completed[0]["id"] == task2["id"]


def test_empty_task_title(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(str(file_path))

    with pytest.raises(ValueError):
        manager.add_task("")


def test_tasks_are_persistent(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager1 = TaskManager(str(file_path))
    manager1.add_task("Persistent task")

    manager2 = TaskManager(str(file_path))

    tasks = manager2.get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Persistent task"
