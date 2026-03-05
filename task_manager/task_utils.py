def add_task(tasks, title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_complete(tasks, index):

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task markd as complete!")
    else:
        print("Invalid task number.")


def view_pending_tasks(tasks):

    for i in range(len(tasks)):
        if not tasks[i]["completed"]:
            print(
                f"{i + 1}. {tasks[i]['title']} - Due: {tasks[i]['due_date']}")


def view_pending_tasks(tasks):
    for i in range(len(tasks)):
        if not tasks[i]["completed"]:
            print(
                f"{i + 1}. {tasks[i]['title']} - Due: {tasks[i]['due_date']}")


def view_progress(tasks):
    percentage = calculate_progress(tasks)
    print(percentage)


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0

    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100