# example_02_access_items.py
# Lesson 24: Accessing list items by index
# IMPORTANT: Index starts at 0, not 1!

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

# Access by positive index (counting from the start)
print("Index 0:", fruits[0])   # apple  (first item)
print("Index 1:", fruits[1])   # banana (second item)
print("Index 2:", fruits[2])   # cherry (third item)
print("Index 3:", fruits[3])   # mango  (fourth item)
print("Index 4:", fruits[4])   # kiwi   (fifth item)

print()  # empty line

# Access by negative index (counting from the end)
print("Index -1:", fruits[-1])  # kiwi   (last item)
print("Index -2:", fruits[-2])  # mango  (second to last)
print("Index -3:", fruits[-3])  # cherry (third to last)
print("Index -4:", fruits[-4])  # banana
print("Index -5:", fruits[-5])  # apple  (first item)

print()

# Scratch connection:
# In Scratch: "item 1 of fruits" → In Python: fruits[0]
# In Scratch: "item 3 of fruits" → In Python: fruits[2]
# Remember: Scratch starts at 1, Python starts at 0!

# Using len() to find the last index
length = len(fruits)
print("Length:", length)
print("Last item using len:", fruits[length - 1])  # same as fruits[-1]
