"""
Lesson 22 - Example 02: Geometric Sequences
A geometric sequence multiplies by the same number (r) each time.
"""

# Basic geometric sequence
print("--- Geometric Sequence: a=2, r=3 ---")
a = 2       # first term
r = 3       # common ratio
n = 6       # number of terms

term = a
for i in range(n):
    print(f"Term {i+1}: {term}")
    term = term * r

# Geometric sequence with fraction ratio
print("\n--- Geometric Sequence: a=64, r=0.5 ---")
term = 64.0
r = 0.5
for i in range(7):
    print(f"Term {i+1}: {term}")
    term = term * r

# Sum of geometric sequence
print("\n--- Sum of First 8 Terms (a=1, r=2) ---")
term = 1
r = 2
total = 0
for i in range(8):
    total += term
    term = term * r
print(f"Sum = {total}")   # 1+2+4+8+16+32+64+128 = 255

# User-defined geometric sequence
print("\n--- Your Sequence ---")
parts = input("Enter first term, ratio, count (e.g. 3 2 5): ").split()
a = int(parts[0])
r = int(parts[1])
n = int(parts[2])
term = a
print("Sequence: ", end="")
for i in range(n):
    if i > 0:
        print(", ", end="")
    print(term, end="")
    term = term * r
print()
