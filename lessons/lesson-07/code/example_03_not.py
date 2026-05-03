# example_03_not.py
# Lesson 7: The "not" operator
# "not" flips True to False and False to True.
# In Scratch: the "not <A>" block.

is_raining = False

# "not is_raining" flips False to True
if not is_raining:
    print("Great weather! Let's go outside.")
else:
    print("It is raining. Stay inside.")

# Another example: check if a number is NOT zero
n = int(input("Enter a number: "))
if not (n == 0):
    print(n, "is not zero")
else:
    print("The number is zero")

# Note: "not (n == 0)" is the same as "n != 0"
# Truth table for "not":
# not True  = False
# not False = True
