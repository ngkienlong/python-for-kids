# example_01_basic_for.py
# Lesson 8: Basic for loop
# The for loop repeats code a fixed number of times.
# In Scratch this is like the "repeat N" block.

# Print "Hello" 5 times
print("--- Printing Hello 5 times ---")
for i in range(5):
    print("Hello")

# The loop variable i counts each iteration
print("\n--- Loop variable i ---")
for i in range(5):
    print("i =", i)

# range(5) gives: 0, 1, 2, 3, 4
# It starts at 0 and stops BEFORE 5
print("\n--- range(5) gives 0 to 4 ---")
for i in range(5):
    print(i)
