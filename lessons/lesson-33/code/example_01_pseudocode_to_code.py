# example_01_pseudocode_to_code.py
# Lesson 33: Show pseudocode as comments, then implement the code
# Problem: Read N numbers, find the average, print numbers above average

# ============================================================
# STEP 1: UNDERSTAND
# Input: N numbers
# Output: numbers that are above the average
# Edge cases: N = 0 (no numbers), all same (none above average)
# ============================================================

# ============================================================
# STEP 2: PSEUDOCODE (plan in English)
# 1. Read N
# 2. If N = 0, print "No numbers" and stop
# 3. Read N numbers into a list
# 4. Calculate the sum of all numbers
# 5. Calculate average = sum / N
# 6. For each number in the list:
#    a. If number > average, print it
# ============================================================

# ============================================================
# STEP 3: CODE (translate pseudocode to Python)
# ============================================================

# Step 1: Read N
n = int(input("How many numbers? "))

# Step 2: Handle edge case
if n == 0:
    print("No numbers")
else:
    # Step 3: Read numbers
    numbers = []
    for i in range(n):
        num = int(input("Enter number " + str(i + 1) + ": "))
        numbers.append(num)

    # Step 4 & 5: Calculate average
    total = sum(numbers)
    average = total / n
    print("Numbers:", numbers)
    print("Average:", round(average, 2))

    # Step 6: Print numbers above average
    print("Numbers above average:")
    found_any = False
    for num in numbers:
        if num > average:
            print(num)
            found_any = True

    if not found_any:
        print("(none)")
