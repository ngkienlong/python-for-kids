"""
Lesson 19 - Example 05: Circle Calculations
Area, circumference, and sphere volume using math.pi
"""
import math

print("=== Circle Calculator ===")
radius = float(input("Enter the radius: "))

# Circle area: A = π × r²
area = math.pi * radius ** 2

# Circle circumference: C = 2 × π × r
circumference = 2 * math.pi * radius

# Diameter: d = 2r
diameter = 2 * radius

print(f"\nRadius:        {radius}")
print(f"Diameter:      {diameter:.4f}")
print(f"Area:          {area:.4f}")
print(f"Circumference: {circumference:.4f}")

# Sphere volume: V = (4/3) × π × r³
volume = (4 / 3) * math.pi * radius ** 3

# Sphere surface area: SA = 4 × π × r²
surface_area = 4 * math.pi * radius ** 2

print(f"\n=== Sphere (same radius) ===")
print(f"Volume:       {volume:.4f}")
print(f"Surface area: {surface_area:.4f}")

# Comparison: circle vs sphere
print(f"\nNote: Sphere surface area = 4 × circle area")
print(f"4 × {area:.4f} = {4 * area:.4f}")
print(f"Surface area  = {surface_area:.4f}")
