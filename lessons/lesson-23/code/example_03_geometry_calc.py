"""
Lesson 23 - Example 03: Geometry Calculations
Area, perimeter, diagonal, and circle — all in one program
"""
import math

print("=== Geometry Calculator ===")
print("Choose a shape:")
print("1. Rectangle")
print("2. Circle")
print("3. Right Triangle")
choice = int(input("Enter 1, 2, or 3: "))

if choice == 1:
    # Rectangle
    parts = input("Enter width and height: ").split()
    w = float(parts[0])
    h = float(parts[1])
    area = w * h
    perimeter = 2 * (w + h)
    diagonal = math.sqrt(w ** 2 + h ** 2)
    print(f"\nRectangle {w} × {h}:")
    print(f"  Area:      {area:.4f}")
    print(f"  Perimeter: {perimeter:.4f}")
    print(f"  Diagonal:  {diagonal:.4f}")

elif choice == 2:
    # Circle
    r = float(input("Enter radius: "))
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    diameter = 2 * r
    print(f"\nCircle with radius {r}:")
    print(f"  Diameter:      {diameter:.4f}")
    print(f"  Area:          {area:.4f}")
    print(f"  Circumference: {circumference:.4f}")

elif choice == 3:
    # Right triangle
    parts = input("Enter legs a and b: ").split()
    a = float(parts[0])
    b = float(parts[1])
    c = math.sqrt(a ** 2 + b ** 2)
    area = a * b / 2
    perimeter = a + b + c
    print(f"\nRight Triangle with legs {a} and {b}:")
    print(f"  Hypotenuse: {c:.4f}")
    print(f"  Area:       {area:.4f}")
    print(f"  Perimeter:  {perimeter:.4f}")

else:
    print("Invalid choice.")
