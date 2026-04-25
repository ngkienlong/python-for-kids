"""
Lesson 18 - Example 01: The Power Operator **
Shows how to use ** to calculate powers
"""

# Basic powers
print("--- Basic Powers ---")
print(2 ** 3)       # 2 to the power 3 = 8
print(5 ** 2)       # 5 squared = 25
print(3 ** 4)       # 3 to the power 4 = 81
print(10 ** 6)      # 10 to the power 6 = 1,000,000

# Power of zero: any number to the power 0 = 1
print("\n--- Power of Zero ---")
print(2 ** 0)       # 1
print(100 ** 0)     # 1
print(7 ** 0)       # 1

# Power of one: any number to the power 1 = itself
print("\n--- Power of One ---")
print(5 ** 1)       # 5
print(99 ** 1)      # 99

# Storing results in variables
base = 3
exponent = 5
result = base ** exponent
print(f"\n{base} to the power {exponent} = {result}")
