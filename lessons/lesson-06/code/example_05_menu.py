# example_05_menu.py
# Lesson 6: A simple menu using elif
# The user picks an operation, then we calculate.

print("=== Calculator Menu ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose an option (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    # Nested if to handle division by zero
    if b == 0:
        print("Error: cannot divide by zero!")
    else:
        print("Result:", a / b)
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
