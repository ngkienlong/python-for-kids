# example_03_remove_insert.py
# Lesson 26: remove(), insert(), and pop()

# --- remove() ---
fruits = ["apple", "banana", "cherry", "banana", "mango"]
print("Original:", fruits)

fruits.remove("banana")   # removes the FIRST "banana"
print("After remove('banana'):", fruits)

# --- insert() ---
numbers = [10, 20, 40, 50]
print("\nOriginal:", numbers)

numbers.insert(2, 30)   # insert 30 at index 2
print("After insert(2, 30):", numbers)

numbers.insert(0, 5)    # insert 5 at the beginning
print("After insert(0, 5):", numbers)

# --- pop() ---
stack = ["first", "second", "third", "fourth"]
print("\nStack:", stack)

item = stack.pop()       # remove and return last item
print("Popped:", item)
print("Stack now:", stack)

item2 = stack.pop(0)     # remove and return item at index 0
print("Popped index 0:", item2)
print("Stack now:", stack)

print()

# Practical example: a to-do list
todo = ["buy milk", "do homework", "clean room", "read book"]
print("To-do list:", todo)

# Mark first task as done (remove it)
done = todo.pop(0)
print("Completed:", done)
print("Remaining:", todo)

# Add urgent task at the beginning
todo.insert(0, "call mom")
print("After adding urgent task:", todo)
