import os
def display_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!")
    else:
        for idx, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx + 1}. {task['task']} - {status}")
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            print(f"Task '{tasks.pop(task_num - 1)['task']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
def save_tasks_to_file(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            f.write(f"{task['task']} | {status}\n")
def load_tasks_from_file(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    
    tasks = []
    with open(filename, "r") as f:
        for line in f:
            task, status = line.strip().split(" | ")
            tasks.append({"task": task, "completed": status == "Completed"})
    
    return tasks
def main():
    tasks = load_tasks_from_file()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks_to_file(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
if __name__ == "__main__":
    main()