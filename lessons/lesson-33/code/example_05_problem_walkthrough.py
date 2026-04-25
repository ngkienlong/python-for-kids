# example_05_problem_walkthrough.py
# Lesson 33: Solve a medium problem step by step with comments
# Problem: Read N numbers, find the two numbers closest to each other

# ============================================================
# STEP 1: UNDERSTAND THE PROBLEM
# Input: N numbers (N >= 2)
# Output: The two numbers with the smallest difference between them
# Edge case: What if multiple pairs have the same minimum difference?
#            → Print the first pair found
# ============================================================

# ============================================================
# STEP 2: PLAN (pseudocode)
# 1. Read N numbers into a list
# 2. Set min_diff = a very large number (infinity)
# 3. Set closest_pair = (None, None)
# 4. For each pair (i, j) where i < j:
#    a. Calculate diff = |numbers[i] - numbers[j]|
#    b. If diff < min_diff:
#       - Update min_diff = diff
#       - Update closest_pair = (numbers[i], numbers[j])
# 5. Print closest_pair
# ============================================================

# ============================================================
# STEP 3: CODE
# ============================================================

print("Find the two closest numbers")
n = int(input("How many numbers? "))

# Read numbers
numbers = []
for i in range(n):
    num = int(input("Number " + str(i + 1) + ": "))
    numbers.append(num)

print("Numbers:", numbers)

# Find the closest pair
min_diff = float('inf')   # start with "infinity"
closest_a = None
closest_b = None

for i in range(n):
    for j in range(i + 1, n):
        diff = abs(numbers[i] - numbers[j])
        if diff < min_diff:
            min_diff = diff
            closest_a = numbers[i]
            closest_b = numbers[j]

print("Closest pair:", closest_a, "and", closest_b)
print("Difference:", min_diff)

# ============================================================
# STEP 4: TEST
# Test 1: [1, 5, 3, 19, 18, 25] → 18 and 19 (diff = 1)
# Test 2: [10, 20, 30] → 10 and 20 (diff = 10)
# Test 3: [5, 5, 10] → 5 and 5 (diff = 0)
# ============================================================
