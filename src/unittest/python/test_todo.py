# test_todo.py

import unittest
import tkinter as tk
from unittest.mock import patch
from todo_gui import TodoApp

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = TodoApp(self.root)

    def test_add_task(self):
        with patch.object(self.app, 'task_entry', return_value=tk.Entry()):
            self.app.task_entry.insert(0, "Task 1")
            self.app.add_task()
            self.assertEqual(self.app.tasks[-1][0], "Task 1")

    def test_remove_task(self):
        self.app.tasks.append(["Task 1", False])
        self.app.tasks.append(["Task 2", False])
        self.app.task_listbox.insert(tk.END, "Task 1")
        self.app.task_listbox.insert(tk.END, "Task 2")
        self.app.task_listbox.select_set(0)
        self.app.remove_task()
        self.assertEqual(self.app.tasks, [["Task 2", False]])

    def test_mark_as_complete(self):
        self.app.tasks.append(["Task 1", False])
        self.app.tasks.append(["Task 2", False])
        self.app.task_listbox.insert(tk.END, "Task 1")
        self.app.task_listbox.insert(tk.END, "Task 2")
        self.app.task_listbox.select_set(0)
        self.app.mark_as_complete()
        self.assertEqual(self.app.tasks[0][1], True)
        self.assertEqual(self.app.task_listbox.itemcget(0, 'bg'), 'light grey')

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
