import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    """Add a new task."""
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks, task_id):
    """Remove a task by its ID."""
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task ID.")

def complete_task(tasks, task_id):
    """Mark a task as completed by its ID."""
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_id]['task']}' completed.")
    else:
        print("Invalid task ID.")

def list_tasks(tasks):
    """List all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")
    for idx, task in enumerate(tasks):
        status = "✔" if task['completed'] else "✘"
        print(f"{idx}. [{status}] {task['task']}")
    print()

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to remove: "))
            remove_task(tasks, task_id)
        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as complete: "))
            complete_task(tasks, task_id)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")
