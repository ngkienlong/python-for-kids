# example_03_find_min_max.py
# Lesson 11: Finding minimum and maximum values in a loop

# Find the largest multiple of 13 up to 200
print("--- Largest multiple of 13 up to 200 ---")
largest = 0
for i in range(1, 201):
    if i % 13 == 0:
        largest = i    # keep updating — last one is the largest
print("Largest:", largest)

# Find the smallest number > 100 that is divisible by 17
print("\n--- Smallest multiple of 17 greater than 100 ---")
found = False
for i in range(101, 200):
    if i % 17 == 0:
        print("Found:", i)
        found = True
        break

# Find min and max from user input
print("\n--- Find min and max of 5 numbers ---")
first = int(input("Enter number 1: "))
min_val = first
max_val = first
for i in range(2, 6):
    n = int(input("Enter number " + str(i) + ": "))
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
print("Minimum:", min_val)
print("Maximum:", max_val)
