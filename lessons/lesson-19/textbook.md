# Lesson 19: Square Root and the math Module 📐

> **Goal:** Import and use the `math` module to calculate square roots, round numbers, and use mathematical constants like π and e.

---

## 1. Importing the math Module

Python's `math` module gives you many useful math functions. You must import it first.

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
```

After `import math`, you access functions with `math.function_name()`.

---

## 2. Square Root: `math.sqrt()`

`math.sqrt(x)` returns the square root of x as a float.

```python
import math

print(math.sqrt(9))     # 3.0
print(math.sqrt(25))    # 5.0
print(math.sqrt(2))     # 1.4142135623730951
print(math.sqrt(100))   # 10.0
```

> ⚠️ `math.sqrt()` always returns a **float**, even if the answer is a whole number.

---

## 3. Perfect Squares

A **perfect square** is a number whose square root is a whole number (1, 4, 9, 16, 25, ...).

```python
import math

n = 36
root = math.sqrt(n)

# Check if root is a whole number
if root == int(root):
    print(f"{n} is a perfect square (sqrt = {int(root)})")
else:
    print(f"{n} is NOT a perfect square (sqrt ≈ {root:.4f})")
```

---

## 4. Floor and Ceiling

- `math.floor(x)` — round **down** to the nearest integer.
- `math.ceil(x)` — round **up** to the nearest integer.

```python
import math

print(math.floor(3.7))   # 3  (round down)
print(math.floor(3.2))   # 3  (round down)
print(math.floor(-3.2))  # -4 (round down, toward negative infinity)

print(math.ceil(3.2))    # 4  (round up)
print(math.ceil(3.9))    # 4  (round up)
print(math.ceil(-3.7))   # -3 (round up, toward positive infinity)
```

| Function | 3.2 | 3.7 | -3.2 | -3.7 |
|----------|-----|-----|------|------|
| `floor` | 3 | 3 | -4 | -4 |
| `ceil` | 4 | 4 | -3 | -3 |
| `round` | 3 | 4 | -3 | -4 |

---

## 5. The `round()` Function

`round(x, n)` rounds x to n decimal places.

```python
print(round(3.14159, 2))    # 3.14
print(round(2.71828, 3))    # 2.718
print(round(7.5))           # 8  (rounds to nearest even in Python 3)
print(round(6.5))           # 6  (rounds to nearest even in Python 3)
```

---

## 6. Math Constants

```python
import math

print(math.pi)      # 3.141592653589793  (π)
print(math.e)       # 2.718281828459045  (Euler's number)
print(math.tau)     # 6.283185307179586  (τ = 2π)
print(math.inf)     # inf  (infinity)
```

---

## 7. Circle Calculations

Using `math.pi` for circle area and circumference.

```python
import math

radius = 5

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Radius: {radius}")
print(f"Area: {area:.4f}")
print(f"Circumference: {circumference:.4f}")
```

Output:
```
Radius: 5
Area: 78.5398
Circumference: 31.4159
```

---

## 8. Logarithm

`math.log(x)` = natural logarithm (base e).
`math.log(x, base)` = logarithm with any base.
`math.log10(x)` = logarithm base 10.

```python
import math

print(math.log10(100))      # 2.0  (10^2 = 100)
print(math.log10(1000))     # 3.0  (10^3 = 1000)
print(math.log(math.e))     # 1.0  (e^1 = e)

# Number of digits in N = floor(log10(N)) + 1
N = 12345
digits = math.floor(math.log10(N)) + 1
print(f"{N} has {digits} digits")   # 5 digits
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| square root | căn bậc hai | The number that, when squared, gives the original |
| perfect square | số chính phương | A number whose square root is a whole number |
| floor | làm tròn xuống | Round down to the nearest integer |
| ceiling | làm tròn lên | Round up to the nearest integer |
| round | làm tròn | Round to the nearest value |
| module | mô-đun | A collection of related functions you can import |
| constant | hằng số | A value that never changes (like π) |
| pi | số pi | The ratio of a circle's circumference to its diameter (≈ 3.14159) |
| euler | số Euler | The base of natural logarithm (≈ 2.71828) |
| logarithm | lô-ga-rít | The inverse of exponentiation |
| approximation | xấp xỉ | A value close to but not exactly the true value |
| irrational | vô tỉ | A number that cannot be written as a simple fraction |

---

## 10. Summary

✅ `import math` loads the math module.
✅ `math.sqrt(x)` returns the square root of x (as a float).
✅ `math.floor(x)` rounds down; `math.ceil(x)` rounds up.
✅ `round(x, n)` rounds to n decimal places.
✅ `math.pi` ≈ 3.14159; `math.e` ≈ 2.71828.
✅ Check perfect square: `math.sqrt(n) == int(math.sqrt(n))`.
✅ `math.log10(n)` gives the base-10 logarithm.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Square Root**

Read a number N and print its square root rounded to 4 decimal places.

- **Input:** One positive integer N (1 ≤ N ≤ 10000).
- **Output:** One line: `sqrt(N) = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 16 | sqrt(16) = 4.0000 |
| 7 | sqrt(7) = 2.6458 |

---

**Exercise E2. Floor and Ceiling**

Read a decimal number X and print its floor and ceiling.

- **Input:** One float X.
- **Output:** Two lines: `floor = ...` and `ceil = ...`.

**Example:**

| Input | Output |
|-------|--------|
| 3.7 | floor = 3 |
| | ceil = 4 |

---

**Exercise E3. Pi and Circle**

Read a radius R and print the area of the circle using `math.pi`. Round to 2 decimal places.

- **Input:** One float R (0 < R ≤ 100).
- **Output:** One line: `Area = X.XX`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Area = 78.54 |

---

**Exercise E4. Round to Decimal Places**

Read a float X and print it rounded to 0, 1, 2, and 3 decimal places.

- **Input:** One float X.
- **Output:** Four lines.

**Example:**

| Input | Output |
|-------|--------|
| 3.14159 | 3 |
| | 3.1 |
| | 3.14 |
| | 3.142 |

---

**Exercise E5. Perfect Square Check (Easy)**

Read N and print "yes" if N is a perfect square, "no" otherwise.

- **Input:** One positive integer N (1 ≤ N ≤ 10000).
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 25 | yes |
| 26 | no |

---

**Exercise E6. Log Base 10**

Read N and print `math.log10(N)` rounded to 4 decimal places.

- **Input:** One positive integer N (1 ≤ N ≤ 100000).
- **Output:** One line: `log10(N) = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 100 | log10(100) = 2.0000 |
| 50 | log10(50) = 1.6990 |

---

**Exercise E7. Euler's Number**

Print the value of `math.e` rounded to 5 decimal places, and print `math.e ** 2` rounded to 4 decimal places.

- **Input:** None.
- **Output:** Two lines.

**Example:**
```
e = 2.71828
e^2 = 7.3891
```

---

### 🟡 Medium

---

**Exercise M1. Square Roots Table**

Print a table of square roots for numbers 1 through 10.

- **Input:** None.
- **Output:** 10 lines, each showing `sqrt(k) = X.XXXX`.

**Example:**
```
sqrt(1) = 1.0000
sqrt(2) = 1.4142
...
sqrt(10) = 3.1623
```

---

**Exercise M2. Circle Area and Circumference**

Read radius R and print both the area and circumference of the circle.

- **Input:** One float R.
- **Output:** Two lines, each rounded to 4 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 7 | Area = 153.9380 |
| | Circumference = 43.9823 |

---

**Exercise M3. Tiles Needed**

A room has area A square meters. Each tile covers T square meters. How many tiles are needed? (Always round up — you can't use half a tile.)

- **Input:** Two floats A and T on one line.
- **Output:** One integer — the number of tiles needed.

**Example:**

| Input | Output |
|-------|--------|
| 20 3 | 7 |
| 10 2.5 | 4 |

---

**Exercise M4. Count Perfect Squares**

Read N and print all perfect squares from 1 to N.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** All perfect squares ≤ N, separated by spaces.

**Example:**

| Input | Output |
|-------|--------|
| 30 | 1 4 9 16 25 |

---

**Exercise M5. Sphere Volume**

Read radius R and print the volume of a sphere: V = (4/3) × π × r³. Round to 4 decimal places.

- **Input:** One float R.
- **Output:** One line: `Volume = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 | Volume = 113.0973 |

---

**Exercise M6. Number of Digits**

Read N and print how many digits it has using `math.floor(math.log10(N)) + 1`.

- **Input:** One positive integer N (1 ≤ N ≤ 10^9).
- **Output:** One integer — the number of digits.

**Example:**

| Input | Output |
|-------|--------|
| 12345 | 5 |
| 7 | 1 |
| 1000 | 4 |

---

**Exercise M7. Hypotenuse Preview**

Read two legs a and b of a right triangle. Print the hypotenuse c = sqrt(a² + b²) rounded to 4 decimal places.

- **Input:** Two floats a and b on one line.
- **Output:** One line: `c = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | c = 5.0000 |
| 5 12 | c = 13.0000 |

---

### 🔴 Hard

---

**Exercise H1. Perfect Square Check**

*Check if a number is a perfect square.*

Read N. Print `yes` if N is a perfect square, `no` otherwise.

- **Input:** One positive integer N (1 ≤ N ≤ 10^9).
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 144 | yes |
| 145 | no |
| 1000000 | yes |

---

**Exercise H2. Circle Area and Circumference**

*Calculate both properties of a circle.*

Read radius R. Print the area and circumference, each rounded to 4 decimal places.

- **Input:** One float R (0 < R ≤ 1000).
- **Output:** Two lines.

**Example:**

| Input | Output |
|-------|--------|
| 10 | Area = 314.1593 |
| | Circumference = 62.8319 |

---

**Exercise H3. Distance Between Two Points**

*Use the distance formula.*

Read x1, y1, x2, y2 on one line. Print the distance between the two points, rounded to 4 decimal places.

Distance = sqrt((x2-x1)² + (y2-y1)²)

- **Input:** Four floats on one line: x1 y1 x2 y2.
- **Output:** One line: `Distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 0 0 3 4 | Distance = 5.0000 |
| 1 1 4 5 | Distance = 5.0000 |

---

**Exercise H4. Hypotenuse**

*Find the hypotenuse of a right triangle.*

Read legs a and b. Print c = sqrt(a² + b²) rounded to 4 decimal places.

- **Input:** Two floats a and b on one line.
- **Output:** One line: `c = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | c = 5.0000 |
| 8 15 | c = 17.0000 |

---

**Exercise H5. Sphere Volume**

*Calculate the volume of a sphere.*

Read radius R. Print V = (4/3) × π × R³, rounded to 4 decimal places.

- **Input:** One float R (0 < R ≤ 100).
- **Output:** One line: `Volume = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Volume = 523.5988 |
| 1 | Volume = 4.1888 |

---

**Exercise H6. How Many Tiles**

*Calculate tiles needed to cover a room.*

A room has area A square meters. Each tile is a square with side T meters. How many tiles are needed? (Use `math.ceil` — you can't cut tiles.)

- **Input:** Two floats A and T on one line.
- **Output:** One integer — the number of tiles needed.

**Example:**

| Input | Output |
|-------|--------|
| 20 1.5 | 9 |
| 100 3 | 12 |

*Explanation: 20 / (1.5 × 1.5) = 20 / 2.25 ≈ 8.89 → ceil = 9.*

---

**Exercise H7. Logarithm Application**

*Count the digits of a number using logarithm.*

Read N. Print how many digits N has. Use the formula: `floor(log10(N)) + 1`.

- **Input:** One positive integer N (1 ≤ N ≤ 10^15).
- **Output:** One integer — the number of digits.

**Example:**

| Input | Output |
|-------|--------|
| 1 | 1 |
| 99 | 2 |
| 1000 | 4 |
| 123456789 | 9 |
