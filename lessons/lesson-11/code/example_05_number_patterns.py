# example_05_number_patterns.py
# Lesson 11: Number patterns combining loops and conditions

# Print numbers that are both odd and divisible by 3 (from 1 to 50)
print("--- Odd multiples of 3 from 1 to 50 ---")
for i in range(1, 51):
    if i % 2 != 0 and i % 3 == 0:
        print(i, end=" ")
print()

# Digit sum pattern: print numbers from 1 to 50 whose digit sum is 5
print("\n--- Numbers from 1 to 50 with digit sum = 5 ---")
for n in range(1, 51):
    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum = digit_sum + temp % 10
        temp = temp // 10
    if digit_sum == 5:
        print(n, end=" ")
print()

# Goldbach: show pairs of primes that sum to 20
print("\n--- Prime pairs that sum to 20 ---")
target = 20
for p in range(2, target):
    # Check if p is prime
    p_is_prime = True
    for i in range(2, p):
        if p % i == 0:
            p_is_prime = False
            break
    if not p_is_prime:
        continue
    q = target - p
    if q < p:
        break
    # Check if q is prime
    q_is_prime = True
    for i in range(2, q):
        if q % i == 0:
            q_is_prime = False
            break
    if q_is_prime:
        print(p, "+", q, "=", target)
