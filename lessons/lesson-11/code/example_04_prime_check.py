# example_04_prime_check.py
# Lesson 11: Checking for prime numbers
# A prime number has exactly 2 divisors: 1 and itself.

# Check if a single number is prime
n = 17
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is prime")
else:
    print(n, "is NOT prime")

# Print all primes from 2 to 50
print("\n--- All primes from 2 to 50 ---")
for num in range(2, 51):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()

# Count primes from 2 to 100
print("\n--- Count of primes from 2 to 100 ---")
count = 0
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        count = count + 1
print("Number of primes:", count)
