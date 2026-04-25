# example_04_triangle_pattern.py
# Lesson 10: Triangle patterns using nested loops

# Right triangle (growing)
print("--- Right triangle (growing) ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Right triangle (shrinking)
print("\n--- Right triangle (shrinking) ---")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Number triangle
print("\n--- Number triangle ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pyramid (centered triangle)
print("\n--- Pyramid ---")
n = 5
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
