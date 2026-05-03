"""
Lesson 21 - Example 01: Even and Odd Numbers
Use n % 2 to check if a number is even or odd
"""

# Basic even/odd check
print("--- Even or Odd? ---")
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# User input
print("\n--- Your Number ---")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# Count even and odd numbers from 1 to 20
print("\n--- Count Even and Odd (1 to 20) ---")
even_count = 0
odd_count = 0
for i in range(1, 21):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers:  {odd_count}")
