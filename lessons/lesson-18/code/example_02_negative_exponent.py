"""
Lesson 18 - Example 02: Negative Exponents
A negative exponent means 1 divided by the positive power
"""

# Negative exponents produce fractions
print("--- Negative Exponents ---")
print(2 ** -1)      # 1/2 = 0.5
print(2 ** -2)      # 1/4 = 0.25
print(2 ** -3)      # 1/8 = 0.125
print(2 ** -4)      # 1/16 = 0.0625

# 10 to negative powers
print("\n--- Powers of 10 (negative) ---")
print(10 ** -1)     # 0.1
print(10 ** -2)     # 0.01
print(10 ** -3)     # 0.001
print(10 ** -6)     # 0.000001

# Verify: x ** -n is the same as 1 / (x ** n)
x = 4
n = 3
print(f"\n{x} ** -{n} = {x ** -n}")
print(f"1 / ({x} ** {n}) = {1 / (x ** n)}")
# Both give the same result!
