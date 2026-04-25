"""
Lesson 23 - Example 02: Number Theory
GCD, LCM, prime check, and perfect numbers combined
"""
import math

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Check if a number is perfect
def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# GCD and LCM
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Print primes up to 50
print("--- Primes up to 50 ---")
primes = [n for n in range(2, 51) if is_prime(n)]
print(primes)

# Print perfect numbers up to 1000
print("\n--- Perfect Numbers up to 1000 ---")
for n in range(1, 1001):
    if is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        print(f"{n} = {' + '.join(str(d) for d in divisors)}")

# GCD and LCM of user input
print("\n--- GCD and LCM ---")
parts = input("Enter two numbers: ").split()
a = int(parts[0])
b = int(parts[1])
g = gcd(a, b)
l = lcm(a, b)
print(f"GCD({a}, {b}) = {g}")
print(f"LCM({a}, {b}) = {l}")
print(f"GCD × LCM = {g * l}  (should equal {a} × {b} = {a * b})")
