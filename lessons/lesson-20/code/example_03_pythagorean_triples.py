"""
Lesson 20 - Example 03: Finding Pythagorean Triples
A triple (a, b, c) satisfies a^2 + b^2 = c^2 with whole numbers
"""

print("=== Pythagorean Triples up to 50 ===")
print("(a, b, c) where a <= b <= c and a^2 + b^2 = c^2\n")

count = 0
for a in range(1, 51):
    for b in range(a, 51):      # b >= a to avoid duplicates
        for c in range(b, 51):  # c >= b (c is the largest)
            if a ** 2 + b ** 2 == c ** 2:
                print(f"({a:2d}, {b:2d}, {c:2d})  →  {a}^2 + {b}^2 = {a**2} + {b**2} = {c**2} = {c}^2")
                count += 1

print(f"\nTotal triples found: {count}")

# Famous triples
print("\n--- Famous Pythagorean Triples ---")
famous = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
for (a, b, c) in famous:
    print(f"({a}, {b}, {c}): {a}^2 + {b}^2 = {a**2 + b**2} = {c}^2 ✓")
