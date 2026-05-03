# example_03_is_prime_function.py
# Lesson 31: is_prime() function and its uses

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False   # found a divisor, not prime
    return True            # no divisors found, it's prime

# Test the function
print("Testing is_prime():")
for n in [1, 2, 3, 4, 5, 10, 13, 17, 20, 23]:
    print(n, "->", is_prime(n))

print()

# Print all primes up to 50
print("Primes up to 50:")
primes = []
for i in range(2, 51):
    if is_prime(i):
        primes.append(i)
print(primes)

print()

# Count primes up to N
n = 100
count = 0
for i in range(2, n + 1):
    if is_prime(i):
        count += 1
print("Number of primes up to", n, ":", count)

print()

# Find the first 10 primes
print("First 10 primes:")
found = 0
num = 2
while found < 10:
    if is_prime(num):
        print(num, end=" ")
        found += 1
    num += 1
print()
