# example_02_for_with_index.py
# Lesson 25: Loop with index using range(len(list))
# Use this when you need to know the position of each item

fruits = ["apple", "banana", "cherry", "mango"]

# Print each item with its index
print("Fruits with index:")
for i in range(len(fruits)):
    print(i, "->", fruits[i])

print()

# Print a numbered list (starting from 1)
print("Numbered list:")
for i in range(len(fruits)):
    print(str(i + 1) + ".", fruits[i])

print()

# Find the index of a specific item
target = "cherry"
for i in range(len(fruits)):
    if fruits[i] == target:
        print(target, "is at index", i)

print()

# Modify items using index
scores = [70, 85, 60, 90, 75]
print("Original scores:", scores)

# Add 5 bonus points to every score
for i in range(len(scores)):
    scores[i] = scores[i] + 5

print("After bonus:", scores)
