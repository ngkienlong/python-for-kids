"""
Lesson 22 - Example 04: Triangular and Square Numbers
Triangular: 1, 3, 6, 10, 15, 21, ...  T(n) = n*(n+1)/2
Square:     1, 4, 9, 16, 25, 36, ...  S(n) = n^2
"""

# Triangular numbers
print("--- Triangular Numbers ---")
for n in range(1, 11):
    tri = n * (n + 1) // 2
    # Visual: show as dots
    print(f"T({n:2d}) = {tri:3d}  {'*' * tri}")

# Square numbers
print("\n--- Square Numbers ---")
for n in range(1, 11):
    sq = n ** 2
    print(f"S({n:2d}) = {sq:3d}  {'*' * sq}")

# Check if a number is triangular
# T(k) = N → k^2 + k - 2N = 0 → k = (-1 + sqrt(1+8N)) / 2
import math
print("\n--- Is a Number Triangular? ---")
test_numbers = [1, 3, 6, 7, 10, 15, 16, 21]
for N in test_numbers:
    k = (-1 + math.sqrt(1 + 8 * N)) / 2
    if k == int(k):
        print(f"{N:3d} → YES (T({int(k)}))")
    else:
        print(f"{N:3d} → no")

# Numbers that are both triangular and square
print("\n--- Numbers that are both Triangular and Square (up to 1000) ---")
for N in range(1, 1001):
    # Check triangular
    k = (-1 + math.sqrt(1 + 8 * N)) / 2
    is_tri = (k == int(k))
    # Check square
    root = math.sqrt(N)
    is_sq = (root == int(root))
    if is_tri and is_sq:
        print(N)
