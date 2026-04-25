"""
Lesson 19 - Example 01: Square Root with math.sqrt()
"""
import math

# Basic square roots
print("--- Square Roots ---")
print(math.sqrt(9))         # 3.0
print(math.sqrt(25))        # 5.0
print(math.sqrt(2))         # 1.4142135623730951
print(math.sqrt(100))       # 10.0

# sqrt() always returns a float
result = math.sqrt(16)
print(f"\nmath.sqrt(16) = {result}")
print(f"Type: {type(result)}")      # <class 'float'>

# Convert to int if needed
print(f"As integer: {int(result)}")

# Square roots of 1 through 10
print("\n--- Square Roots Table ---")
for n in range(1, 11):
    print(f"sqrt({n:2d}) = {math.sqrt(n):.4f}")

# Reading from user
print("\n--- User Input ---")
n = int(input("Enter a number: "))
print(f"sqrt({n}) = {math.sqrt(n):.4f}")
