# calculator_combo.py

def run_cli_calculator():
    # CLI calculator code here
    def add(x, y):
     return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (1/2/3/4 or +, -, *, /): ")

        if choice in ('1', '2', '3', '4', '+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice in ('1', '+'):
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice in ('2', '-'):
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice in ('3', '*'):
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice in ('4', '/'):
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            next_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calc != 'yes':
                print("Thank you for using the calculator!")
                break
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()


def run_gui_calculator():
    # GUI calculator code here
    import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Create main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Labels and entries
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Operation selector
tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the app
root.mainloop()


# User chooses which mode to run
if __name__ == "__main__":
    mode = input("Choose mode: (1) CLI or (2) GUI: ")
    if mode == "1":
        run_cli_calculator()
    elif mode == "2":
        run_gui_calculator()
    else:
        print("Invalid choice.")
