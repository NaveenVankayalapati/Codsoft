import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0)

add_button = tk.Button(frame, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=1)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
clear_button.pack()

save_button = tk.Button(root, text="Save Tasks", width=20, command=save_tasks)
save_button.pack()

load_button = tk.Button(root, text="Load Tasks", width=20, command=load_tasks)
load_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

load_tasks()

root.mainloop()
