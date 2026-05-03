# example_04_calculator.py
# Lesson 4: Simple calculator using input()
# Ask the user for two numbers, then print all four operations.

print("=== Simple Calculator ===")

# Read two numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Calculate and print all four operations
print("Sum:        ", a + b)
print("Difference: ", a - b)
print("Product:    ", a * b)

# Division — be careful if b is 0!
# (We will handle division by zero properly in Lesson 6.)
print("Quotient:   ", a / b)
