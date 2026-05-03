"""
Lesson 23 - Example 01: Combined Math
Uses **, sqrt, and sequences together
"""
import math

print("=== Combined Math: Powers, Roots, and Sequences ===")

# Powers of 2 and their square roots
print("\n--- Powers of 2 and Square Roots ---")
for i in range(11):
    value = 2 ** i
    root = math.sqrt(value)
    is_perfect = (root == int(root))
    marker = " ← perfect square" if is_perfect else ""
    print(f"2^{i:2d} = {value:5d}   sqrt = {root:.4f}{marker}")

# Fibonacci numbers and their squares
print("\n--- Fibonacci Numbers and Their Squares ---")
a = 0
b = 1
for i in range(10):
    sq = a ** 2
    root = math.sqrt(a) if a > 0 else 0
    print(f"F({i}) = {a:3d}   F({i})^2 = {sq:5d}   sqrt(F({i})) = {root:.4f}")
    a, b = b, a + b

# Sum of squares of first N natural numbers
print("\n--- Sum of Squares ---")
N = int(input("Enter N: "))
total = sum(k ** 2 for k in range(1, N + 1))
formula = N * (N + 1) * (2 * N + 1) // 6   # closed-form formula
print(f"Sum of 1^2 + 2^2 + ... + {N}^2 = {total}")
print(f"Formula N(N+1)(2N+1)/6 = {formula}")
