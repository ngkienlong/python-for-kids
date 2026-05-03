# Lesson 20: The Pythagorean Theorem 📐

> **Goal:** Use the Pythagorean theorem (a² + b² = c²) to find hypotenuses, check right triangles, calculate distances, and solve real-world problems.

---

## 1. The Pythagorean Theorem

In a right triangle:
- **a** and **b** are the two **legs** (the shorter sides).
- **c** is the **hypotenuse** (the longest side, opposite the right angle).

The theorem states: **a² + b² = c²**

```
        /|
       / |
   c  /  | b
     /   |
    /    |
   /_____|
       a
```

---

## 2. Finding the Hypotenuse

Given legs a and b, find c:

```python
import math

a = 3
b = 4
c = math.sqrt(a ** 2 + b ** 2)
print(f"c = {c}")   # c = 5.0
```

The famous **3-4-5 triangle**: 3² + 4² = 9 + 16 = 25 = 5².

---

## 3. Finding a Missing Leg

Given hypotenuse c and one leg a, find the other leg b:

b² = c² - a²  →  b = sqrt(c² - a²)

```python
import math

c = 13
a = 5
b = math.sqrt(c ** 2 - a ** 2)
print(f"b = {b}")   # b = 12.0
```

---

## 4. Checking if a Triangle is a Right Triangle

Given three sides a, b, c (where c is the largest), check if a² + b² = c².

```python
import math

a = 3
b = 4
c = 5

# Sort so c is the largest
sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]

if a ** 2 + b ** 2 == c ** 2:
    print("Right triangle!")
else:
    print("Not a right triangle.")
```

> ⚠️ For floating-point numbers, use `abs(a**2 + b**2 - c**2) < 0.0001` instead of `==`.

---

## 5. Pythagorean Triples

A **Pythagorean triple** is a set of three whole numbers (a, b, c) where a² + b² = c².

Famous triples:
| a | b | c |
|---|---|---|
| 3 | 4 | 5 |
| 5 | 12 | 13 |
| 8 | 15 | 17 |
| 7 | 24 | 25 |

```python
# Find all Pythagorean triples up to 20
for a in range(1, 21):
    for b in range(a, 21):
        for c in range(b, 21):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"({a}, {b}, {c})")
```

---

## 6. Distance Between Two Points

The distance formula is the Pythagorean theorem applied to coordinates.

Distance = sqrt((x2 - x1)² + (y2 - y1)²)

```python
import math

x1, y1 = 1, 2
x2, y2 = 4, 6

dx = x2 - x1    # horizontal distance = 3
dy = y2 - y1    # vertical distance = 4

distance = math.sqrt(dx ** 2 + dy ** 2)
print(f"Distance = {distance}")   # 5.0
```

---

## 7. Diagonal of a Rectangle

The diagonal of a rectangle with width w and height h is:

d = sqrt(w² + h²)

```python
import math

width = 6
height = 8
diagonal = math.sqrt(width ** 2 + height ** 2)
print(f"Diagonal = {diagonal}")   # 10.0
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| hypotenuse | cạnh huyền | The longest side of a right triangle |
| leg | cạnh góc vuông | One of the two shorter sides of a right triangle |
| right angle | góc vuông | A 90-degree angle |
| Pythagorean theorem | định lý Pythagoras | a² + b² = c² for right triangles |
| triple | bộ ba | A set of three numbers (a, b, c) satisfying a² + b² = c² |
| diagonal | đường chéo | A line connecting opposite corners of a rectangle |
| distance | khoảng cách | How far apart two points are |
| proof | chứng minh | A logical argument showing something is true |
| theorem | định lý | A mathematical statement that has been proven |
| perpendicular | vuông góc | At a 90-degree angle to something |

---

## 9. Summary

✅ Pythagorean theorem: a² + b² = c².
✅ Find hypotenuse: `c = math.sqrt(a**2 + b**2)`.
✅ Find missing leg: `b = math.sqrt(c**2 - a**2)`.
✅ Check right triangle: `a**2 + b**2 == c**2` (sort sides first).
✅ Distance formula: `d = math.sqrt((x2-x1)**2 + (y2-y1)**2)`.
✅ Diagonal of rectangle: `d = math.sqrt(w**2 + h**2)`.
✅ Famous triples: (3,4,5), (5,12,13), (8,15,17).

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Hypotenuse (3-4-5)**

Calculate the hypotenuse of a right triangle with legs a=3 and b=4.

- **Input:** None (hardcode a=3, b=4).
- **Output:** One line: `c = 5.0000`.

---

**Exercise E2. Check 3-4-5**

Check if (3, 4, 5) is a Pythagorean triple. Print "yes" or "no".

- **Input:** None.
- **Output:** `yes`

---

**Exercise E3. Diagonal of a Square**

Read the side length S of a square. Print the diagonal length.

- **Input:** One float S.
- **Output:** One line: `Diagonal = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Diagonal = 7.0711 |

---

**Exercise E4. Distance from Origin**

Read x and y. Print the distance from the origin (0, 0) to the point (x, y).

- **Input:** Two floats x and y on one line.
- **Output:** One line: `Distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | Distance = 5.0000 |

---

**Exercise E5. Famous Triples**

Print all three famous Pythagorean triples: (3,4,5), (5,12,13), (8,15,17). For each, verify that a²+b²=c².

- **Input:** None.
- **Output:** Three lines, each showing the triple and the verification.

**Example:**
```
3^2 + 4^2 = 5^2 → 9 + 16 = 25 ✓
```

---

**Exercise E6. Missing Leg**

Read hypotenuse c=10 and leg a=6. Find the other leg b.

- **Input:** None (hardcode c=10, a=6).
- **Output:** One line: `b = X.XXXX`.

---

**Exercise E7. Diagonal of Rectangle**

Read width W and height H of a rectangle. Print the diagonal length.

- **Input:** Two floats W and H on one line.
- **Output:** One line: `Diagonal = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 6 8 | Diagonal = 10.0000 |

---

### 🟡 Medium

---

**Exercise M1. Find Hypotenuse**

Read legs a and b. Print the hypotenuse c rounded to 4 decimal places.

- **Input:** Two floats a and b on one line.
- **Output:** One line: `c = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 5 12 | c = 13.0000 |

---

**Exercise M2. Find Missing Leg**

Read hypotenuse c and one leg a. Print the other leg b.

- **Input:** Two floats c and a on one line.
- **Output:** One line: `b = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 13 5 | b = 12.0000 |

---

**Exercise M3. Check Right Triangle**

Read three sides a, b, c. Print "right triangle" or "not a right triangle".

- **Input:** Three floats on one line.
- **Output:** One line.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 5 | right triangle |
| 3 4 6 | not a right triangle |

---

**Exercise M4. Distance Between Two Points**

Read x1, y1, x2, y2. Print the distance between the two points.

- **Input:** Four floats on one line.
- **Output:** One line: `Distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 0 0 3 4 | Distance = 5.0000 |

---

**Exercise M5. Pythagorean Triples up to 15**

Print all Pythagorean triples (a, b, c) where a ≤ b ≤ c ≤ 15.

- **Input:** None.
- **Output:** All triples, one per line.

**Example:**
```
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
...
```

---

**Exercise M6. Ladder Problem**

A ladder leans against a wall. Read the wall height H and the distance from the wall D. Print the minimum ladder length needed.

- **Input:** Two floats H and D on one line.
- **Output:** One line: `Ladder length = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 4 3 | Ladder length = 5.0000 |

---

**Exercise M7. Perimeter of Right Triangle**

Read legs a and b. Print the perimeter (a + b + c) of the right triangle.

- **Input:** Two floats a and b on one line.
- **Output:** One line: `Perimeter = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | Perimeter = 12.0000 |

---

### 🔴 Hard

---

**Exercise H1. Find Hypotenuse**

*Calculate the hypotenuse of a right triangle.*

Read legs a and b. Print c = sqrt(a² + b²) rounded to 4 decimal places.

- **Input:** Two floats a and b on one line (0 < a, b ≤ 1000).
- **Output:** One line: `c = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | c = 5.0000 |
| 7 24 | c = 25.0000 |

---

**Exercise H2. Find Missing Leg**

*Find the unknown leg of a right triangle.*

Read hypotenuse c and one leg a. Print b = sqrt(c² - a²) rounded to 4 decimal places.

- **Input:** Two floats c and a on one line (a < c).
- **Output:** One line: `b = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 10 6 | b = 8.0000 |
| 25 7 | b = 24.0000 |

---

**Exercise H3. Check Right Triangle**

*Determine if three sides form a right triangle.*

Read three sides a, b, c. Sort them so c is the largest. Check if a² + b² = c².

- **Input:** Three floats on one line.
- **Output:** `right triangle` or `not a right triangle`.

**Example:**

| Input | Output |
|-------|--------|
| 5 13 12 | right triangle |
| 4 5 6 | not a right triangle |

---

**Exercise H4. Distance Between Two Points**

*Calculate the distance between two points on a grid.*

Read x1, y1, x2, y2. Print the distance rounded to 4 decimal places.

- **Input:** Four floats on one line.
- **Output:** One line: `Distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 1 1 4 5 | Distance = 5.0000 |
| 0 0 1 1 | Distance = 1.4142 |

---

**Exercise H5. Diagonal of a Rectangle**

*Find the diagonal of a rectangle.*

Read width W and height H. Print the diagonal length rounded to 4 decimal places.

- **Input:** Two floats W and H on one line.
- **Output:** One line: `Diagonal = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 9 12 | Diagonal = 15.0000 |
| 1 1 | Diagonal = 1.4142 |

---

**Exercise H6. Pythagorean Triples up to N**

*Find all Pythagorean triples within a range.*

Read N. Print all triples (a, b, c) where a ≤ b ≤ c ≤ N and a² + b² = c².

- **Input:** One integer N (5 ≤ N ≤ 100).
- **Output:** All triples, one per line in format `(a, b, c)`.

**Example:**

| Input | Output |
|-------|--------|
| 15 | (3, 4, 5) |
| | (5, 12, 13) |
| | (6, 8, 10) |
| | (9, 12, 15) |

---

**Exercise H7. Ladder Problem**

*Find the minimum ladder length.*

A ladder leans against a wall. The wall is H meters tall. The base of the ladder is D meters from the wall. Find the minimum ladder length needed.

- **Input:** Two floats H and D on one line.
- **Output:** One line: `Ladder length = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 4 3 | Ladder length = 5.0000 |
| 12 5 | Ladder length = 13.0000 |
