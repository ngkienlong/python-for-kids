"""
Lesson 20 - Example 05: Diagonal of a Rectangle
The diagonal is the hypotenuse of a right triangle
with legs equal to the width and height.
"""
import math

print("=== Rectangle Diagonal Calculator ===")
parts = input("Enter width and height (e.g. 6 8): ").split()
width = float(parts[0])
height = float(parts[1])

# Diagonal = sqrt(width^2 + height^2)
diagonal = math.sqrt(width ** 2 + height ** 2)

print(f"\nWidth:    {width}")
print(f"Height:   {height}")
print(f"Diagonal: {diagonal:.4f}")

# Also calculate perimeter and area
perimeter = 2 * (width + height)
area = width * height

print(f"\nPerimeter: {perimeter:.4f}")
print(f"Area:      {area:.4f}")

# Ladder problem: same formula
print("\n--- Ladder Problem ---")
print("A ladder leans against a wall.")
wall_height = float(input("Wall height (m): "))
base_distance = float(input("Distance from wall (m): "))
ladder_length = math.sqrt(wall_height ** 2 + base_distance ** 2)
print(f"Minimum ladder length: {ladder_length:.4f} m")
