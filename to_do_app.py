tasks = []

def add_task(title, description):
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['title']} ({status}) - {task['description']}")

def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def edit_task(index, new_title, new_description):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        tasks[index]["description"] = new_description
        print("Task edited successfully!")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nCommand Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter task index to mark as completed: ")) - 1
        mark_completed(index)
    elif choice == "4":
        index = int(input("Enter task index to edit: ")) - 1
        new_title = input("Enter new task title: ")
        new_description = input("Enter new task description: ")
        edit_task(index, new_title, new_description)
    elif choice == "5":
        index = int(input("Enter task index to delete: ")) - 1
        delete_task(index)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
