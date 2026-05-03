# example_04_input_validation.py
# Lesson 9: Input validation loop
# Keep asking until the user gives a valid answer.

# Validate age input
print("--- Age validation ---")
age = int(input("Enter your age (0-120): "))
while age < 0 or age > 120:
    print("Invalid! Age must be between 0 and 120.")
    age = int(input("Enter your age (0-120): "))
print("Valid age entered:", age)

# Validate a menu choice
print("\n--- Menu choice validation ---")
print("Choose a subject:")
print("1. Math")
print("2. Science")
print("3. English")
choice = int(input("Enter 1, 2, or 3: "))
while choice < 1 or choice > 3:
    print("Please enter 1, 2, or 3 only.")
    choice = int(input("Enter 1, 2, or 3: "))
print("You chose option", choice)
