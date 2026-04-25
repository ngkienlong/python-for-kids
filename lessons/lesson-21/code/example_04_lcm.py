"""
Lesson 21 - Example 04: LCM — Least Common Multiple
LCM(a, b) = a * b // GCD(a, b)
"""
import math

# LCM formula
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Examples
print("--- LCM Examples ---")
pairs = [(4, 6), (3, 5), (12, 18), (7, 11), (8, 12)]
for (a, b) in pairs:
    g = math.gcd(a, b)
    l = lcm(a, b)
    print(f"LCM({a}, {b}) = {a} × {b} ÷ GCD({a},{b}) = {a*b} ÷ {g} = {l}")

# Verify: LCM is divisible by both a and b
print("\n--- Verification ---")
a, b = 12, 18
l = lcm(a, b)
print(f"LCM({a}, {b}) = {l}")
print(f"{l} ÷ {a} = {l // a} (remainder {l % a})")
print(f"{l} ÷ {b} = {l // b} (remainder {l % b})")

# Practical use: when do two events coincide?
print("\n--- Practical Example ---")
print("Bus A comes every 6 minutes.")
print("Bus B comes every 8 minutes.")
print("Both buses just left. When will they leave together again?")
a, b = 6, 8
print(f"LCM({a}, {b}) = {lcm(a, b)} minutes")

# User input
print("\n--- Your Numbers ---")
parts = input("Enter two numbers: ").split()
a = int(parts[0])
b = int(parts[1])
print(f"LCM({a}, {b}) = {lcm(a, b)}")
