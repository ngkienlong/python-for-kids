# example_03_even_odd.py
# Lesson 5: Check if a number is even or odd
# A number is even if it is divisible by 2 (remainder = 0).

number = int(input("Enter a whole number: "))

# Use the modulo operator % to find the remainder
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# How it works:
# 4 % 2 = 0  → even
# 7 % 2 = 1  → odd
# 0 % 2 = 0  → even (zero is even)
