import os

file_name = "todo_list.txt"

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]  # Always return a list
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_data(tasks, filename):
    with open(filename, 'w') as file:  # Overwrite the file with updated tasks
        file.writelines([task + '\n' for task in tasks])


def add_task(task, tasks):
    tasks.append(task)  # Append to the list
    save_data(tasks, file_name)  # Save the updated list
    print(f"Task Added: {task}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found. Add some first!")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_number, tasks):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)  # Remove the task
        save_data(tasks, file_name)  # Save the updated list
        print(f"Task Deleted: {removed_task}")
    else:
        print("Invalid task number.")

def mark_task_completed(task_number, tasks):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] += " (Completed)"
        save_data(tasks, file_name)  # Save the updated list
        print(f"Task Marked as Completed: {tasks[task_number - 1]}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_data(file_name)  # Load tasks into a list

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            task = input("Enter your task: ")
            add_task(task, tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number, tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_task_completed(task_number, tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
