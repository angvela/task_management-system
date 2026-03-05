from datetime import datetime

def validate_task_input(title, description, due_date):
    """
    Validates task inputs are not empty
    """
    if not title or not description:
        raise ValueError("Invalid task input.")
    if len(title) > 50:
        raise ValueError("Invalid task input.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid task input.")
    # Optional: Add check for description length if needed
    # if len(description) > 100:
    #     raise ValueError("Invalid task input.")

    return True