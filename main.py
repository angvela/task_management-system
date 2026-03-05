
from utails import add_task, mark_task_complete, view_pending_tasks, calculate_progress
from validation import validate_task_input

def main():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. Mark Task As Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input()

        if choice == "1":
            title = input()
            description = input()
            due_date = input()

            try:
                validate_task_input(title, description, due_date)
                add_task(tasks, title, description, due_date)
            except ValueError:
                print("Invalid task input.")

        elif choice == "2":
            try:
                index = int(input()) - 1
                mark_task_complete(tasks, index)
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            progress = calculate_progress(tasks)
            print(progress)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()




