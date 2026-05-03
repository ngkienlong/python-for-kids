"""
Lesson 21 - Example 02: Divisibility
n % k == 0 means n is divisible by k
"""

# Check divisibility for a single number
print("--- Divisibility of 24 ---")
n = 24
for k in range(1, 13):
    if n % k == 0:
        print(f"{n} is divisible by {k}")
    else:
        print(f"{n} is NOT divisible by {k}")

# Divisibility rules
print("\n--- Divisibility Rules ---")
test = 123
print(f"Number: {test}")
print(f"Divisible by 2? {test % 2 == 0}  (last digit: {test % 10})")
print(f"Divisible by 3? {test % 3 == 0}  (digit sum: {1+2+3})")
print(f"Divisible by 5? {test % 5 == 0}  (last digit: {test % 10})")
print(f"Divisible by 9? {test % 9 == 0}  (digit sum: {1+2+3})")

# User input
print("\n--- Check Your Number ---")
n = int(input("Enter a number: "))
print(f"Divisible by 2: {n % 2 == 0}")
print(f"Divisible by 3: {n % 3 == 0}")
print(f"Divisible by 5: {n % 5 == 0}")
print(f"Divisible by 10: {n % 10 == 0}")
