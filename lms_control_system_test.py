from datetime import datetime
import pprint as p
import random
import string
from tabulate import tabulate
import unittest
from unittest.mock import patch

class LMS:
    def __init__(self):
        """Initializes the LMS database with Todo and Complete lists."""
        self.lmsDatabase = {
            'Todo': [],
            'Complete': []
        }

class control_system:
    def __init__(self, database):
        """Initializes the control system with the given database."""
        self.database = database

    def generate_id(self, length=6):
        """Generates a unique ID for tasks."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def add_todo(self, todo):
        """Adds a new task to the Todo list."""
        data = {
            "ID": self.generate_id(),
            "Todo": todo,
            "Date Added": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.database.lmsDatabase['Todo'].append(data)

    def complete(self, task):
        """Marks a task as completed by moving it to the Complete list."""
        for todo in self.database.lmsDatabase['Todo']:
            if todo["Todo"].lower() == task.lower():
                todo['Completed At'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.database.lmsDatabase['Complete'].append(todo)
                self.database.lmsDatabase['Todo'].remove(todo)
                return
        print(f"Task '{task}' not found in the 'Todo' list.")

    def remove_todo(self, task):
        """Removes a task from the Todo list."""
        for todo in self.database.lmsDatabase['Todo']:
            if todo["Todo"].lower() == task.lower():
                self.database.lmsDatabase['Todo'].remove(todo)
                print(f"Task '{task}' has been removed from the 'Todo' list.")
                return
        print(f"Task '{task}' not found in the 'Todo' list.")

    def remove_completed_item(self, task):
        """Removes a task from the Completed list."""
        for complete in self.database.lmsDatabase['Complete']:
            if complete["Todo"].lower() == task.lower():
                self.database.lmsDatabase['Complete'].remove(complete)
                print(f"Task '{task}' has been removed from the 'Complete' list.")
                return
        print(f"Task '{task}' not found in the 'Complete' list.")

    def display_tasks(self):
        """Displays all tasks in Todo and Complete lists."""
        todo_table = [[task['ID'], task['Todo'], task['Date Added']] for task in self.database.lmsDatabase['Todo']]
        complete_table = [[task['ID'], task['Todo'], task['Date Added'], task['Completed At']] for task in self.database.lmsDatabase['Complete']]

        if todo_table:
            print("\nTodo Tasks:")
            print(tabulate(todo_table, headers=["ID", "Task", "Date Added"], tablefmt="fancy_grid"))
        else:
            print("\nNo tasks in the Todo list.")

        if complete_table:
            print("\nCompleted Tasks:")
            print(tabulate(complete_table, headers=["ID", "Task", "Date Added", "Completed At"], tablefmt="fancy_grid"))
        else:
            print("\nNo tasks in the Complete list.")

class TestControlSystemBoundaryValues(unittest.TestCase):

    def setUp(self):
        """Sets up a fresh instance of the LMS database and control system for each test."""
        self.db = LMS()
        self.lms = control_system(self.db)

    def test_add_todo_minimum_boundary(self):
        """Tests adding a task with a single character."""
        self.lms.add_todo('A')
        self.assertEqual(len(self.db.lmsDatabase['Todo']), 1)
        self.assertEqual(self.db.lmsDatabase['Todo'][0]['Todo'], 'A')

    def test_add_empty_todo(self):
        """Tests adding an empty task."""
        self.lms.add_todo('')
        self.assertEqual(len(self.db.lmsDatabase['Todo']), 1)
        self.assertEqual(self.db.lmsDatabase['Todo'][0]['Todo'], '')

    def test_add_todo_maximum_boundary(self):
        """Tests adding a task with a very long string (1000 characters)."""
        long_task = 'A' * 1000
        self.lms.add_todo(long_task)
        self.assertEqual(len(self.db.lmsDatabase['Todo']), 1)
        self.assertEqual(self.db.lmsDatabase['Todo'][0]['Todo'], long_task)

    def test_complete_case_insensitive(self):
        """Tests completing a task with different casing."""
        self.lms.add_todo('Finish biology project')
        self.lms.complete('FINISH BIOLOGY PROJECT')
        self.assertEqual(len(self.db.lmsDatabase['Todo']), 0)
        self.assertEqual(len(self.db.lmsDatabase['Complete']), 1)
        self.assertEqual(self.db.lmsDatabase['Complete'][0]['Todo'], 'Finish biology project')

    def test_remove_non_existent_todo(self):
        """Tests removing a task that doesn't exist."""
        with patch('builtins.print') as mocked_print:
            self.lms.remove_todo('Non-existent task')
            mocked_print.assert_called_with("Task 'Non-existent task' not found in the 'Todo' list.")

    def test_remove_existing_todo(self):
        """Tests removing an existing task."""
        self.lms.add_todo('Study for math test')
        self.lms.remove_todo('Study for math test')
        self.assertEqual(len(self.db.lmsDatabase['Todo']), 0)

    def test_display_empty_tasks(self):
        """Tests displaying tasks when no tasks exist (empty boundary)."""
        with patch('builtins.print') as mocked_print:
            self.lms.display_tasks()
            mocked_print.assert_any_call("\nNo tasks in the Todo list.")
            mocked_print.assert_any_call("\nNo tasks in the Complete list.")

    def test_display_non_empty_tasks(self):
        """Tests displaying tasks when tasks exist (non-empty boundary)."""
        self.lms.add_todo('Finish biology project')
        self.lms.complete('Finish biology project')
        with patch('builtins.print') as mocked_print:
            self.lms.display_tasks()
            mocked_print.assert_any_call("\nTodo Tasks:")
            mocked_print.assert_any_call("\nCompleted Tasks:")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
