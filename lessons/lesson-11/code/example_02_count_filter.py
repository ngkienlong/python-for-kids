# example_02_count_filter.py
# Lesson 11: Filtering and counting with loops

# Filter: print only numbers divisible by 7 from 1 to 50
print("--- Multiples of 7 from 1 to 50 ---")
for i in range(1, 51):
    if i % 7 == 0:
        print(i)

# Count: how many numbers from 1 to 100 are divisible by 3 but not 9?
print("\n--- Count: divisible by 3 but not 9 (1 to 100) ---")
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 9 != 0:
        count = count + 1
print("Count:", count)

# Sum: sum of all numbers from 1 to 100 that end in digit 3 or 7
print("\n--- Sum of numbers ending in 3 or 7 (1 to 100) ---")
total = 0
for i in range(1, 101):
    last_digit = i % 10
    if last_digit == 3 or last_digit == 7:
        total = total + i
print("Sum:", total)
