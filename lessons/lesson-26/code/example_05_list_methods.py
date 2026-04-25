# example_05_list_methods.py
# Lesson 26: count() and index() methods

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("List:", numbers)

# count() — how many times does a value appear?
print("\ncount() examples:")
print("Count of 1:", numbers.count(1))   # 2
print("Count of 5:", numbers.count(5))   # 3
print("Count of 7:", numbers.count(7))   # 0 (not in list)

# index() — where is the first occurrence?
print("\nindex() examples:")
print("Index of 4:", numbers.index(4))   # 2
print("Index of 5:", numbers.index(5))   # 4 (first occurrence)
print("Index of 9:", numbers.index(9))   # 5

print()

# Practical example: find the most common score
scores = [85, 90, 85, 72, 90, 85, 78, 90, 85]
print("Scores:", scores)
print("85 appears:", scores.count(85), "times")
print("90 appears:", scores.count(90), "times")
print("First 85 is at index:", scores.index(85))

print()

# Summary of all list methods
sample = [5, 3, 8, 1, 9, 3, 7]
print("Original:", sample)
print("Length:", len(sample))
print("Count of 3:", sample.count(3))
print("Index of 8:", sample.index(8))

sample.sort()
print("After sort():", sample)

sample.reverse()
print("After reverse():", sample)

sample.insert(2, 99)
print("After insert(2, 99):", sample)

sample.remove(99)
print("After remove(99):", sample)

popped = sample.pop()
print("Popped:", popped, "| List now:", sample)
