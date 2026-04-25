"""
Lesson 22 - Example 05: Sequence Sums
Sum arithmetic, geometric, and Fibonacci sequences
"""

# Sum of arithmetic sequence
print("--- Sum of Arithmetic Sequence ---")
a = 1       # first term
d = 1       # common difference
n = 100     # number of terms

# Method 1: loop
total_loop = 0
for i in range(n):
    total_loop += a + i * d
print(f"Sum of 1 to 100 (loop): {total_loop}")

# Method 2: formula S = n/2 * (first + last)
last = a + (n - 1) * d
total_formula = n * (a + last) // 2
print(f"Sum of 1 to 100 (formula): {total_formula}")

# Sum of geometric sequence
print("\n--- Sum of Geometric Sequence ---")
a = 1
r = 2
n = 10
total = 0
term = a
for i in range(n):
    total += term
    term = term * r
print(f"Sum of 2^0 + 2^1 + ... + 2^9 = {total}")   # 1023

# Sum of Fibonacci numbers
print("\n--- Sum of First N Fibonacci Numbers ---")
N = int(input("How many Fibonacci numbers to sum? "))
a = 0
b = 1
total = 0
for i in range(N):
    total += a
    a, b = b, a + b
print(f"Sum of first {N} Fibonacci numbers = {total}")

# Sum of 1/k^2 (Basel problem approximation)
print("\n--- Sum of 1/k^2 (first 100 terms) ---")
total = 0.0
for k in range(1, 101):
    total += 1 / (k ** 2)
print(f"Sum ≈ {total:.6f}")
print(f"π^2/6 ≈ {3.14159265 ** 2 / 6:.6f}")   # the exact answer
