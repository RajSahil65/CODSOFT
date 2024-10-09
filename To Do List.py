# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, new_task):
        if task_id < len(self.tasks):
            self.tasks[task_id] = new_task
        else:
            print("Task not found")

    def delete_task(self, task_id):
        if task_id < len(self.tasks):
            del self.tasks[task_id]
        else:
            print("Task not found")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Display tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the task ID to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_id-1, new_task)
        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id-1)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()