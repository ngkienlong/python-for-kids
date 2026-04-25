# Lesson 10: Nested Loops 🔲

> **Goal:** Use a loop inside another loop to print grids, tables, and patterns.

---

## 1. What is a Nested Loop?

A **nested loop** is a loop inside another loop. The outer loop runs first, and for each step of the outer loop, the inner loop runs completely.

> 💡 Think of it like a clock: the minute hand (inner loop) goes all the way around before the hour hand (outer loop) moves one step.

---

## 2. Basic Nested Loop

```python
for i in range(3):          # outer loop: runs 3 times
    for j in range(4):      # inner loop: runs 4 times for EACH i
        print("*", end="")  # end="" stays on the same line
    print()                 # print() moves to the next line
```

**Output:**
```
****
****
****
```

- The outer loop runs 3 times (i = 0, 1, 2).
- For each value of i, the inner loop runs 4 times (j = 0, 1, 2, 3).
- Total: 3 × 4 = **12** iterations.

> ⚠️ Use **different variable names** for outer and inner loops. `i` for outer, `j` for inner is the convention.

---

## 3. `print()` Tricks

| Code | Effect |
|------|--------|
| `print("*")` | Print `*` and move to next line |
| `print("*", end="")` | Print `*` and stay on the same line |
| `print()` | Print an empty line (move to next line) |

---

## 4. Multiplication Table

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")   # \t is a tab character
    print()
```

**Output:**
```
1	2	3	
2	4	6	
3	6	9	
```

---

## 5. Rectangle Pattern

```python
rows = 3
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

**Output:**
```
*****
*****
*****
```

---

## 6. Triangle Pattern

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

**Output:**
```
*
**
***
****
*****
```

The inner loop runs `i` times — so row 1 has 1 star, row 2 has 2 stars, etc.

---

## 7. Number Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end="  ")
    print()
```

**Output:**
```
1 1  1 2  1 3  
2 1  2 2  2 3  
3 1  3 2  3 3  
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| nested | lồng nhau | One thing inside another |
| outer loop | vòng lặp ngoài | The loop that contains another loop |
| inner loop | vòng lặp trong | The loop that is inside another loop |
| row | hàng | A horizontal line in a grid |
| column | cột | A vertical line in a grid |
| pattern | mẫu hình | A repeated design or arrangement |
| grid | lưới | A rectangular arrangement of rows and columns |
| combination | tổ hợp | A pairing of values from two loops |
| matrix | ma trận | A grid of numbers |

---

## 9. Summary

✅ A nested loop is a loop inside another loop.
✅ Use `i` for the outer loop variable and `j` for the inner loop variable.
✅ Outer loop runs N times, inner loop runs M times → N × M total iterations.
✅ `print("*", end="")` stays on the same line.
✅ `print()` with no arguments moves to the next line.
✅ The inner loop variable can control how many characters to print per row.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Rectangle of Stars**

Print a rectangle of stars with 3 rows and 6 columns.

- **Input:** None.
- **Output:**
```
******
******
******
```

---

**Exercise E2. Number Grid**

Print a 3×3 grid where each cell shows the row number (1-3).

- **Input:** None.
- **Output:**
```
1 1 1
2 2 2
3 3 3
```

---

**Exercise E3. Right Triangle**

Print a right triangle of stars with 5 rows.

- **Input:** None.
- **Output:**
```
*
**
***
****
*****
```

---

**Exercise E4. Multiplication Table (3×3)**

Print a 3×3 multiplication table.

- **Input:** None.
- **Output:**
```
1 2 3
2 4 6
3 6 9
```

---

**Exercise E5. Count Pairs**

Print all pairs (i, j) where i goes from 1 to 3 and j goes from 1 to 3.

- **Input:** None.
- **Output:**
```
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

**Exercise E6. Reverse Triangle**

Print a reverse triangle of stars with 4 rows.

- **Input:** None.
- **Output:**
```
****
***
**
*
```

---

**Exercise E7. Square Numbers Grid**

Print a 4×4 grid where each cell shows i × j.

- **Input:** None.
- **Output:**
```
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
```

---

### 🟡 Medium

---

**Exercise M1. Full Multiplication Table (5×5)**

Print a 5×5 multiplication table with aligned columns.

- **Input:** None.
- **Output:**
```
1  2  3  4  5
2  4  6  8  10
3  6  9  12 15
4  8  12 16 20
5  10 15 20 25
```

---

**Exercise M2. Hollow Rectangle**

Print a 4×6 rectangle where only the border is `*` and the inside is spaces.

- **Input:** None.
- **Output:**
```
******
*    *
*    *
******
```

---

**Exercise M3. Number Triangle**

Print a triangle where row i contains the numbers 1 through i.

- **Input:** None.
- **Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

**Exercise M4. Diagonal Pattern**

Print a 5×5 grid where the cell is `*` if i == j (the diagonal), otherwise `.`.

- **Input:** None.
- **Output:**
```
*....
.*...
..*..
...*. 
....*
```

---

**Exercise M5. Sum of Each Row**

For a 4×4 multiplication table, print the sum of each row.

- **Input:** None.
- **Output:**
```
Row 1 sum: 10
Row 2 sum: 20
Row 3 sum: 30
Row 4 sum: 40
```

---

**Exercise M6. Staircase**

Print a staircase pattern with 5 steps using `#`.

- **Input:** None.
- **Output:**
```
#
##
###
####
#####
```

---

**Exercise M7. Checkerboard**

Print a 4×4 checkerboard pattern using `#` and `.`.

- **Input:** None.
- **Output:**
```
#.#.
.#.#
#.#.
.#.#
```

---

### 🔴 Hard

---

**Exercise H1. Full Multiplication Table**

Print the full 10×10 multiplication table, with each number taking 4 spaces (right-aligned).

- **Input:** None.
- **Output:** A 10×10 grid where row i, column j shows i × j, each number right-aligned in 4 spaces.

**Example (first 3 rows):**
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
```

---

**Exercise H2. Right Triangle of Stars**

Read N. Print a right triangle where row i has i stars (i from 1 to N).

- **Input:** One integer N (1 ≤ N ≤ 20).
- **Output:** N rows of stars.

**Example:**

| Input | Output |
|-------|--------|
| 4 | * |
| | ** |
| | *** |
| | **** |

---

**Exercise H3. Hollow Rectangle**

Read N (rows) and M (columns). Print a hollow rectangle — only the border is `*`, inside is spaces.

- **Input:** Two integers N and M (2 ≤ N, M ≤ 20).
- **Output:** An N×M hollow rectangle.

**Example:**

| Input | Output |
|-------|--------|
| 4 6 | ****** |
| | *    * |
| | *    * |
| | ****** |

---

**Exercise H4. Count Even Pairs**

Read N. Count how many pairs (i, j) with 1 ≤ i < j ≤ N have an even sum (i + j is even).

- **Input:** One integer N (2 ≤ N ≤ 100).
- **Output:** One integer — the count of pairs where i + j is even.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 4 |
| 5 | 6 |

**Explanation:** For N=4, pairs with even sum: (1,3), (2,4), (1,3) wait — pairs are (1,3), (2,4), (3,1)... Let's list: (1,3)=4✓, (2,4)=6✓, (1,3) already counted. Valid pairs (i<j): (1,3), (2,4), (3,5)... For N=4: (1,3)=4✓, (2,4)=6✓, (1,1) not valid since i<j. Also (2,2) not valid. So: (1,3), (2,4) = 2? Actually for N=4: (1,3)✓, (2,4)✓, (1,1)✗, (3,1)✗ since i<j. Hmm — (1,3), (2,4), (3,5)✗ out of range. Wait also (1,1)✗. Let me recount: pairs (i,j) with i<j≤4: (1,2)=3✗, (1,3)=4✓, (1,4)=5✗, (2,3)=5✗, (2,4)=6✓, (3,4)=7✗ → 2 pairs. But example says 4. Let me use N=4 → answer 4 means i+j even includes (1,3),(2,4),(3,1)... no, i<j. Re-examine: maybe the answer for N=4 is 2 and N=5 is 4. Use those values.

**Corrected Example:**

| Input | Output |
|-------|--------|
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |

---

**Exercise H5. Diamond Pattern**

Read an odd number N. Print a diamond of stars with N rows (widest at the middle).

- **Input:** One odd integer N (1 ≤ N ≤ 11).
- **Output:** A diamond pattern.

**Example:**

| Input | Output |
|-------|--------|
| 5 | &nbsp;&nbsp;* |
| | &nbsp;*** |
| | ***** |
| | &nbsp;*** |
| | &nbsp;&nbsp;* |

---

**Exercise H6. Sum of Multiplication Table**

Read N. Calculate the sum of all values in the N×N multiplication table (sum of i×j for all i,j from 1 to N).

- **Input:** One integer N (1 ≤ N ≤ 100).
- **Output:** One integer — the total sum.

**Example:**

| Input | Output |
|-------|--------|
| 2 | 9 |
| 3 | 36 |
| 4 | 100 |

**Explanation:** For N=2: 1×1 + 1×2 + 2×1 + 2×2 = 1+2+2+4 = 9.

---

**Exercise H7. Pascal's Triangle**

Print the first N rows of Pascal's triangle. Each number is the sum of the two numbers above it. Row 1 is just `1`.

- **Input:** One integer N (1 ≤ N ≤ 10).
- **Output:** N rows of Pascal's triangle numbers.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1 |
| | 1 1 |
| | 1 2 1 |
| | 1 3 3 1 |
| | 1 4 6 4 1 |
