"""
Lesson 20 - Example 01: Finding the Hypotenuse
c = sqrt(a^2 + b^2)
"""
import math

print("=== Hypotenuse Calculator ===")
a = float(input("Enter leg a: "))
b = float(input("Enter leg b: "))

# Apply the Pythagorean theorem
c = math.sqrt(a ** 2 + b ** 2)

print(f"\nLeg a = {a}")
print(f"Leg b = {b}")
print(f"Hypotenuse c = {c:.4f}")

# Verify: a^2 + b^2 should equal c^2
print(f"\nVerification: {a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}")
print(f"c^2 = {c**2:.4f}")

# Famous 3-4-5 example
print("\n--- Famous 3-4-5 Triangle ---")
a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)
print(f"a=3, b=4 → c = {c}")   # 5.0
