 # todo_gui.py
"""
This module implements a simple to-do list application using Tkinter.
"""
import tkinter as tk

class TodoApp:
    """
    REpresents a simple to-do list application.
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
        for task in self.tasks:
        self.task_listbox.insert(tk.END, task[0])
        self.remove_button = tk.Button(
            master,
            text="Remove Task",
            command=self.remove_task
         )
        self.remove_button.pack()
        self.complete_button = tk.Button(
            master,
            text="Mark as Complete",
            command=self.mark_as_complete
         )
        self.complete_button.pack()
        self.quit_button = tk.Button(
            master,
            text="Quit",
            command=self.quit_and_save
         )
        self.quit_button.pack()
    def add_task(self):
        """
        Add a task to the task list.
        """
        task = self.task_entry.get()
        if task:
            self.tasks.append([task, False])
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            pass
    def mark_as_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            task[1] = True
            self.task_listbox.itemconfig(index, {'bg': 'light grey'})
        except IndexError:
            pass
    def quit_and_save(self):
        with open("tasks.txt", "w") as file:
            for task, completed in self.tasks:
                file.write(f"{task},{completed}\n")
        self.master.quit()
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task, completed = line.strip().split(",")
                    self.tasks.append([task, completed == "True"])
        except FileNotFoundError:
            pass
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
