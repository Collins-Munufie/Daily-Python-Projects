import tkinter as tk
from tkinter import messagebox

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Initialize tasks list
tasks = load_tasks()

# Set up window
window = tk.Tk()
window.title("To-Do List GUI")
window.geometry("800x900")

# Entry box
entry = tk.Entry(window, width=50)
entry.pack(pady=40)

# Add and Delete buttons
tk.Button(window, text="Add Task", width=50, command = add_task).pack(pady=20)
tk.Button(window, text="Delete Selected Task", width=50, command = delete_task).pack(pady=20)

# Listbox to display tasks
listbox = tk.Listbox(window, width=80, height=20)
listbox.pack(pady=30)

# Populate listbox with loaded tasks
for task in tasks:
    listbox.insert(tk.END, task)

# Start the GUI loop
window.mainloop()
