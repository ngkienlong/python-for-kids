# example_02_range_variants.py
# Lesson 8: Different ways to use range()

# range(start, stop) — start is included, stop is NOT included
print("--- range(1, 6): numbers 1 to 5 ---")
for i in range(1, 6):
    print(i)

# range(start, stop, step) — jump by step each time
print("\n--- range(1, 10, 2): odd numbers 1 to 9 ---")
for i in range(1, 10, 2):
    print(i)

# range with step 10
print("\n--- range(0, 101, 10): multiples of 10 ---")
for i in range(0, 101, 10):
    print(i)

# range(start, stop, -1) — count DOWN
print("\n--- range(5, 0, -1): countdown from 5 ---")
for i in range(5, 0, -1):
    print(i)
print("Blast off!")
