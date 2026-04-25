# example_03_review_loops.py
# Lesson 34: Review — for loop, while loop, and nested loops

# --- For loop ---
print("=== For Loop ===")
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("Even numbers 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

print("Countdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Blast off!")

print()

# --- While loop ---
print("=== While Loop ===")
print("Powers of 2 up to 1000:")
power = 1
while power <= 1000:
    print(power, end=" ")
    power *= 2
print()

print("Collatz sequence starting from 27:")
n = 27
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count += 1
print("Reached 1 in", count, "steps")

print()

# --- Nested loops ---
print("=== Nested Loops ===")
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

print()
print("Triangle pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print()
print("Number grid:")
for i in range(1, 4):
    for j in range(1, 4):
        print(str(i) + "x" + str(j) + "=" + str(i*j), end="  ")
    print()
