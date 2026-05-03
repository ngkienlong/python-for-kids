# example_04_patterns.py
# Lesson 8: Printing patterns with loops
# Use the loop variable to control how many characters to print.

# Growing star triangle
print("--- Growing triangle ---")
for i in range(1, 6):
    print("*" * i)

# Shrinking star triangle
print("\n--- Shrinking triangle ---")
for i in range(5, 0, -1):
    print("*" * i)

# Number pattern: row i has i copies of digit i
print("\n--- Number triangle ---")
for i in range(1, 6):
    print(str(i) * i)

# Multiplication table for 5
print("\n--- Multiplication table for 5 ---")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
