"""
Lesson 23 - Example 05: Real-World Math
Combines compound interest + Pythagorean theorem + area in one program
"""
import math

print("=== Real-World Math Challenges ===\n")

# --- Challenge 1: Savings Goal ---
print("--- Challenge 1: How long to reach a savings goal? ---")
P = float(input("Starting savings ($): "))
R = float(input("Annual interest rate (%): "))
goal = float(input("Savings goal ($): "))

balance = P
years = 0
while balance < goal:
    balance = balance * (1 + R / 100)
    years += 1

print(f"It takes {years} years to reach ${goal:.2f}")
print(f"Final balance: ${balance:.2f}")

# --- Challenge 2: Staircase Handrail ---
print("\n--- Challenge 2: Staircase Handrail ---")
N = int(input("Number of steps: "))
step_w = float(input("Step width (m): "))
step_h = float(input("Step height (m): "))

total_width = N * step_w
total_height = N * step_h
handrail = math.sqrt(total_width ** 2 + total_height ** 2)

print(f"Total horizontal span: {total_width:.2f} m")
print(f"Total vertical rise:   {total_height:.2f} m")
print(f"Handrail length:       {handrail:.4f} m")

# --- Challenge 3: Tile a Room ---
print("\n--- Challenge 3: Tile a Room ---")
room_w = float(input("Room width (m): "))
room_h = float(input("Room height (m): "))
tile_size = float(input("Tile side length (m): "))

room_area = room_w * room_h
tile_area = tile_size ** 2
tiles_needed = math.ceil(room_area / tile_area)
leftover = tiles_needed * tile_area - room_area

print(f"Room area:    {room_area:.4f} m²")
print(f"Tile area:    {tile_area:.4f} m²")
print(f"Tiles needed: {tiles_needed}")
print(f"Leftover:     {leftover:.4f} m²")
