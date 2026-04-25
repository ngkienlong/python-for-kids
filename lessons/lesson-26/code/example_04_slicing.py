# example_04_slicing.py
# Lesson 26: List slicing — get a portion of a list
# Syntax: list[start:stop]  (stop is NOT included)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Full list:", numbers)
print("Indices:  ", list(range(len(numbers))))

print()

# Basic slicing
print("numbers[2:5]:", numbers[2:5])    # index 2, 3, 4 → [30, 40, 50]
print("numbers[0:3]:", numbers[0:3])    # index 0, 1, 2 → [10, 20, 30]
print("numbers[7:10]:", numbers[7:10])  # index 7, 8, 9 → [80, 90, 100]

print()

# Omit start or stop
print("numbers[:4]:", numbers[:4])      # from start to index 3 → [10, 20, 30, 40]
print("numbers[6:]:", numbers[6:])      # from index 6 to end → [70, 80, 90, 100]
print("numbers[:]:", numbers[:])        # full copy → [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print()

# Practical use: get first 3 and last 3
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])

print()

# Get the middle section
n = len(numbers)
middle_start = n // 4
middle_end = 3 * n // 4
print("Middle section:", numbers[middle_start:middle_end])
