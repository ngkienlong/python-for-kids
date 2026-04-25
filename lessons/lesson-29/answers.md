# Lesson 29: Answers 📤

---

## 🟢 Easy

**E1.**
```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
greet("Charlie")
```

**E2.**
```python
def square(n):
    return n * n

print(square(3))
print(square(5))
print(square(7))
```

**E3.**
```python
def add(a, b):
    return a + b

a = int(input())
b = int(input())
print(add(a, b))
```

**E4.**
```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))
print(is_even(10))
```

**E5.**
```python
def area(width, height):
    return width * height

w = int(input())
h = int(input())
print(area(w, h))
```

**E6.**
```python
def greet(name="friend"):
    print("Hello, " + name + "!")

greet("Alice")
greet()
```

**E7.**
```python
def my_abs(n):
    if n < 0:
        return -n
    return n

print(my_abs(-5))
print(my_abs(3))
print(my_abs(-8))
```

---

## 🟡 Medium

**M1.**
```python
def max_two(a, b):
    if a > b:
        return a
    return b

a = int(input())
b = int(input())
print(max_two(a, b))
```

**M2.**
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

temp = float(input())
print(celsius_to_fahrenheit(temp))
```

**M3.**
```python
def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

base = int(input())
exp = int(input())
print(power(base, exp))
```

**M4.**
```python
def classify(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

n = int(input())
for i in range(n):
    num = int(input())
    print(classify(num))
```

**M5.**
```python
def area_circle(r):
    return 3.14159 * r * r

def perimeter_circle(r):
    return 2 * 3.14159 * r

r = float(input())
print("Area:", round(area_circle(r), 2))
print("Perimeter:", round(perimeter_circle(r), 2))
```

**M6.**
```python
def repeat(text, times):
    return text * times

text = input()
times = int(input())
print(repeat(text, times))
```

**M7.**
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

n = int(input())
for i in range(n):
    score = int(input())
    print(get_grade(score))
```

---

## 🔴 Hard

**H1.**
```python
def add(a, b):
    return a + b

a = int(input())
b = int(input())
print(add(a, b))
```

**H2.**
```python
def is_even(n):
    return n % 2 == 0

n = int(input())
for i in range(n):
    num = int(input())
    if is_even(num):
        print(num)
```

**H3.**
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temp = float(input())
direction = input()

if direction == "C":
    print(round(celsius_to_fahrenheit(temp), 2))
else:
    print(round(fahrenheit_to_celsius(temp), 2))
```
*Explanation: Read the temperature and direction. Call the appropriate conversion function based on the direction.*

**H4.**
```python
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input())
b = int(input())
c = int(input())
print(max_of_three(a, b, c))
```

**H5.**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
```
*Explanation: A number is prime if no number from 2 to n-1 divides it evenly. The function returns False as soon as it finds a divisor.*

**H6.**
```python
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10   # get last digit
        n = n // 10       # remove last digit
    return total

count = int(input())
for i in range(count):
    num = int(input())
    print(digit_sum(num))
```
*Explanation: Use `% 10` to get the last digit and `// 10` to remove it. Repeat until n becomes 0.*

**H7.**
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input())
for i in range(n + 1):
    print(fibonacci(i))
```
*Explanation: The function calculates the nth Fibonacci number using a loop. fib(0)=0, fib(1)=1, and each subsequent number is the sum of the two before it.*
