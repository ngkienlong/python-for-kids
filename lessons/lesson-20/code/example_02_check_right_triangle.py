"""
Lesson 20 - Example 02: Check if a Triangle is a Right Triangle
Sort sides first, then check a^2 + b^2 == c^2
"""
import math

print("=== Right Triangle Checker ===")
parts = input("Enter three sides (e.g. 3 4 5): ").split()
sides = sorted([float(x) for x in parts])
a, b, c = sides[0], sides[1], sides[2]

print(f"\nSorted sides: a={a}, b={b}, c={c} (c is largest)")
print(f"a^2 + b^2 = {a**2} + {b**2} = {a**2 + b**2}")
print(f"c^2 = {c**2}")

# Use a small tolerance for floating-point comparison
tolerance = 0.0001
if abs(a ** 2 + b ** 2 - c ** 2) < tolerance:
    print("→ RIGHT TRIANGLE ✓")
else:
    print("→ Not a right triangle ✗")

# Test several known triples
print("\n--- Testing Known Triples ---")
test_cases = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (3, 4, 6),      # not a right triangle
    (1, 1, 2),      # not a right triangle
]
for (x, y, z) in test_cases:
    sides = sorted([x, y, z])
    a, b, c = sides
    if a ** 2 + b ** 2 == c ** 2:
        print(f"({x}, {y}, {z}) → right triangle ✓")
    else:
        print(f"({x}, {y}, {z}) → not a right triangle ✗")
