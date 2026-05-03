# example_04_list_comprehension.py
# Lesson 27: List comprehension — create lists in one line
# Syntax: [expression for item in list]
# Syntax: [expression for item in list if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original:", numbers)

# Double every number
doubled = [x * 2 for x in numbers]
print("Doubled:", doubled)

# Square every number
squared = [x ** 2 for x in numbers]
print("Squared:", squared)

# Keep only even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)

# Keep only numbers greater than 5
big = [x for x in numbers if x > 5]
print("Greater than 5:", big)

# Square only the even numbers
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("Squares of evens:", even_squares)

print()

# Compare: loop vs comprehension
# Loop version:
result_loop = []
for x in numbers:
    if x % 3 == 0:
        result_loop.append(x * 10)
print("Multiples of 3, times 10 (loop):", result_loop)

# Comprehension version (same result, one line):
result_comp = [x * 10 for x in numbers if x % 3 == 0]
print("Multiples of 3, times 10 (comp):", result_comp)

print()

# Normalize a list (divide each by max)
scores = [40, 60, 80, 100, 50]
maximum = max(scores)
normalized = [round(x / maximum, 2) for x in scores]
print("Original scores:", scores)
print("Normalized:", normalized)
