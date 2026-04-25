# example_05_compare_numbers.py
# Lesson 5: Compare two numbers and find the larger one

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find the larger number
if a > b:
    print("The first number is larger:", a)
else:
    if a == b:
        print("Both numbers are equal:", a)
    else:
        print("The second number is larger:", b)

# Note: we nest an if/else inside the else block.
# In Lesson 6 we will learn elif, which makes this cleaner.
