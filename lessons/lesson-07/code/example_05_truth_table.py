# example_05_truth_table.py
# Lesson 7: Print truth tables for and, or, not
# This program shows all possible combinations of True and False.

print("=== Truth Table: AND ===")
print("A       B       A and B")
print(True,  " ", True,  " ", True  and True)
print(True,  " ", False, " ", True  and False)
print(False, " ", True,  " ", False and True)
print(False, " ", False, " ", False and False)

print()

print("=== Truth Table: OR ===")
print("A       B       A or B")
print(True,  " ", True,  " ", True  or True)
print(True,  " ", False, " ", True  or False)
print(False, " ", True,  " ", False or True)
print(False, " ", False, " ", False or False)

print()

print("=== Truth Table: NOT ===")
print("A       not A")
print(True,  " ", not True)
print(False, " ", not False)

print()

# Precedence: not > and > or
# Use parentheses to make the order clear!
print("=== Precedence Example ===")
print("True or False and False =", True or False and False)
# Same as: True or (False and False) = True or False = True

print("(True or False) and False =", (True or False) and False)
# = True and False = False
