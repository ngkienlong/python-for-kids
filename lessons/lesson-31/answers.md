# Lesson 31: Answers 🔢

---

## 🟢 Easy

**E1.**
```python
def area_square(s):
    return s * s

def area_rectangle(w, h):
    return w * h

def area_triangle(b, h):
    return 0.5 * b * h

print("Area of square (5):", area_square(5))
print("Area of rectangle (4, 6):", area_rectangle(4, 6))
print("Area of triangle (3, 8):", area_triangle(3, 8))
```

**E2.**
```python
def is_divisible(n, d):
    return n % d == 0

print("10 divisible by 2:", is_divisible(10, 2))
print("10 divisible by 3:", is_divisible(10, 3))
print("15 divisible by 5:", is_divisible(15, 5))
```

**E3.**
```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(1, 8):
    print(str(i) + "! =", factorial(i))
```

**E4.**
```python
def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

for i in range(11):
    print("2^" + str(i) + " =", power(2, i))
```

**E5.**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, 31):
    if is_prime(i):
        primes.append(str(i))
print(" ".join(primes))
```

**E6.**
```python
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print("digit_sum(123) =", digit_sum(123))
print("digit_sum(456) =", digit_sum(456))
print("digit_sum(9999) =", digit_sum(9999))
```

**E7.**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

for i in range(7):
    print(str(i) + "! =", factorial(i))
```

---

## 🟡 Medium

**M1.**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

a = float(input())
b = float(input())
op = input()

if op == "+":
    print(add(a, b))
elif op == "-":
    print(subtract(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
```

**M2.**
```python
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

a = int(input())
b = int(input())
print(gcd(a, b))
```

**M3.**
```python
def is_perfect(n):
    if n < 2:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

for i in range(1, 501):
    if is_perfect(i):
        print(i)
```

**M4.**
```python
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

n = int(input())
print(collatz_steps(n))
```

**M5.**
```python
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

for i in range(1, 11):
    print("fib(" + str(i) + ") =", fibonacci(i))
```

**M6.**
```python
def bmi(weight, height):
    return weight / (height * height)

def bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input())
height = float(input())
b = bmi(weight, height)
print("BMI:", round(b, 2))
print("Category:", bmi_category(b))
```

**M7.**
```python
def number_to_word(n):
    words = ["", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten"]
    if 1 <= n <= 10:
        return words[n]
    return "unknown"

count = int(input())
for i in range(count):
    num = int(input())
    print(number_to_word(num))
```

---

## 🔴 Hard

**H1.**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

op = input()
a = float(input())
b = float(input())

if op == "+":
    print(round(add(a, b), 2))
elif op == "-":
    print(round(subtract(a, b), 2))
elif op == "*":
    print(round(multiply(a, b), 2))
elif op == "/":
    result = divide(a, b)
    if result is None:
        print("Error: division by zero")
    else:
        print(round(result, 2))
```

**H2.**
```python
def is_perfect(n):
    if n < 2:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

for i in range(1, 1001):
    if is_perfect(i):
        print(i)
```
*Explanation: For each number, sum all its proper divisors (divisors less than itself). If the sum equals the number, it is perfect.*

**H3.**
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input())
b = int(input())
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
```
*Explanation: The Euclidean algorithm for GCD: repeatedly replace (a, b) with (b, a % b) until b is 0. LCM = a * b / GCD.*

**H4.**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

n = int(input())
print(nth_prime(n))
```
*Explanation: Count prime numbers until we reach the nth one. Start from 2 and check each number.*

**H5.**
```python
def collatz_length(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

n = int(input())
print(collatz_length(n))
```
*Explanation: Follow the Collatz rules (even: divide by 2, odd: multiply by 3 and add 1) and count steps until reaching 1.*

**H6.**
```python
def digit_reverse(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

count = int(input())
for i in range(count):
    num = int(input())
    print(digit_reverse(num))
```
*Explanation: Extract the last digit with `% 10`, build the reversed number by multiplying by 10 and adding the digit, then remove the last digit with `// 10`.*

**H7.**
```python
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

n = int(input())
for i in range(1, n + 1):
    if is_palindrome(i):
        print(i)
```
*Explanation: Convert the number to a string and check if it equals its reverse. `s[::-1]` is a Python shortcut to reverse a string.*
