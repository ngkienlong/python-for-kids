# example_04_search_list.py
# Lesson 25: Search for an item in a list (linear search)
# We check each item one by one until we find the target

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("Students:", students)

# Search for a name
target = "Charlie"
found = False

for i in range(len(students)):
    if students[i] == target:
        found = True
        print(target, "found at index", i)
        break   # stop searching once found

if not found:
    print(target, "not found in the list")

print()

# Search for a number
numbers = [15, 42, 7, 88, 23, 56, 31]
print("Numbers:", numbers)

search = 88
found_index = -1   # -1 means "not found yet"

for i in range(len(numbers)):
    if numbers[i] == search:
        found_index = i
        break

if found_index != -1:
    print(search, "found at index", found_index)
else:
    print(search, "not found")

print()

# Count how many times a value appears
votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Alice"]
print("Votes:", votes)

alice_votes = 0
bob_votes = 0
charlie_votes = 0

for vote in votes:
    if vote == "Alice":
        alice_votes += 1
    elif vote == "Bob":
        bob_votes += 1
    elif vote == "Charlie":
        charlie_votes += 1

print("Alice:", alice_votes, "votes")
print("Bob:", bob_votes, "votes")
print("Charlie:", charlie_votes, "votes")
