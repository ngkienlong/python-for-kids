"""
Lesson 19 - Example 04: Perfect Squares
A perfect square has a whole-number square root: 1, 4, 9, 16, 25, ...
"""
import math

# Check if a single number is a perfect square
def is_perfect_square(n):
    root = math.sqrt(n)
    return root == int(root)

# Test some numbers
print("--- Perfect Square Check ---")
test_numbers = [1, 4, 7, 9, 15, 16, 25, 26, 36, 50, 100]
for n in test_numbers:
    root = math.sqrt(n)
    if root == int(root):
        print(f"{n:4d} → YES (sqrt = {int(root)})")
    else:
        print(f"{n:4d} → no  (sqrt ≈ {root:.4f})")

# List all perfect squares up to 200
print("\n--- Perfect Squares up to 200 ---")
squares = []
for n in range(1, 201):
    root = math.sqrt(n)
    if root == int(root):
        squares.append(n)
print(squares)

# Read from user
print("\n--- User Input ---")
n = int(input("Enter a number: "))
root = math.sqrt(n)
if root == int(root):
    print(f"{n} IS a perfect square (sqrt = {int(root)})")
else:
    print(f"{n} is NOT a perfect square (sqrt ≈ {root:.4f})")
