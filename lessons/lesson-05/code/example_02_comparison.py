# example_02_comparison.py
# Lesson 5: Comparison operators
# All comparisons return True or False (boolean values).

a = 10
b = 5

print(a == b)    # False  (10 is not equal to 5)
print(a != b)    # True   (10 is not equal to 5)
print(a > b)     # True   (10 is greater than 5)
print(a < b)     # False  (10 is not less than 5)
print(a >= 10)   # True   (10 is greater than or equal to 10)
print(a <= 9)    # False  (10 is not less than or equal to 9)

# IMPORTANT: == is comparison, = is assignment!
# a = 5   means: store 5 in a
# a == 5  means: is a equal to 5? (returns True or False)

x = 7
result = x > 5
print(result)         # True
print(type(result))   # <class 'bool'>
