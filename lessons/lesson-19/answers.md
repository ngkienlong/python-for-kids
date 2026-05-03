# Lesson 19: Answers 📐

---

## 🟢 Easy

**E1.**
```python
import math
N = int(input())
print(f"sqrt({N}) = {math.sqrt(N):.4f}")
```

**E2.**
```python
import math
X = float(input())
print(f"floor = {math.floor(X)}")
print(f"ceil = {math.ceil(X)}")
```

**E3.**
```python
import math
R = float(input())
area = math.pi * R ** 2
print(f"Area = {area:.2f}")
```

**E4.**
```python
X = float(input())
print(round(X, 0))
print(round(X, 1))
print(round(X, 2))
print(round(X, 3))
```

**E5.**
```python
import math
N = int(input())
root = math.sqrt(N)
if root == int(root):
    print("yes")
else:
    print("no")
```

**E6.**
```python
import math
N = int(input())
print(f"log10({N}) = {math.log10(N):.4f}")
```

**E7.**
```python
import math
print(f"e = {math.e:.5f}")
print(f"e^2 = {math.e ** 2:.4f}")
```

---

## 🟡 Medium

**M1.**
```python
import math
for k in range(1, 11):
    print(f"sqrt({k}) = {math.sqrt(k):.4f}")
```

**M2.**
```python
import math
R = float(input())
area = math.pi * R ** 2
circ = 2 * math.pi * R
print(f"Area = {area:.4f}")
print(f"Circumference = {circ:.4f}")
```

**M3.**
```python
import math
parts = input().split()
A = float(parts[0])
T = float(parts[1])
tiles = math.ceil(A / T)
print(tiles)
```

**M4.**
```python
import math
N = int(input())
result = []
for k in range(1, N + 1):
    root = math.sqrt(k)
    if root == int(root):
        result.append(k)
print(" ".join(str(x) for x in result))
```

**M5.**
```python
import math
R = float(input())
volume = (4 / 3) * math.pi * R ** 3
print(f"Volume = {volume:.4f}")
```

**M6.**
```python
import math
N = int(input())
digits = math.floor(math.log10(N)) + 1
print(digits)
```

**M7.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c:.4f}")
```

---

## 🔴 Hard

**H1.**

Use `math.isqrt()` for integer square root, or check if `sqrt(N) == int(sqrt(N))`.

```python
import math
N = int(input())
root = math.sqrt(N)
if root == int(root):
    print("yes")
else:
    print("no")
```

**H2.**
```python
import math
R = float(input())
area = math.pi * R ** 2
circ = 2 * math.pi * R
print(f"Area = {area:.4f}")
print(f"Circumference = {circ:.4f}")
```

**H3.**

Apply the distance formula: sqrt((x2-x1)² + (y2-y1)²).

```python
import math
parts = input().split()
x1, y1, x2, y2 = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = {dist:.4f}")
```

**H4.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c:.4f}")
```

**H5.**
```python
import math
R = float(input())
volume = (4 / 3) * math.pi * R ** 3
print(f"Volume = {volume:.4f}")
```

**H6.**

Each tile covers T×T area. Divide room area by tile area, then use `ceil`.

```python
import math
parts = input().split()
A = float(parts[0])
T = float(parts[1])
tile_area = T * T
tiles = math.ceil(A / tile_area)
print(tiles)
```

**H7.**

Use `math.floor(math.log10(N)) + 1` to count digits.

```python
import math
N = int(input())
digits = math.floor(math.log10(N)) + 1
print(digits)
```
