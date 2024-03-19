# To-Do List Application

tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append(task_name)
    print("Task added successfully.")

def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
