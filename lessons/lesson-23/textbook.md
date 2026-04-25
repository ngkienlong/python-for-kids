# Lesson 23: Math Challenge Round 🏆

> **Goal:** Combine all Module 5 skills — exponents, square roots, Pythagorean theorem, divisibility, and sequences — to solve multi-step real-world problems.

---

## 1. Review: Module 5 Skills

Here is a quick summary of everything you have learned in Module 5.

| Lesson | Topic | Key Tool |
|--------|-------|---------|
| 18 | Exponents | `**`, `pow()` |
| 19 | Square Root | `math.sqrt()`, `math.floor()`, `math.ceil()` |
| 20 | Pythagorean Theorem | `c = math.sqrt(a**2 + b**2)` |
| 21 | Divisibility | `%`, GCD, LCM |
| 22 | Sequences | loops, Fibonacci, arithmetic, geometric |

---

## 2. Problem Decomposition

Complex problems are easier when you break them into steps.

**Example:** "A square room has area 50 m². How long is the diagonal?"

Step 1: Find the side length → `side = math.sqrt(50)`
Step 2: Find the diagonal → `diagonal = math.sqrt(side**2 + side**2)`

Or more directly: `diagonal = math.sqrt(2 * 50) = math.sqrt(100) = 10`

```python
import math

area = 50
side = math.sqrt(area)
diagonal = math.sqrt(side ** 2 + side ** 2)
print(f"Side: {side:.4f}")
print(f"Diagonal: {diagonal:.4f}")
```

---

## 3. Combining Exponents and Sequences

```python
# Print the first 10 powers of 2 and check if each is a perfect square
import math

for i in range(10):
    value = 2 ** i
    root = math.sqrt(value)
    is_perfect = (root == int(root))
    print(f"2^{i} = {value:5d}  perfect square: {is_perfect}")
```

---

## 4. Combining GCD and Sequences

```python
import math

# Find GCD of consecutive Fibonacci numbers
a = 0
b = 1
print("GCD of consecutive Fibonacci pairs:")
for i in range(8):
    g = math.gcd(a, b) if a > 0 else b
    print(f"GCD({a}, {b}) = {g}")
    a, b = b, a + b
```

---

## 5. Combining Pythagorean Theorem and Sequences

```python
import math

# Staircase: N steps, each 1m wide and 0.2m tall
# Find the length of the handrail (hypotenuse of the staircase triangle)
N = 10
step_width = 1.0
step_height = 0.2

total_width = N * step_width
total_height = N * step_height
handrail = math.sqrt(total_width ** 2 + total_height ** 2)

print(f"Steps: {N}")
print(f"Total width: {total_width} m")
print(f"Total height: {total_height} m")
print(f"Handrail length: {handrail:.4f} m")
```

---

## 6. Verify Your Answer

Always check your answer using a different method.

```python
import math

# Find hypotenuse two ways
a = 3
b = 4

# Method 1: Pythagorean theorem
c1 = math.sqrt(a ** 2 + b ** 2)

# Method 2: pow()
c2 = pow(a ** 2 + b ** 2, 0.5)

print(f"Method 1: {c1}")
print(f"Method 2: {c2}")
print(f"Same? {abs(c1 - c2) < 0.0001}")
```

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| review | ôn tập | Go over material you have already learned |
| challenge | thử thách | A harder problem that tests your skills |
| decompose | phân tách | Break a complex problem into smaller steps |
| verify | kiểm tra | Check that your answer is correct |
| intermediate | trung gian | A value calculated on the way to the final answer |
| combine | kết hợp | Use multiple skills together |
| strategy | chiến lược | A plan for solving a problem |
| approach | cách tiếp cận | The method you choose to solve a problem |

---

## 8. Summary

✅ Break complex problems into small steps.
✅ Store intermediate results in variables.
✅ Combine `**`, `math.sqrt()`, `%`, GCD, and loops.
✅ Verify your answer using a different method.
✅ Use `f-strings` to format output clearly.
✅ Comment your code to explain each step.

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Combined Powers**

Read N. Print N², N³, and 2ᴺ on three separate lines.

- **Input:** One integer N (1 ≤ N ≤ 15).
- **Output:** Three lines.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 16 |
| | 64 |
| | 16 |

---

**Exercise E2. Hypotenuse and Area**

Read legs a and b of a right triangle. Print the hypotenuse and the area (= a × b / 2).

- **Input:** Two floats a and b on one line.
- **Output:** Two lines, each rounded to 4 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | Hypotenuse = 5.0000 |
| | Area = 6.0000 |

---

**Exercise E3. GCD and LCM Together**

Read two integers A and B. Print both their GCD and LCM.

- **Input:** Two integers on one line.
- **Output:** Two lines.

**Example:**

| Input | Output |
|-------|--------|
| 12 18 | GCD = 6 |
| | LCM = 36 |

---

**Exercise E4. Fibonacci and Squares**

Print the first 8 Fibonacci numbers and mark which ones are perfect squares.

- **Input:** None.
- **Output:** 8 lines, each showing the Fibonacci number and "square" or "".

**Example:**
```
F(0) = 0  square
F(1) = 1  square
F(2) = 1  square
F(3) = 2
...
```

---

**Exercise E5. Circle and Square**

Read a side length S. Print the area of the square (S²) and the area of the circle that fits inside it (radius = S/2).

- **Input:** One float S.
- **Output:** Two lines, rounded to 4 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 10 | Square area = 100.0000 |
| | Circle area = 78.5398 |

---

**Exercise E6. Compound Interest Check**

Read P, R%, and Y. Print the final amount and whether it is more than double the original.

- **Input:** Three values: P (float), R (float), Y (int).
- **Output:** Two lines.

**Example:**

| Input | Output |
|-------|--------|
| 1000 10 8 | Final: 2143.59 |
| | More than double: True |

---

**Exercise E7. Sequence and Divisibility**

Print the first 15 terms of the arithmetic sequence starting at 3 with difference 3. Mark each term that is also divisible by 9.

- **Input:** None.
- **Output:** 15 lines.

**Example:**
```
3
6
9 (divisible by 9)
12
...
```

---

### 🟡 Medium

---

**Exercise M1. Staircase Handrail**

Read N (number of steps), W (step width in m), H (step height in m). Print the handrail length.

- **Input:** Three values on one line: N (int), W (float), H (float).
- **Output:** One line: `Handrail = X.XXXX m`.

**Example:**

| Input | Output |
|-------|--------|
| 10 1 0.2 | Handrail = 10.1980 m |

---

**Exercise M2. Year-by-Year Savings**

Read P, R%, and Y. Print the balance at the end of each year.

- **Input:** Three values: P (float), R (float), Y (int).
- **Output:** Y lines, each showing `Year k: X.XX`.

**Example:**

| Input | Output |
|-------|--------|
| 1000 10 3 | Year 1: 1100.00 |
| | Year 2: 1210.00 |
| | Year 3: 1331.00 |

---

**Exercise M3. Pythagorean Triples and GCD**

Print all Pythagorean triples (a, b, c) up to 30 where GCD(a, b, c) = 1 (primitive triples).

- **Input:** None.
- **Output:** All primitive triples, one per line.

---

**Exercise M4. Tile a Floor**

Read room width W, room height H, and tile size T. Print the number of tiles needed and the leftover area.

- **Input:** Three floats on one line: W H T.
- **Output:** Two lines.

**Example:**

| Input | Output |
|-------|--------|
| 5 4 1.5 | Tiles needed: 9 |
| | Leftover area: 2.75 m² |

---

**Exercise M5. Chain of GCDs**

Read N numbers. Print the GCD of all of them.

- **Input:** First line: N. Second line: N integers.
- **Output:** One integer — the GCD of all N numbers.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 6 |
| 12 18 24 30 | |

---

**Exercise M6. Sum of 1/k²**

Read N. Print the sum of 1/1² + 1/2² + 1/3² + ... + 1/N², rounded to 6 decimal places.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One float.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1.463611 |
| 100 | 1.634984 |

---

**Exercise M7. Distance Traveled**

Read N waypoints as x, y pairs. Print the total distance traveled from the first to the last waypoint.

- **Input:** First line: N. Then N lines, each with x and y.
- **Output:** One float: `Total distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 3 | Total distance = 10.0000 |
| 0 0 | |
| 3 4 | |
| 9 4 | |

---

### 🔴 Hard

---

**Exercise H1. Spiral Staircase**

*Find the handrail length of a spiral staircase.*

A staircase has N steps. Each step is W meters wide and H meters tall. The handrail runs along the hypotenuse of the entire staircase (from bottom-left to top-right corner).

- **Input:** Three values on one line: N (int), W (float), H (float).
- **Output:** One line: `Handrail = X.XXXX m`.

**Example:**

| Input | Output |
|-------|--------|
| 20 1 0.2 | Handrail = 20.3961 m |
| 10 0.5 0.3 | Handrail = 5.8310 m |

*Explanation: total_width = N×W, total_height = N×H, handrail = sqrt(total_width² + total_height²).*

---

**Exercise H2. Savings with Interest**

*Track savings year by year.*

Read principal P, annual rate R (%), and years Y. Print the balance at the end of each year, rounded to 2 decimal places.

- **Input:** Three values on one line: P (float), R (float), Y (int).
- **Output:** Y lines, each showing `Year k: X.XX`.

**Example:**

| Input | Output |
|-------|--------|
| 500 8 4 | Year 1: 540.00 |
| | Year 2: 583.20 |
| | Year 3: 629.86 |
| | Year 4: 680.24 |

---

**Exercise H3. Perfect Square Fibonacci**

*Find Fibonacci numbers that are also perfect squares.*

Find the first 5 Fibonacci numbers (starting from F(0)=0) that are also perfect squares.

- **Input:** None.
- **Output:** 5 lines, each showing the Fibonacci number.

**Example:**
```
0
1
1
144
...
```

*(Note: The 5th perfect-square Fibonacci is very large — just find the first 5.)*

---

**Exercise H4. Tile a Floor**

*Calculate tiles needed and leftover area.*

A room is W meters wide and H meters tall. Tiles are squares with side T meters. How many tiles are needed (always round up)? What is the leftover area (tiles × T² − room area)?

- **Input:** Three floats on one line: W H T.
- **Output:** Two lines: tiles needed and leftover area (rounded to 4 decimal places).

**Example:**

| Input | Output |
|-------|--------|
| 5 4 1.5 | Tiles needed: 9 |
| | Leftover area: 0.2500 m² |

*Explanation: room area = 20 m², tile area = 2.25 m², tiles = ceil(20/2.25) = 9, leftover = 9×2.25 − 20 = 0.25.*

---

**Exercise H5. Chain of GCDs**

*Find the GCD of a list of numbers.*

Read N, then N integers. Print the GCD of all N numbers.

- **Input:** First line: N (2 ≤ N ≤ 20). Second line: N integers.
- **Output:** One integer — the GCD of all numbers.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 6 |
| 12 18 24 30 | |
| 3 | 1 |
| 7 11 13 | |

---

**Exercise H6. Sequence Sum Formula**

*Compute the sum of 1/k² for k from 1 to N.*

Read N. Print the sum 1/1² + 1/2² + 1/3² + ... + 1/N², rounded to 6 decimal places.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** One float.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 1.549768 |
| 1000 | 1.643935 |

*(The exact limit as N→∞ is π²/6 ≈ 1.644934.)*

---

**Exercise H7. Distance Traveled**

*Calculate total distance along a path.*

Read N waypoints. Print the total distance traveled from the first waypoint to the last, following the path in order.

- **Input:** First line: N (2 ≤ N ≤ 100). Then N lines, each with two floats x and y.
- **Output:** One line: `Total distance = X.XXXX`.

**Example:**

| Input | Output |
|-------|--------|
| 4 | Total distance = 15.0000 |
| 0 0 | |
| 3 4 | |
| 3 4 | |
| 9 4 | |

*Explanation: (0,0)→(3,4) = 5, (3,4)→(3,4) = 0, (3,4)→(9,4) = 6. Wait — (3,4)→(9,4) = 6, but (0,0)→(3,4) = 5, so total = 5+0+6 = 11. Adjust example: (0,0)→(3,4)=5, (3,4)→(9,4)=6, (9,4)→(9,16)=12. Total = 23. Use simpler example: 3 points: (0,0), (3,4), (9,4) → 5+6=11.*

| Input | Output |
|-------|--------|
| 3 | Total distance = 11.0000 |
| 0 0 | |
| 3 4 | |
| 9 4 | |
