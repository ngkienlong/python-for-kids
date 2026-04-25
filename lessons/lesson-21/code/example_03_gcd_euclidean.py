"""
Lesson 21 - Example 03: GCD using the Euclidean Algorithm
GCD = Greatest Common Divisor
The Euclidean algorithm: while b != 0: a, b = b, a % b
"""
import math

# Manual Euclidean algorithm — step by step
print("--- Euclidean Algorithm (step by step) ---")
a = 48
b = 18
print(f"Finding GCD({a}, {b}):")
while b != 0:
    print(f"  a={a}, b={b} → new a={b}, new b={a % b}")
    a, b = b, a % b
print(f"GCD = {a}")

# Function version
def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test several pairs
print("\n--- GCD Examples ---")
pairs = [(12, 8), (100, 75), (7, 13), (36, 24), (1000, 250)]
for (x, y) in pairs:
    g = my_gcd(x, y)
    print(f"GCD({x}, {y}) = {g}")

# Compare with math.gcd
print("\n--- Verify with math.gcd ---")
print(f"math.gcd(48, 18) = {math.gcd(48, 18)}")
print(f"my_gcd(48, 18)   = {my_gcd(48, 18)}")

# User input
print("\n--- Your Numbers ---")
parts = input("Enter two numbers: ").split()
a = int(parts[0])
b = int(parts[1])
print(f"GCD({a}, {b}) = {my_gcd(a, b)}")
