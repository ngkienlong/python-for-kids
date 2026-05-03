"""
Lesson 20 - Example 04: Distance Formula
Distance = sqrt((x2-x1)^2 + (y2-y1)^2)
This is the Pythagorean theorem applied to coordinates.
"""
import math

print("=== Distance Calculator ===")
print("Enter two points:")
parts1 = input("Point 1 (x1 y1): ").split()
parts2 = input("Point 2 (x2 y2): ").split()

x1, y1 = float(parts1[0]), float(parts1[1])
x2, y2 = float(parts2[0]), float(parts2[1])

# Calculate horizontal and vertical distances
dx = x2 - x1    # horizontal distance
dy = y2 - y1    # vertical distance

# Apply Pythagorean theorem
distance = math.sqrt(dx ** 2 + dy ** 2)

print(f"\nPoint 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Horizontal distance (dx): {dx}")
print(f"Vertical distance (dy):   {dy}")
print(f"Distance: sqrt({dx}^2 + {dy}^2) = sqrt({dx**2} + {dy**2}) = {distance:.4f}")

# Example: distance from origin
print("\n--- Distance from Origin ---")
for (px, py) in [(3, 4), (5, 12), (1, 1), (0, 5)]:
    d = math.sqrt(px ** 2 + py ** 2)
    print(f"({px}, {py}) → distance from (0,0) = {d:.4f}")
