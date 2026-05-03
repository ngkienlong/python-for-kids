# example_01_sort.py
# Lesson 26: Sorting a list with sort()

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Original:", numbers)

# Sort ascending (smallest to largest)
numbers.sort()
print("Sorted ascending:", numbers)

# Sort descending (largest to smallest)
numbers.sort(reverse=True)
print("Sorted descending:", numbers)

print()

# Sort a list of names alphabetically
names = ["Charlie", "Alice", "Eve", "Bob", "Diana"]
print("Original names:", names)
names.sort()
print("Sorted alphabetically:", names)

print()

# Sort scores and find top 3
scores = [72, 95, 88, 61, 79, 84, 91]
print("Scores:", scores)
scores.sort(reverse=True)
print("Sorted (best first):", scores)
print("Top 3:", scores[0], scores[1], scores[2])
