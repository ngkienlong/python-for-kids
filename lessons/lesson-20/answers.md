# Lesson 20: Answers 📐

---

## 🟢 Easy

**E1.**
```python
import math
a = 3
b = 4
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c:.4f}")
```

**E2.**
```python
a, b, c = 3, 4, 5
if a ** 2 + b ** 2 == c ** 2:
    print("yes")
else:
    print("no")
```

**E3.**
```python
import math
S = float(input())
diagonal = math.sqrt(S ** 2 + S ** 2)
print(f"Diagonal = {diagonal:.4f}")
```

**E4.**
```python
import math
parts = input().split()
x = float(parts[0])
y = float(parts[1])
dist = math.sqrt(x ** 2 + y ** 2)
print(f"Distance = {dist:.4f}")
```

**E5.**
```python
triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
for (a, b, c) in triples:
    print(f"{a}^2 + {b}^2 = {c}^2 → {a**2} + {b**2} = {c**2} ✓")
```

**E6.**
```python
import math
c = 10
a = 6
b = math.sqrt(c ** 2 - a ** 2)
print(f"b = {b:.4f}")
```

**E7.**
```python
import math
parts = input().split()
W = float(parts[0])
H = float(parts[1])
diagonal = math.sqrt(W ** 2 + H ** 2)
print(f"Diagonal = {diagonal:.4f}")
```

---

## 🟡 Medium

**M1.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c:.4f}")
```

**M2.**
```python
import math
parts = input().split()
c = float(parts[0])
a = float(parts[1])
b = math.sqrt(c ** 2 - a ** 2)
print(f"b = {b:.4f}")
```

**M3.**
```python
parts = input().split()
sides = sorted([float(x) for x in parts])
a, b, c = sides[0], sides[1], sides[2]
if abs(a ** 2 + b ** 2 - c ** 2) < 0.0001:
    print("right triangle")
else:
    print("not a right triangle")
```

**M4.**
```python
import math
parts = input().split()
x1, y1, x2, y2 = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = {dist:.4f}")
```

**M5.**
```python
for a in range(1, 16):
    for b in range(a, 16):
        for c in range(b, 16):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"({a}, {b}, {c})")
```

**M6.**
```python
import math
parts = input().split()
H = float(parts[0])
D = float(parts[1])
length = math.sqrt(H ** 2 + D ** 2)
print(f"Ladder length = {length:.4f}")
```

**M7.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c
print(f"Perimeter = {perimeter:.4f}")
```

---

## 🔴 Hard

**H1.**
```python
import math
parts = input().split()
a = float(parts[0])
b = float(parts[1])
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c:.4f}")
```

**H2.**
```python
import math
parts = input().split()
c = float(parts[0])
a = float(parts[1])
b = math.sqrt(c ** 2 - a ** 2)
print(f"b = {b:.4f}")
```

**H3.**

Sort the sides first so c is the largest, then check a² + b² == c².

```python
parts = input().split()
sides = sorted([float(x) for x in parts])
a, b, c = sides[0], sides[1], sides[2]
if abs(a ** 2 + b ** 2 - c ** 2) < 0.0001:
    print("right triangle")
else:
    print("not a right triangle")
```

**H4.**
```python
import math
parts = input().split()
x1, y1, x2, y2 = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = {dist:.4f}")
```

**H5.**
```python
import math
parts = input().split()
W = float(parts[0])
H = float(parts[1])
diagonal = math.sqrt(W ** 2 + H ** 2)
print(f"Diagonal = {diagonal:.4f}")
```

**H6.**

Use three nested loops to check all combinations where a ≤ b ≤ c ≤ N.

```python
N = int(input())
for a in range(1, N + 1):
    for b in range(a, N + 1):
        for c in range(b, N + 1):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"({a}, {b}, {c})")
```

**H7.**

The ladder is the hypotenuse of a right triangle with legs H and D.

```python
import math
parts = input().split()
H = float(parts[0])
D = float(parts[1])
length = math.sqrt(H ** 2 + D ** 2)
print(f"Ladder length = {length:.4f}")
```
