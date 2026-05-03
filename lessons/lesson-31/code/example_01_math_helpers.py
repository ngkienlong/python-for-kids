# example_01_math_helpers.py
# Lesson 31: Math helper functions
import math

def area_circle(r):
    """Return the area of a circle with radius r."""
    return math.pi * r * r

def area_rectangle(w, h):
    """Return the area of a rectangle."""
    return w * h

def hypotenuse(a, b):
    """Return the hypotenuse of a right triangle (Pythagorean theorem)."""
    return math.sqrt(a * a + b * b)

def is_perfect_square(n):
    """Return True if n is a perfect square."""
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

def perimeter_rectangle(w, h):
    """Return the perimeter of a rectangle."""
    return 2 * (w + h)

# --- Test all functions ---
print("=== Circle ===")
for r in [1, 3, 5, 10]:
    print("radius", r, "-> area =", round(area_circle(r), 2))

print()
print("=== Rectangle ===")
print("4 x 6 -> area =", area_rectangle(4, 6))
print("4 x 6 -> perimeter =", perimeter_rectangle(4, 6))

print()
print("=== Hypotenuse ===")
print("3, 4 ->", hypotenuse(3, 4))    # 5.0
print("5, 12 ->", hypotenuse(5, 12))  # 13.0
print("8, 15 ->", hypotenuse(8, 15))  # 17.0

print()
print("=== Perfect Squares ===")
for n in range(1, 26):
    if is_perfect_square(n):
        print(n, "is a perfect square")
