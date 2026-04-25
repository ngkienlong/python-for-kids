# example_02_multiplication_table.py
# Lesson 10: Multiplication table using nested loops

# Simple 5x5 multiplication table
print("--- 5x5 Multiplication Table ---")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(result, end="\t")   # \t = tab for alignment
    print()                       # new line after each row

# 10x10 multiplication table with better alignment
print("\n--- 10x10 Multiplication Table ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(str(i * j).rjust(4), end="")  # right-align in 4 spaces
    print()
