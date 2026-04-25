# example_03_rectangle_pattern.py
# Lesson 10: Rectangle and hollow rectangle patterns

# Solid rectangle (4 rows, 8 columns)
print("--- Solid rectangle 4x8 ---")
for i in range(4):
    for j in range(8):
        print("*", end="")
    print()

# Hollow rectangle (5 rows, 10 columns)
print("\n--- Hollow rectangle 5x10 ---")
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        # Print * on the border, space inside
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Checkerboard pattern
print("\n--- Checkerboard 4x4 ---")
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
