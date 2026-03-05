import pytest
from task_manager.task_utils import calculate_progress
from task_manager.validation import validate_task_input

def test_calculate_progress():
    tasks = [
        {'title': 'Task 1', 'description': 'testing', 'due_date': '2024_05_26', 'completed': True},
        {'title': 'Task 2', 'description': 'testing', 'due_date': '2024_05_26', 'completed': False}
    ]
    assert calculate_progress(tasks) == 50.0

def test_validate_task_input_valid():
    # Should not raise
    validate_task_input("Valid Title", "Valid Description", "2024-05-24")

def test_validate_task_input_empty_title():
    with pytest.raises(ValueError):
        validate_task_input("", "Description", "2024-05-24")

def test_validate_task_input_long_title():
    with pytest.raises(ValueError):
        validate_task_input("A" * 51, "Description", "2024-05-24")

def test_validate_task_input_empty_description():
    with pytest.raises(ValueError):
        validate_task_input("Title", "", "2024-05-24")

def test_validate_task_input_invalid_date():
    with pytest.raises(ValueError):
        validate_task_input("Title", "Description", "invalid-date")