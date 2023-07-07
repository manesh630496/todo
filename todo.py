class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            task = self.tasks[task_index]
            task['completed'] = True
            print("Task completed!")

    def delete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            del self.tasks[task_index]
            print("Task deleted!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "✓" if task['completed'] else " "
                print(f"{index + 1}. [{status}] {task['description']}")

    def start(self):
        print("Welcome to the Todo App!")
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Complete Task")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                description = input("Enter task description: ")
                task = {'description': description, 'completed': False}
                self.add_task(task)
            elif choice == "2":
                task_index = int(input("Enter task index to mark as complete: ")) - 1
                self.complete_task(task_index)
            elif choice == "3":
                task_index = int(input("Enter task index to delete: ")) - 1
                self.delete_task(task_index)
            elif choice == "4":
                self.view_tasks()
            elif choice == "5":
                print("Thank you for using the Todo App!")
                break
            else:
                print("Invalid choice. Please try again.")


# Create and start the TodoApp
app = TodoApp()
app.start()

