# Lesson 22: Number Patterns and Sequences 🔢

> **Goal:** Generate and analyze arithmetic sequences, geometric sequences, Fibonacci numbers, triangular numbers, and square numbers using loops.

---

## 1. Arithmetic Sequences

An **arithmetic sequence** adds the same number (the **common difference** d) each time.

Example: 3, 7, 11, 15, 19, ... (d = 4)

```python
# Arithmetic sequence: first term a=3, difference d=4, 6 terms
a = 3
d = 4
n = 6

for i in range(n):
    term = a + i * d
    print(term)
```

Output: 3, 7, 11, 15, 19, 23

The **k-th term** (0-indexed): `term = a + k * d`

---

## 2. Geometric Sequences

A **geometric sequence** multiplies by the same number (the **common ratio** r) each time.

Example: 2, 6, 18, 54, 162, ... (r = 3)

```python
# Geometric sequence: first term a=2, ratio r=3, 5 terms
a = 2
r = 3
n = 5

term = a
for i in range(n):
    print(term)
    term = term * r
```

Output: 2, 6, 18, 54, 162

---

## 3. Fibonacci Sequence

The **Fibonacci sequence** starts with 0 and 1. Each term is the sum of the two previous terms.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

```python
# Print first 10 Fibonacci numbers
a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b
```

The key step: `a, b = b, a + b` — both values update at the same time.

---

## 4. Triangular Numbers

**Triangular numbers** are: 1, 3, 6, 10, 15, 21, ...

The n-th triangular number = 1 + 2 + 3 + ... + n = `n * (n + 1) // 2`

```python
# Print first 8 triangular numbers
for n in range(1, 9):
    tri = n * (n + 1) // 2
    print(f"T({n}) = {tri}")
```

Output:
```
T(1) = 1
T(2) = 3
T(3) = 6
T(4) = 10
...
```

---

## 5. Square Numbers

**Square numbers** are: 1, 4, 9, 16, 25, 36, ...

The n-th square number = n²

```python
# Print first 10 square numbers
for n in range(1, 11):
    print(f"{n}^2 = {n ** 2}")
```

---

## 6. Sum of a Sequence

Use a loop to accumulate the sum.

```python
# Sum of first 10 Fibonacci numbers
a = 0
b = 1
total = 0
for i in range(10):
    total += a
    a, b = b, a + b
print(f"Sum = {total}")   # 88
```

---

## 7. Finding a Term in a Sequence

To find which term number a value is in an arithmetic sequence:

If `target = a + k * d`, then `k = (target - a) / d`.

```python
a = 3       # first term
d = 4       # common difference
target = 19

if (target - a) % d == 0:
    k = (target - a) // d
    print(f"{target} is term number {k + 1}")   # 1-indexed
else:
    print(f"{target} is not in the sequence")
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| sequence | dãy số | An ordered list of numbers following a pattern |
| arithmetic | cộng sai | A sequence where you add the same number each time |
| geometric | nhân sai | A sequence where you multiply by the same number each time |
| Fibonacci | Fibonacci | A sequence where each term = sum of the two previous terms |
| triangular | số tam giác | Numbers that form a triangle: 1, 3, 6, 10, ... |
| square number | số chính phương | Numbers that are perfect squares: 1, 4, 9, 16, ... |
| term | số hạng | One number in a sequence |
| common difference | công sai | The fixed amount added in an arithmetic sequence |
| common ratio | công bội | The fixed multiplier in a geometric sequence |
| pattern | quy luật | A rule that describes how a sequence grows |
| series | chuỗi tổng | The sum of the terms of a sequence |
| sum | tổng | The result of adding numbers together |

---

## 9. Summary

✅ Arithmetic: `term = a + k * d` (add d each step).
✅ Geometric: `term = a * r^k` (multiply by r each step).
✅ Fibonacci: `a, b = b, a + b` (each term = sum of previous two).
✅ Triangular: `T(n) = n * (n + 1) // 2`.
✅ Square: `S(n) = n ** 2`.
✅ Use a loop to generate any sequence.
✅ Use an accumulator variable to sum a sequence.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Arithmetic Sequence**

Print the first 5 terms of the arithmetic sequence starting at 1 with difference 3.

- **Input:** None.
- **Output:** 5 lines: 1, 4, 7, 10, 13.

---

**Exercise E2. Geometric Sequence**

Print the first 6 terms of the geometric sequence starting at 2 with ratio 2.

- **Input:** None.
- **Output:** 6 lines: 2, 4, 8, 16, 32, 64.

---

**Exercise E3. First 10 Fibonacci Numbers**

Print the first 10 Fibonacci numbers (starting from 0).

- **Input:** None.
- **Output:** 10 lines: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

---

**Exercise E4. Triangular Numbers**

Print the first 6 triangular numbers.

- **Input:** None.
- **Output:** 6 lines: 1, 3, 6, 10, 15, 21.

---

**Exercise E5. Square Numbers**

Print the first 8 square numbers.

- **Input:** None.
- **Output:** 8 lines: 1, 4, 9, 16, 25, 36, 49, 64.

---

**Exercise E6. Sum of First 5 Terms**

Print the sum of the first 5 terms of the arithmetic sequence: 2, 5, 8, 11, 14.

- **Input:** None.
- **Output:** One line: `Sum = 40`.

---

**Exercise E7. Fibonacci Check**

Print whether 13 is a Fibonacci number. (Hint: generate Fibonacci numbers until you reach or pass 13.)

- **Input:** None.
- **Output:** `13 is a Fibonacci number` or `13 is not a Fibonacci number`.

---

### 🟡 Medium

---

**Exercise M1. Arithmetic Sequence (User Input)**

Read first term a, difference d, and count n. Print n terms of the arithmetic sequence.

- **Input:** Three integers a, d, n on one line.
- **Output:** n lines, one term per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 3 4 | 5 |
| | 8 |
| | 11 |
| | 14 |

---

**Exercise M2. Geometric Sequence (User Input)**

Read first term a, ratio r, and count n. Print n terms of the geometric sequence.

- **Input:** Three integers a, r, n on one line.
- **Output:** n lines, one term per line.

**Example:**

| Input | Output |
|-------|--------|
| 3 2 5 | 3 |
| | 6 |
| | 12 |
| | 24 |
| | 48 |

---

**Exercise M3. Fibonacci up to N**

Read N. Print all Fibonacci numbers that are ≤ N.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** All Fibonacci numbers ≤ N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 20 | 0 |
| | 1 |
| | 1 |
| | 2 |
| | 3 |
| | 5 |
| | 8 |
| | 13 |

---

**Exercise M4. Sum of Arithmetic Sequence**

Read a, d, n. Print the sum of the first n terms.

- **Input:** Three integers a, d, n on one line.
- **Output:** One integer — the sum.

**Example:**

| Input | Output |
|-------|--------|
| 1 2 5 | 25 |

*Explanation: 1 + 3 + 5 + 7 + 9 = 25.*

---

**Exercise M5. Is it Triangular?**

Read N. Print "yes" if N is a triangular number, "no" otherwise.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 10 | yes |
| 11 | no |

---

**Exercise M6. Nth Fibonacci**

Read N (0-indexed). Print the Nth Fibonacci number.

- **Input:** One integer N (0 ≤ N ≤ 30).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 0 | 0 |
| 6 | 8 |
| 10 | 55 |

---

**Exercise M7. Sequence Sum**

Read N. Print the sum of the first N triangular numbers.

- **Input:** One integer N (1 ≤ N ≤ 100).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 20 |

*Explanation: T(1)+T(2)+T(3)+T(4) = 1+3+6+10 = 20.*

---

### 🔴 Hard

---

**Exercise H1. Print Arithmetic Sequence**

*Generate an arithmetic sequence.*

Read first term a, common difference d, and count n. Print n terms of the arithmetic sequence, one per line.

- **Input:** Three integers on one line: a d n (1 ≤ n ≤ 50).
- **Output:** n lines.

**Example:**

| Input | Output |
|-------|--------|
| 10 5 4 | 10 |
| | 15 |
| | 20 |
| | 25 |

---

**Exercise H2. Print Geometric Sequence**

*Generate a geometric sequence.*

Read first term a, ratio r, and count n. Print n terms, one per line.

- **Input:** Three integers on one line: a r n (1 ≤ n ≤ 20).
- **Output:** n lines.

**Example:**

| Input | Output |
|-------|--------|
| 1 3 5 | 1 |
| | 3 |
| | 9 |
| | 27 |
| | 81 |

---

**Exercise H3. Nth Fibonacci Number**

*Find the Nth Fibonacci number (0-indexed).*

Read N. Print the Nth Fibonacci number. F(0)=0, F(1)=1, F(2)=1, F(3)=2, ...

- **Input:** One integer N (0 ≤ N ≤ 40).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 0 | 0 |
| 7 | 13 |
| 10 | 55 |

---

**Exercise H4. Sum of Fibonacci up to N**

*Sum all Fibonacci numbers that are ≤ N.*

Read N. Print the sum of all Fibonacci numbers that are ≤ N.

- **Input:** One integer N (1 ≤ N ≤ 100000).
- **Output:** One integer — the sum.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 20 |
| 20 | 33 |

*Explanation: 0+1+1+2+3+5+8 = 20 (all Fibonacci ≤ 10).*

---

**Exercise H5. Find Term in Arithmetic Sequence**

*Determine if a value is in an arithmetic sequence.*

Read first term a, common difference d, and target value t. Print which term number it is (1-indexed), or "not in sequence" if it is not.

- **Input:** Three integers on one line: a d t.
- **Output:** One line.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 19 | Term 5 |
| 3 4 20 | not in sequence |

---

**Exercise H6. Geometric Series Sum**

*Sum the first n terms of a geometric sequence.*

Read first term a, ratio r (as a float), and count n. Print the sum of the first n terms.

- **Input:** Three values on one line: a (int), r (float), n (int).
- **Output:** One float rounded to 4 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 1 0.5 5 | 1.9375 |
| 2 3 4 | 80.0000 |

---

**Exercise H7. Sequence Type Detector**

*Identify the type of a sequence.*

Read 5 numbers. Determine if they form an arithmetic sequence, a geometric sequence, or neither.

- **Input:** Five numbers on one line.
- **Output:** `arithmetic`, `geometric`, or `neither`.

**Example:**

| Input | Output |
|-------|--------|
| 2 5 8 11 14 | arithmetic |
| 3 6 12 24 48 | geometric |
| 1 2 4 7 11 | neither |
