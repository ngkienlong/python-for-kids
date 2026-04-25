# example_03_accumulator.py
# Lesson 8: The accumulator pattern
# An accumulator collects a running total as the loop runs.

# Sum of 1 to 10
total = 0                    # start the accumulator at 0
for i in range(1, 11):       # i goes from 1 to 10
    total = total + i        # add i to the running total
    print("After adding", i, "-> total =", total)

print("Final sum:", total)   # 1+2+3+...+10 = 55

# Count how many even numbers are in range 1 to 20
print("\n--- Counting even numbers from 1 to 20 ---")
count = 0
for i in range(1, 21):
    if i % 2 == 0:           # if i is even
        count = count + 1    # increment the counter
print("Even numbers found:", count)

# Product accumulator (factorial of 5)
print("\n--- 5! = 1 x 2 x 3 x 4 x 5 ---")
product = 1                  # start at 1 (not 0!) for multiplication
for i in range(1, 6):
    product = product * i
print("5! =", product)
