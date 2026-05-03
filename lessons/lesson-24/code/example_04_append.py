# example_04_append.py
# Lesson 24: Adding items to a list with append()
# append() always adds to the END of the list

# Start with an empty list
shopping = []
print("Start:", shopping)

# Add items one by one
shopping.append("milk")
print("After append milk:", shopping)

shopping.append("bread")
print("After append bread:", shopping)

shopping.append("eggs")
print("After append eggs:", shopping)

shopping.append("butter")
print("After append butter:", shopping)

print()
print("Final shopping list:")
print(shopping)
print("Total items:", len(shopping))

print()

# Build a list from user input
print("Enter 3 favorite foods:")
foods = []
food1 = input("Food 1: ")
foods.append(food1)
food2 = input("Food 2: ")
foods.append(food2)
food3 = input("Food 3: ")
foods.append(food3)

print("Your favorite foods:", foods)
print("You entered", len(foods), "foods.")
