# example_05_number_grid.py
# Lesson 10: Number grids and combination counting

# Grid showing i*j values
print("--- i*j grid (4x4) ---")
for i in range(1, 5):
    for j in range(1, 5):
        print(str(i * j).rjust(3), end="")
    print()

# Grid showing i+j values
print("\n--- i+j grid (4x4) ---")
for i in range(1, 5):
    for j in range(1, 5):
        print(str(i + j).rjust(3), end="")
    print()

# Count pairs where i + j is even
print("\n--- Pairs (i,j) where i+j is even (1 to 5) ---")
count = 0
for i in range(1, 6):
    for j in range(1, 6):
        if (i + j) % 2 == 0:
            print("(", i, "+", j, "=", i + j, ")", end="  ")
            count = count + 1
    print()
print("Total pairs:", count)
