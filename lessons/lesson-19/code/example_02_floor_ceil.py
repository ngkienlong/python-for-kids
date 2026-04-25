"""
Lesson 19 - Example 02: Floor and Ceiling
math.floor() rounds down, math.ceil() rounds up
"""
import math

# Floor: always rounds DOWN
print("--- math.floor() ---")
print(math.floor(3.2))      # 3
print(math.floor(3.7))      # 3
print(math.floor(3.0))      # 3
print(math.floor(-3.2))     # -4  (down means more negative)
print(math.floor(-3.7))     # -4

# Ceiling: always rounds UP
print("\n--- math.ceil() ---")
print(math.ceil(3.2))       # 4
print(math.ceil(3.7))       # 4
print(math.ceil(3.0))       # 3  (already whole number)
print(math.ceil(-3.2))      # -3  (up means less negative)
print(math.ceil(-3.7))      # -3

# round(): rounds to nearest
print("\n--- round() ---")
print(round(3.2))           # 3
print(round(3.7))           # 4
print(round(3.14159, 2))    # 3.14
print(round(2.71828, 3))    # 2.718

# Practical example: tiles needed
print("\n--- Practical: Tiles Needed ---")
room_area = 17.5            # square meters
tile_area = 2.0             # square meters per tile
tiles_needed = math.ceil(room_area / tile_area)
print(f"Room area: {room_area} m²")
print(f"Tile area: {tile_area} m²")
print(f"Tiles needed: {tiles_needed}")  # 9 (can't use half a tile)
