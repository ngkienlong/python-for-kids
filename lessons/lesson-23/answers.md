# Lesson 23: Answers 🏆

---

## 🟢 Easy

**E1.**
```python
N = int(input())
print(N ** 2)
print(N ** 3)
print(2 ** N)
```

**E2.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
area = a * b / 2
print(f"Hypotenuse = {c:.4f}")
print(f"Area = {area:.4f}")
```

**E3.**
```python
import math
parts = input().split()
A = int(parts[0])
B = int(parts[1])
g = math.gcd(A, B)
l = A * B // g
print(f"GCD = {g}")
print(f"LCM = {l}")
```

**E4.**
```python
import math
a = 0
b = 1
for i in range(8):
    root = math.sqrt(a)
    if root == int(root):
        print(f"F({i}) = {a}  square")
    else:
        print(f"F({i}) = {a}")
    a, b = b, a + b
```

**E5.**
```python
import math
S = float(input())
sq_area = S ** 2
circle_area = math.pi * (S / 2) ** 2
print(f"Square area = {sq_area:.4f}")
print(f"Circle area = {circle_area:.4f}")
```

**E6.**
```python
parts = input().split()
P = float(parts[0])
R = float(parts[1])
Y = int(parts[2])
final = P * (1 + R / 100) ** Y
print(f"Final: {final:.2f}")
print(f"More than double: {final > 2 * P}")
```

**E7.**
```python
a = 3
d = 3
for i in range(15):
    term = a + i * d
    if term % 9 == 0:
        print(f"{term} (divisible by 9)")
    else:
        print(term)
```

---

## 🟡 Medium

**M1.**
```python
import math
parts = input().split()
N = int(parts[0])
W = float(parts[1])
H = float(parts[2])
total_width = N * W
total_height = N * H
handrail = math.sqrt(total_width ** 2 + total_height ** 2)
print(f"Handrail = {handrail:.4f} m")
```

**M2.**
```python
parts = input().split()
P = float(parts[0])
R = float(parts[1])
Y = int(parts[2])
balance = P
for year in range(1, Y + 1):
    balance = balance * (1 + R / 100)
    print(f"Year {year}: {balance:.2f}")
```

**M3.**
```python
import math
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a ** 2 + b ** 2 == c ** 2:
                if math.gcd(math.gcd(a, b), c) == 1:
                    print(f"({a}, {b}, {c})")
```

**M4.**
```python
import math
parts = input().split()
W = float(parts[0])
H = float(parts[1])
T = float(parts[2])
room_area = W * H
tile_area = T * T
tiles = math.ceil(room_area / tile_area)
leftover = tiles * tile_area - room_area
print(f"Tiles needed: {tiles}")
print(f"Leftover area: {leftover:.2f} m²")
```

**M5.**
```python
import math
N = int(input())
nums = list(map(int, input().split()))
result = nums[0]
for i in range(1, N):
    result = math.gcd(result, nums[i])
print(result)
```

**M6.**
```python
N = int(input())
total = 0.0
for k in range(1, N + 1):
    total += 1 / (k ** 2)
print(f"{total:.6f}")
```

**M7.**
```python
import math
N = int(input())
points = []
for i in range(N):
    parts = input().split()
    points.append((float(parts[0]), float(parts[1])))
total = 0.0
for i in range(N - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    total += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Total distance = {total:.4f}")
```

---

## 🔴 Hard

**H1.**

The handrail is the hypotenuse of a right triangle with legs N×W and N×H.

```python
import math
parts = input().split()
N = int(parts[0])
W = float(parts[1])
H = float(parts[2])
total_width = N * W
total_height = N * H
handrail = math.sqrt(total_width ** 2 + total_height ** 2)
print(f"Handrail = {handrail:.4f} m")
```

**H2.**

Multiply the balance by `(1 + R/100)` each year.

```python
parts = input().split()
P = float(parts[0])
R = float(parts[1])
Y = int(parts[2])
balance = P
for year in range(1, Y + 1):
    balance = balance * (1 + R / 100)
    print(f"Year {year}: {balance:.2f}")
```

**H3.**

Generate Fibonacci numbers and check each one for being a perfect square.

```python
import math

count = 0
a = 0
b = 1
while count < 5:
    root = math.sqrt(a)
    if root == int(root):
        print(a)
        count += 1
    a, b = b, a + b
```

**H4.**

Divide room area by tile area, use `ceil` for tiles, then compute leftover.

```python
import math
parts = input().split()
W = float(parts[0])
H = float(parts[1])
T = float(parts[2])
room_area = W * H
tile_area = T * T
tiles = math.ceil(room_area / tile_area)
leftover = tiles * tile_area - room_area
print(f"Tiles needed: {tiles}")
print(f"Leftover area: {leftover:.4f} m²")
```

**H5.**

Start with the first number as the running GCD, then apply `gcd(running, next)` for each remaining number.

```python
import math
N = int(input())
nums = list(map(int, input().split()))
result = nums[0]
for i in range(1, N):
    result = math.gcd(result, nums[i])
print(result)
```

**H6.**

Loop from k=1 to N and accumulate `1 / k**2`.

```python
N = int(input())
total = 0.0
for k in range(1, N + 1):
    total += 1 / (k ** 2)
print(f"{total:.6f}")
```

**H7.**

Read all waypoints, then sum the distances between consecutive pairs using the distance formula.

```python
import math
N = int(input())
points = []
for i in range(N):
    parts = input().split()
    points.append((float(parts[0]), float(parts[1])))
total = 0.0
for i in range(N - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    total += dist
print(f"Total distance = {total:.4f}")
```
