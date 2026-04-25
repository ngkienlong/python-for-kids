# example_02_input_number.py
# Lesson 4: Reading numbers with input()
# IMPORTANT: input() always returns a STRING, even if the user types a number!

# This reads a string — we cannot do math with it yet
raw = input("Enter a number: ")
print("You typed:", raw)
print("Type is:", type(raw))   # <class 'str'>

# To do math, we must convert to int or float
number = int(input("Enter a whole number: "))
print("Your number plus 10 is:", number + 10)
print("Type is:", type(number))   # <class 'int'>
