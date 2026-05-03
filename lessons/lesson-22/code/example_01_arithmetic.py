"""
Lesson 22 - Example 01: Arithmetic Sequences
An arithmetic sequence adds the same number (d) each time.
"""

# Basic arithmetic sequence
print("--- Arithmetic Sequence: a=3, d=4 ---")
a = 3       # first term
d = 4       # common difference
n = 8       # number of terms

for i in range(n):
    term = a + i * d
    print(f"Term {i+1}: {term}")

# Sum of arithmetic sequence
print("\n--- Sum of First 10 Terms ---")
a = 1
d = 2
total = 0
for i in range(10):
    term = a + i * d
    total += term
print(f"Sum = {total}")   # 1+3+5+7+9+11+13+15+17+19 = 100

# User-defined arithmetic sequence
print("\n--- Your Sequence ---")
parts = input("Enter first term, difference, count (e.g. 5 3 6): ").split()
a = int(parts[0])
d = int(parts[1])
n = int(parts[2])
print(f"Sequence: ", end="")
for i in range(n):
    if i > 0:
        print(", ", end="")
    print(a + i * d, end="")
print()
