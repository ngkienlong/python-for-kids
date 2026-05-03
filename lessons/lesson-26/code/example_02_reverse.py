# example_02_reverse.py
# Lesson 26: Reversing a list with reverse()

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]
print("Original:", fruits)

# Reverse the list in place
fruits.reverse()
print("Reversed:", fruits)

print()

# Reverse a list of numbers
numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)
numbers.reverse()
print("Reversed:", numbers)

print()

# Difference between sort(reverse=True) and reverse()
# sort(reverse=True) = sort then flip (largest first)
# reverse() = just flip the current order

data = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original data:", data)

# Make a copy to compare
data_copy = data[:]   # slicing with [:] makes a copy

data.sort(reverse=True)
print("sort(reverse=True):", data)   # sorted: largest first

data_copy.reverse()
print("reverse():", data_copy)       # just flipped: not sorted
