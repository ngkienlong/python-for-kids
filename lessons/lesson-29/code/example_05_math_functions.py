# example_05_math_functions.py
# Lesson 29: Math functions — area, perimeter, hypotenuse
import math

# Area of a circle
def area_circle(radius):
    return math.pi * radius * radius

# Perimeter (circumference) of a circle
def perimeter_circle(radius):
    return 2 * math.pi * radius

# Area of a rectangle
def area_rectangle(width, height):
    return width * height

# Perimeter of a rectangle
def perimeter_rectangle(width, height):
    return 2 * (width + height)

# Hypotenuse of a right triangle (Pythagorean theorem)
def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)

# Is a perfect square?
def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

# --- Test all functions ---
print("=== Circle (radius = 5) ===")
r = 5
print("Area:", round(area_circle(r), 2))
print("Perimeter:", round(perimeter_circle(r), 2))

print()
print("=== Rectangle (4 x 6) ===")
print("Area:", area_rectangle(4, 6))
print("Perimeter:", perimeter_rectangle(4, 6))

print()
print("=== Right Triangle (3, 4) ===")
print("Hypotenuse:", hypotenuse(3, 4))   # should be 5.0

print()
print("=== Perfect Squares ===")
for n in [4, 9, 10, 16, 25, 30]:
    print(n, "->", is_perfect_square(n))
