#Day-7 Challenge

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:\n")
        for i, task in enumerate(tasks, 1):
            print(f"Task No : {i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Deleted: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n-----To-Do List CLI-----\n")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit\n")
        
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
