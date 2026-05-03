# example_03_test_cases.py
# Lesson 33: How to test a function with multiple test cases
# Good testing catches bugs before users find them!

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def max_of_list(numbers):
    """Return the maximum value in a list."""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# ============================================================
# Test is_prime()
# ============================================================
print("=== Testing is_prime() ===")

# Format: (input, expected_output)
prime_tests = [
    (0, False),    # 0 is not prime
    (1, False),    # 1 is not prime
    (2, True),     # 2 is the smallest prime
    (3, True),     # 3 is prime
    (4, False),    # 4 = 2 × 2, not prime
    (5, True),     # 5 is prime
    (9, False),    # 9 = 3 × 3, not prime
    (13, True),    # 13 is prime
    (100, False),  # 100 is not prime
]

all_passed = True
for n, expected in prime_tests:
    result = is_prime(n)
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  is_prime({n}) = {result} (expected {expected}) [{status}]")

print("All tests passed!" if all_passed else "Some tests FAILED!")

print()

# ============================================================
# Test max_of_list()
# ============================================================
print("=== Testing max_of_list() ===")

list_tests = [
    ([3, 7, 1, 9, 5], 9),          # normal case
    ([5, 5, 5], 5),                  # all same
    ([42], 42),                      # single item
    ([-3, -1, -7], -1),             # all negative
    ([0, 0, 0], 0),                  # all zeros
    ([], None),                      # empty list
]

all_passed2 = True
for nums, expected in list_tests:
    result = max_of_list(nums)
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed2 = False
    print(f"  max_of_list({nums}) = {result} (expected {expected}) [{status}]")

print("All tests passed!" if all_passed2 else "Some tests FAILED!")
