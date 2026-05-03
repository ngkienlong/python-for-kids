# example_03_modify_list.py
# Lesson 24: Modifying (changing) items in a list

colors = ["red", "green", "blue"]
print("Original list:", colors)

# Change the item at index 1 (green → yellow)
colors[1] = "yellow"
print("After changing index 1:", colors)

# Change the first item
colors[0] = "purple"
print("After changing index 0:", colors)

# Change the last item using negative index
colors[-1] = "orange"
print("After changing index -1:", colors)

print()

# Example: update a student's score
scores = [85, 72, 90, 68, 95]
print("Original scores:", scores)

# Student at index 1 retook the test and got 88
scores[1] = 88
print("Updated scores:", scores)

print()

# Swap two items
items = ["A", "B", "C", "D"]
print("Before swap:", items)

# Swap index 0 and index 3
temp = items[0]       # save the first item
items[0] = items[3]   # put last item in first position
items[3] = temp       # put saved item in last position

print("After swap:", items)
