# example_02_debug_example.py
# Lesson 33: Show a buggy program and how to fix it
# We demonstrate 3 common bugs and their fixes

print("=== Bug 1: Off-by-one error ===")
# BUGGY: Should print sum of 1 to N, but misses N
n = 5
total_buggy = 0
for i in range(n):       # range(5) = 0,1,2,3,4 — misses 5!
    total_buggy += i
print("Buggy result:", total_buggy)   # 10 (wrong, should be 15)

# FIXED: Use range(1, n+1) to include N
total_fixed = 0
for i in range(1, n + 1):   # range(1, 6) = 1,2,3,4,5 ✓
    total_fixed += i
print("Fixed result:", total_fixed)   # 15 ✓

print()
print("=== Bug 2: Wrong variable name ===")
# BUGGY: Uses wrong variable in the loop
numbers = [10, 20, 30, 40, 50]
total_buggy2 = 0
for num in numbers:
    total_buggy2 += num   # correct — uses num, not numbers

# A common mistake: accidentally using the list name
# total_buggy2 += numbers  ← this would cause a TypeError

print("Sum:", total_buggy2)   # 150 ✓

print()
print("=== Bug 3: Division by zero ===")
# BUGGY: Crashes if the list is empty
def average_buggy(nums):
    return sum(nums) / len(nums)   # crashes if len(nums) == 0!

# FIXED: Check for empty list first
def average_fixed(nums):
    if len(nums) == 0:
        return 0   # or return None, or print an error
    return sum(nums) / len(nums)

print("Average of [1,2,3]:", average_fixed([1, 2, 3]))   # 2.0
print("Average of []:", average_fixed([]))                 # 0

print()
print("=== Debugging tip: use print() to trace values ===")
# Add temporary print statements to see what's happening
numbers2 = [5, 3, 8, 1, 9]
maximum = numbers2[0]
print("DEBUG: starting maximum =", maximum)

for num in numbers2:
    print("DEBUG: checking", num, "vs maximum", maximum)
    if num > maximum:
        maximum = num
        print("DEBUG: updated maximum to", maximum)

print("Final maximum:", maximum)
