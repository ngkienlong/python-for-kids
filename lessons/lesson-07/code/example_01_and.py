# example_01_and.py
# Lesson 7: The "and" operator
# "and" is True only when BOTH conditions are True.
# In Scratch: the "<A> and <B>" block.

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

# Both conditions must be True to ride
if age >= 10 and height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you cannot ride.")

# Truth table for "and":
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False
