# example_02_calculator_functions.py
# Lesson 31: A menu-driven calculator using functions

def add(a, b):
    """Return a + b."""
    return a + b

def subtract(a, b):
    """Return a - b."""
    return a - b

def multiply(a, b):
    """Return a * b."""
    return a * b

def divide(a, b):
    """Return a / b, or an error message if b is zero."""
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def print_menu():
    """Print the calculator menu."""
    print("=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("==================")

# Show the menu
print_menu()

# Get user input
choice = int(input("Choose operation (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Call the right function based on choice
if choice == 1:
    result = add(a, b)
    print(a, "+", b, "=", result)
elif choice == 2:
    result = subtract(a, b)
    print(a, "-", b, "=", result)
elif choice == 3:
    result = multiply(a, b)
    print(a, "*", b, "=", result)
elif choice == 4:
    result = divide(a, b)
    print(a, "/", b, "=", result)
else:
    print("Invalid choice!")
