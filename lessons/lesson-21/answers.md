# Lesson 21: Answers 🔢

---

## 🟢 Easy

**E1.**
```python
N = int(input())
if N % 2 == 0:
    print("even")
else:
    print("odd")
```

**E2.**
```python
N = int(input())
if N % 3 == 0:
    print("yes")
else:
    print("no")
```

**E3.**
```python
parts = input().split()
A = int(parts[0])
B = int(parts[1])
print(A % B)
```

**E4.**
```python
N = int(input())
count = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        count += 1
print(count)
```

**E5.**
```python
N = int(input())
if N % 3 == 0 and N % 5 == 0:
    print("yes")
else:
    print("no")
```

**E6.**
```python
N = int(input())
total = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        total += i
print(total)
```

**E7.**
```python
N = int(input())
print(N % 10)
```

---

## 🟡 Medium

**M1.**
```python
parts = input().split()
a = int(parts[0])
b = int(parts[1])
while b != 0:
    a, b = b, a % b
print(a)
```

**M2.**
```python
import math
parts = input().split()
a = int(parts[0])
b = int(parts[1])
print(a * b // math.gcd(a, b))
```

**M3.**
```python
N = int(input())
divisors = []
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)
print(" ".join(str(x) for x in divisors))
```

**M4.**
```python
import math
parts = input().split()
p = int(parts[0])
q = int(parts[1])
g = math.gcd(p, q)
print(f"{p // g}/{q // g}")
```

**M5.**
```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**M6.**
```python
parts = input().split()
N = int(parts[0])
K = int(parts[1])
total = 0
for i in range(K, N + 1, K):
    total += i
print(total)
```

**M7.**
```python
N = int(input())
count = 0
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
print(count)
```

---

## 🔴 Hard

**H1.**

Implement the Euclidean algorithm manually.

```python
parts = input().split()
a = int(parts[0])
b = int(parts[1])
while b != 0:
    a, b = b, a % b
print(a)
```

**H2.**

Use the formula LCM = a × b ÷ GCD.

```python
parts = input().split()
a = int(parts[0])
b = int(parts[1])
# Find GCD first
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
print(a * b // gcd)
```

**H3.**

Loop from 1 to N and print each divisor on its own line.

```python
N = int(input())
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
```

**H4.**

Sum all proper divisors (1 to N-1) and compare to N.

```python
N = int(input())
total = 0
for i in range(1, N):
    if N % i == 0:
        total += i
if total == N:
    print("perfect")
else:
    print("not perfect")
```

**H5.**

Find GCD and check if it equals 1.

```python
parts = input().split()
a = int(parts[0])
b = int(parts[1])
x, y = a, b
while y != 0:
    x, y = y, x % y
if x == 1:
    print("coprime")
else:
    print("not coprime")
```

**H6.**

Use `range(K, N+1, K)` to iterate over multiples of K.

```python
parts = input().split()
N = int(parts[0])
K = int(parts[1])
total = 0
for i in range(K, N + 1, K):
    total += i
print(total)
```

**H7.**

Divide both numerator and denominator by their GCD.

```python
parts = input().split()
p = int(parts[0])
q = int(parts[1])
# Find GCD
a, b = p, q
while b != 0:
    a, b = b, a % b
gcd = a
print(f"{p // gcd}/{q // gcd}")
```
