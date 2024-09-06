def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice. Try again.")

todo_list()
