import tkinter as tk
import json

class AuthenticationWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        master.title("Login")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Authenticate user (dummy authentication for demonstration)
        if username == "user" and password == "password":
            self.app.show()
            self.master.destroy()
        else:
            tk.messagebox.showerror("Login Failed", "Invalid username or password.")

class TodoApp:
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
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.display_tasks()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.display_tasks()

    def mark_as_complete(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.display_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(self.tasks, file)

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = f"{task['task']} {'(Completed)' if task['completed'] else ''}"
            self.task_listbox.insert(tk.END, task_text)

    def show(self):
        self.master.deiconify()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.withdraw()  # Hide the main window initially
    auth_window = tk.Toplevel(root)
    AuthenticationWindow(auth_window, app)
    root.mainloop()

if __name__ == "__main__":
    main()
