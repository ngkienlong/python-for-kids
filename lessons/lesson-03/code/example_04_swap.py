# Lesson 3 - Example 4: Swapping two variables
# Use a temporary variable to swap values.

a = 5
b = 10

print("Before:", a, b)   # Before: 5 10

# Method 1: use a temporary variable
temp = a    # save a in temp
a = b       # put b's value into a
b = temp    # put temp (old a) into b

print("After:", a, b)    # After: 10 5

# Method 2: Python shortcut (one line!)
x = 1
y = 2
x, y = y, x
print("Swapped:", x, y)  # Swapped: 2 1
