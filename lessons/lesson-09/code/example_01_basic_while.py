# example_01_basic_while.py
# Lesson 9: Basic while loop
# A while loop runs as long as the condition is True.
# In Scratch this is like the "repeat until" block (but reversed).

# Count from 1 to 5
print("--- Counting from 1 to 5 ---")
count = 1               # start value
while count <= 5:       # condition: keep going while count <= 5
    print(count)        # loop body
    count = count + 1   # IMPORTANT: update count or loop runs forever!

print("Loop finished!")

# Show the condition becoming False
print("\n--- Watching the condition ---")
number = 10
while number > 0:
    print("number =", number, "| condition (number > 0) is True")
    number = number - 3
print("number =", number, "| condition (number > 0) is False -> loop stopped")
