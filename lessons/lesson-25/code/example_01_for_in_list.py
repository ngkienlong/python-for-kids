# example_01_for_in_list.py
# Lesson 25: Loop through a list using "for item in list"
# This is the simplest way to visit every item in a list

fruits = ["apple", "banana", "cherry", "mango"]

# Print each fruit
print("All fruits:")
for fruit in fruits:
    print(fruit)

print()

# Print each fruit in uppercase
print("Uppercase fruits:")
for fruit in fruits:
    print(fruit.upper())

print()

# Calculate the total length of all fruit names
total_length = 0
for fruit in fruits:
    total_length += len(fruit)
print("Total characters in all fruit names:", total_length)

print()

# Scratch connection:
# In Scratch: "for each [item] in [fruits]" → do something
# In Python:  for fruit in fruits:  → do something
numbers = [10, 20, 30, 40, 50]
print("Numbers doubled:")
for num in numbers:
    print(num * 2)
