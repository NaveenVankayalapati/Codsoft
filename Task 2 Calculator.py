import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
        else:
            result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid operation.")
        return
    
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x400")

# Create and configure frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Create labels
label_num1 = tk.Label(frame, text="Enter Number 1:")
label_num1.grid(row=0, column=0)

label_num2 = tk.Label(frame, text="Enter Number 2:")
label_num2.grid(row=1, column=0)

# Create and configure entry widgets
entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1)

# Create operation choice dropdown
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_dropdown = tk.OptionMenu(frame, operation_var, *operation_choices)
operation_var.set("+")  # Default operation
operation_dropdown.grid(row=2, column=0, columnspan=2)

# Create and configure calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create and configure result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
