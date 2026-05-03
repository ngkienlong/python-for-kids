# example_04_edge_cases.py
# Lesson 33: Demonstrate edge case handling
# Edge cases are unusual inputs that can break your program

print("=== Edge Case 1: Empty list ===")

def safe_average(numbers):
    """Calculate average, handling empty list."""
    if len(numbers) == 0:
        return "No data"
    return sum(numbers) / len(numbers)

print(safe_average([10, 20, 30]))   # 20.0
print(safe_average([]))              # No data

print()
print("=== Edge Case 2: Division by zero ===")

def safe_divide(a, b):
    """Divide a by b, handling zero divisor."""
    if b == 0:
        return "Error: division by zero"
    return a / b

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error: division by zero

print()
print("=== Edge Case 3: Negative numbers ===")

def count_positive(numbers):
    """Count positive numbers in a list."""
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

print(count_positive([1, -2, 3, -4, 5]))   # 3
print(count_positive([-1, -2, -3]))         # 0
print(count_positive([]))                    # 0

print()
print("=== Edge Case 4: Single item ===")

def find_max(numbers):
    """Find maximum, handling single item and empty list."""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([5]))           # 5 (single item)
print(find_max([3, 7, 1]))    # 7 (normal)
print(find_max([]))            # None (empty)

print()
print("=== Edge Case 5: N = 0 in a loop ===")

def sum_to_n(n):
    """Sum from 1 to N. Handle N = 0."""
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to_n(5))    # 15
print(sum_to_n(1))    # 1
print(sum_to_n(0))    # 0
print(sum_to_n(-3))   # 0
