# Lesson 22: Answers 🔢

---

## 🟢 Easy

**E1.**
```python
a = 1
d = 3
for i in range(5):
    print(a + i * d)
```

**E2.**
```python
term = 2
for i in range(6):
    print(term)
    term = term * 2
```

**E3.**
```python
a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b
```

**E4.**
```python
for n in range(1, 7):
    print(n * (n + 1) // 2)
```

**E5.**
```python
for n in range(1, 9):
    print(n ** 2)
```

**E6.**
```python
a = 2
d = 3
total = 0
for i in range(5):
    total += a + i * d
print(f"Sum = {total}")
```

**E7.**
```python
a = 0
b = 1
found = False
while a <= 13:
    if a == 13:
        found = True
        break
    a, b = b, a + b
if found:
    print("13 is a Fibonacci number")
else:
    print("13 is not a Fibonacci number")
```

---

## 🟡 Medium

**M1.**
```python
parts = input().split()
a = int(parts[0])
d = int(parts[1])
n = int(parts[2])
for i in range(n):
    print(a + i * d)
```

**M2.**
```python
parts = input().split()
a = int(parts[0])
r = int(parts[1])
n = int(parts[2])
term = a
for i in range(n):
    print(term)
    term = term * r
```

**M3.**
```python
N = int(input())
a = 0
b = 1
while a <= N:
    print(a)
    a, b = b, a + b
```

**M4.**
```python
parts = input().split()
a = int(parts[0])
d = int(parts[1])
n = int(parts[2])
total = 0
for i in range(n):
    total += a + i * d
print(total)
```

**M5.**
```python
import math
N = int(input())
# T(k) = k*(k+1)/2 = N → k^2 + k - 2N = 0
# k = (-1 + sqrt(1 + 8N)) / 2
k = (-1 + math.sqrt(1 + 8 * N)) / 2
if k == int(k):
    print("yes")
else:
    print("no")
```

**M6.**
```python
N = int(input())
a = 0
b = 1
for i in range(N):
    a, b = b, a + b
# After N iterations, a holds F(N)
# But we need to reset and redo
a = 0
b = 1
for i in range(N):
    a, b = b, a + b
print(a)
```

**M7.**
```python
N = int(input())
total = 0
for n in range(1, N + 1):
    total += n * (n + 1) // 2
print(total)
```

---

## 🔴 Hard

**H1.**
```python
parts = input().split()
a = int(parts[0])
d = int(parts[1])
n = int(parts[2])
for i in range(n):
    print(a + i * d)
```

**H2.**
```python
parts = input().split()
a = int(parts[0])
r = int(parts[1])
n = int(parts[2])
term = a
for i in range(n):
    print(term)
    term = term * r
```

**H3.**

Generate Fibonacci numbers one by one until reaching the Nth one.

```python
N = int(input())
a = 0
b = 1
for i in range(N):
    a, b = b, a + b
print(a)
```

**H4.**

Generate Fibonacci numbers and add them while they are ≤ N.

```python
N = int(input())
a = 0
b = 1
total = 0
while a <= N:
    total += a
    a, b = b, a + b
print(total)
```

**H5.**

Check if `(target - a)` is divisible by d, and if the result is non-negative.

```python
parts = input().split()
a = int(parts[0])
d = int(parts[1])
t = int(parts[2])
diff = t - a
if d != 0 and diff % d == 0 and diff // d >= 0:
    term_number = diff // d + 1
    print(f"Term {term_number}")
else:
    print("not in sequence")
```

**H6.**

Multiply each term by r and accumulate the sum.

```python
parts = input().split()
a = int(parts[0])
r = float(parts[1])
n = int(parts[2])
total = 0.0
term = float(a)
for i in range(n):
    total += term
    term = term * r
print(f"{total:.4f}")
```

**H7.**

Check if all consecutive differences are equal (arithmetic) or all consecutive ratios are equal (geometric).

```python
parts = input().split()
nums = [float(x) for x in parts]

# Check arithmetic: all differences equal
diffs = [nums[i+1] - nums[i] for i in range(4)]
if all(abs(d - diffs[0]) < 0.0001 for d in diffs):
    print("arithmetic")
else:
    # Check geometric: all ratios equal (and no zeros)
    if all(nums[i] != 0 for i in range(4)):
        ratios = [nums[i+1] / nums[i] for i in range(4)]
        if all(abs(r - ratios[0]) < 0.0001 for r in ratios):
            print("geometric")
        else:
            print("neither")
    else:
        print("neither")
```
