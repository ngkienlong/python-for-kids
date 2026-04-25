"""
Lesson 22 - Example 03: Fibonacci Sequence
Each term = sum of the two previous terms.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

# Print first 15 Fibonacci numbers
print("--- First 15 Fibonacci Numbers ---")
a = 0       # F(0)
b = 1       # F(1)
for i in range(15):
    print(f"F({i}) = {a}")
    a, b = b, a + b     # key step: both update at the same time

# Find the Nth Fibonacci number
print("\n--- Find the Nth Fibonacci Number ---")
N = int(input("Enter N (0-indexed): "))
a = 0
b = 1
for i in range(N):
    a, b = b, a + b
print(f"F({N}) = {a}")

# Sum of Fibonacci numbers up to a limit
print("\n--- Fibonacci Numbers up to 100 ---")
a = 0
b = 1
total = 0
fibs = []
while a <= 100:
    fibs.append(a)
    total += a
    a, b = b, a + b
print(f"Numbers: {fibs}")
print(f"Sum: {total}")

# Check if a number is Fibonacci
print("\n--- Is 34 a Fibonacci Number? ---")
target = 34
a = 0
b = 1
found = False
while a <= target:
    if a == target:
        found = True
        break
    a, b = b, a + b
print(f"34 is Fibonacci: {found}")
