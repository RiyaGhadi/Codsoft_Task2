import tkinter as tk
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero", font=("Arial", 20))
                return
            result = num1 / num2
        result_label.config(text="Result: " + str(result),font=("Arial", 20))
    except ValueError:
        result_label.config(text="Invalid input",font=("Arial", 20))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
# Title label
title_label = tk.Label(window, text="Simple Calculator", font=("Arial", 40, "bold","underline"),justify="center",background="blue",foreground="white")
title_label.pack(fill="both")

# Labels for entry fields
num1_label = tk.Label(window, text="Enter the first number:",font=("Arial", 16))
num1_label.pack()

entry1 = tk.Entry(window,font=("Arial", 14))
entry1.pack()

num2_label = tk.Label(window, text="Enter the second number:",font=("Arial", 16))
num2_label.pack()

entry2 = tk.Entry(window,font=("Arial", 14))
entry2.pack()

# Buttons for operations
add_button = tk.Button(window, text="+", command=lambda: calculate("+"),width=3,height=1,font=3)
add_button.pack()

subtract_button = tk.Button(window, text="-", command=lambda: calculate("-"),width=3,height=1,font=3)
subtract_button.pack()

multiply_button = tk.Button(window, text="*", command=lambda: calculate("*"),width=3,height=1,font=3)
multiply_button.pack()

divide_button = tk.Button(window, text="/", command=lambda: calculate("/"),width=3,height=1,font=3)
divide_button.pack()

# Label to display the result
result_label = tk.Label(window)
result_label.pack()

# Start the main event loop
window.mainloop()
