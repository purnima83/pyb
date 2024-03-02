"""
This module implements a simple to-do list application using Tkinter.
"""
import tkinter as tk
import json

class TodoApp:
    """
    Represents a simple to-do list application.
    This class provides functionality to manage tasks in a to-do list using Tkinter.
    """
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        self.tasks = []
        self.load_tasks()
        self.task_entry = tk.Entry(master)
        self.task_entry.pack()
        self.add_button = tk.Button(
            master,
            text="Add Task",
            command=self.add_task
        )
        self.add_button.pack()
        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack()
        self.complete_button = tk.Button(
            master,
            text="Mark as Complete",
            command=self.mark_as_complete
        )
        self.complete_button.pack()
        self.remove_button = tk.Button(
            master,
            text="Remove Task",
            command=self.remove_task
        )
        self.remove_button.pack()

    def add_task(self):
        """
        Add a task to the task list.
        """
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.display_tasks()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        """
        Remove a task from the task list.
        """
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.display_tasks()

    def mark_as_complete(self):
        """
        Mark a task as complete.
        """
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.display_tasks()

    def load_tasks(self):
        """
        Load tasks from a file.
        """
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """
        Save tasks to a file.
        """
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(self.tasks, file)

    def display_tasks(self):
        """
        Display tasks in the listbox.
        """
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = f"{task['task']} {'(Completed)' if task['completed'] else ''}"
            self.task_listbox.insert(tk.END, task_text)
    # Other methods with docstrings
def main():
    """
    Main function called.
    """
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
