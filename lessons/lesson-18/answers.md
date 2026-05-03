# Lesson 18: Answers ⚡

---

## 🟢 Easy

**E1.**
```python
N = int(input())
print(f"N squared = {N ** 2}")
print(f"N cubed = {N ** 3}")
```

**E2.**
```python
for k in range(7):
    print(f"10^{k} = {10 ** k}")
```

**E3.**
```python
N = int(input())
print(f"{N}^0 = {N ** 0}")
```

**E4.**
```python
B = int(input())
print(f"{B}^-1 = {B ** -1}")
print(f"{B}^-2 = {B ** -2}")
print(f"{B}^-3 = {B ** -3}")
```

**E5.**
```python
line = input().split()
B = int(line[0])
E = int(line[1])
print(f"{B}^{E} = {pow(B, E)}")
```

**E6.**
```python
print(f"2^64 = {2 ** 64}")
```

**E7.**
```python
print(f"1e3 = {1e3}")
print(f"2.5e4 = {2.5e4}")
print(f"1e-2 = {1e-2}")
```

---

## 🟡 Medium

**M1.**
```python
N = int(input())
for k in range(N + 1):
    print(f"2^{k} = {2 ** k}")
```

**M2.**
```python
parts = input().split()
P = float(parts[0])
R = float(parts[1])
Y = int(parts[2])
simple = P + P * R / 100 * Y
compound = P * (1 + R / 100) ** Y
print(f"Simple: {simple:.2f}")
print(f"Compound: {compound:.2f}")
```

**M3.**
```python
S = int(input())
for i in range(9):
    print(S * (2 ** i))
```

**M4.**
```python
N = int(input())
total = 0
for i in range(1, N + 1):
    total += i ** 2
print(f"Sum = {total}")
```

**M5.**
```python
parts = input().split()
A = int(parts[0])
B = int(parts[1])
a_sq = A ** 2
b_cu = B ** 3
if a_sq > b_cu:
    print(f"A^2 = {a_sq}, B^3 = {b_cu}, A^2 is larger")
elif b_cu > a_sq:
    print(f"A^2 = {a_sq}, B^3 = {b_cu}, B^3 is larger")
else:
    print(f"A^2 = {a_sq}, B^3 = {b_cu}, equal")
```

**M6.**
```python
print(f"1 KB = {2 ** 10} bytes")
print(f"1 MB = {2 ** 20} bytes")
print(f"1 GB = {2 ** 30} bytes")
print(f"1 TB = {2 ** 40} bytes")
```

**M7.**
```python
parts = input().split()
N = int(parts[0])
H = int(parts[1])
for k in range(1, H + 1):
    print(f"Hour {k}: {N * (2 ** k)}")
```

---

## 🔴 Hard

**H1.**
```python
N = int(input())
for k in range(N + 1):
    print(2 ** k)
```

**H2.**
```python
parts = input().split()
P = float(parts[0])
R = float(parts[1])
Y = int(parts[2])
amount = P * (1 + R / 100) ** Y
print(f"Final amount: {amount:.2f}")
```

**H3.**

Count how many times we double 1 until we reach N.

```python
N = int(input())
count = 0
value = 1
while value < N:
    value = value * 2
    count += 1
print(count)
```

**H4.**

Use powers of 2 to convert binary digits to decimal.

```python
parts = input().split()
d3 = int(parts[0])
d2 = int(parts[1])
d1 = int(parts[2])
d0 = int(parts[3])
decimal = d3 * (2 ** 3) + d2 * (2 ** 2) + d1 * (2 ** 1) + d0 * (2 ** 0)
print(decimal)
```

**H5.**

Find the exponent using `math.floor(math.log10(N))`, then divide to get the coefficient.

```python
import math
N = float(input())
b = math.floor(math.log10(N))
a = N / (10 ** b)
print(f"{a:.2f} × 10^{b}")
```

**H6.**

Compute the inner exponent first, then the outer one.

```python
parts = input().split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])
result = a ** (b ** c)
print(result)
```

**H7.**

Use the formula: final = N × 2^H.

```python
parts = input().split()
N = int(parts[0])
H = int(parts[1])
final = N * (2 ** H)
print(final)
```
