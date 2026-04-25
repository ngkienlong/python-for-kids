# example_01_nested_basic.py
# Lesson 10: Basic nested loops
# A nested loop is a loop inside another loop.

# Simple nested loop: outer runs 3 times, inner runs 4 times
print("--- Outer 3 x Inner 4 = 12 total iterations ---")
for i in range(3):              # outer loop
    for j in range(4):          # inner loop
        print("(", i, ",", j, ")", end=" ")
    print()                     # new line after each row

# Count total iterations
print("\n--- Counting total iterations ---")
total = 0
for i in range(3):
    for j in range(5):
        total = total + 1
print("Total iterations:", total, "(3 x 5 =", 3 * 5, ")")

# Nested loop with different variable names
print("\n--- Row and column labels ---")
for row in range(1, 4):
    for col in range(1, 5):
        print("R" + str(row) + "C" + str(col), end=" ")
    print()
