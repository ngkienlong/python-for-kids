# example_02_or.py
# Lesson 7: The "or" operator
# "or" is True when AT LEAST ONE condition is True.
# In Scratch: the "<A> or <B>" block.

age = int(input("Enter your age: "))

# Get a discount if you are a child OR a senior
if age < 18 or age > 60:
    print("You get a discount! Price: 50000 dong")
else:
    print("Full price: 100000 dong")

# Truth table for "or":
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False  ← only False when BOTH are False
