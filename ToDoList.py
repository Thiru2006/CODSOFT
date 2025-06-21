todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks in your to-do list.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
        print()

def add_task():
    task_name = input("Enter the task: ")
    todo_list.append({"task": task_name, "done": False})
    print("Task added successfully.\n")

def mark_done():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def update_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_num < len(todo_list):
            new_task = input("Enter the new task description: ")
            todo_list[task_num]["task"] = new_task
            print("Task updated successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list.pop(task_num)
            print("Task deleted successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def todo_app():
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

todo_app()
