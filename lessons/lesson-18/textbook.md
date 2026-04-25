# Lesson 18: Power and Exponents ⚡

> **Goal:** Use the `**` operator and `pow()` function to calculate powers, understand negative exponents, and solve real-world problems involving exponential growth.

---

## 1. The Power Operator `**`

In math, `2³` means "2 multiplied by itself 3 times" = 2 × 2 × 2 = 8.

In Python, we write this as `2 ** 3`.

```python
print(2 ** 3)    # 8
print(5 ** 2)    # 25  (5 squared)
print(3 ** 4)    # 81  (3 to the power 4)
print(10 ** 6)   # 1000000
```

| Math notation | Python | Result |
|---------------|--------|--------|
| 2³ | `2 ** 3` | 8 |
| 5² | `5 ** 2` | 25 |
| 10⁶ | `10 ** 6` | 1000000 |
| 7¹ | `7 ** 1` | 7 |

---

## 2. Power of Zero

Any number to the power of 0 equals 1.

```python
print(2 ** 0)    # 1
print(100 ** 0)  # 1
print(0 ** 0)    # 1  (special case in Python)
```

> 💡 **Rule:** `x ** 0 = 1` for any x.

---

## 3. Negative Exponents

A negative exponent means "1 divided by the positive power".

```python
print(2 ** -1)   # 0.5   (= 1/2)
print(2 ** -2)   # 0.25  (= 1/4)
print(10 ** -3)  # 0.001 (= 1/1000)
```

| Python | Math meaning | Result |
|--------|-------------|--------|
| `2 ** -1` | 1 / 2¹ | 0.5 |
| `2 ** -2` | 1 / 2² | 0.25 |
| `10 ** -3` | 1 / 10³ | 0.001 |

---

## 4. The `pow()` Function

`pow(base, exponent)` does the same thing as `**`.

```python
print(pow(2, 10))    # 1024
print(pow(3, 3))     # 27
print(pow(5, 0))     # 1
```

`pow()` is useful when you want to make your code read more like English: "the power of 2 to 10".

---

## 5. Large Numbers — Python Handles Them!

Python can handle very large numbers exactly (no overflow!).

```python
print(2 ** 100)
# 1267650600228229401496703205376

print(2 ** 64)
# 18446744073709551616
```

This is different from many other programming languages that would give an error or wrong answer for such large numbers.

---

## 6. Scientific Notation

Very large or very small numbers can be written in scientific notation.

```python
# Scientific notation in Python
x = 1e6     # 1 × 10^6 = 1,000,000
y = 2.5e3   # 2.5 × 10^3 = 2,500
z = 1e-4    # 1 × 10^-4 = 0.0001

print(x)    # 1000000.0
print(y)    # 2500.0
print(z)    # 0.0001
```

---

## 7. Compound Interest

Compound interest formula: `A = P × (1 + r/100) ** n`

- `P` = principal (starting amount)
- `r` = annual interest rate (%)
- `n` = number of years
- `A` = final amount

```python
P = 1000    # starting amount: $1000
r = 5       # interest rate: 5% per year
n = 10      # number of years

A = P * (1 + r / 100) ** n
print(f"After {n} years: ${A:.2f}")
# After 10 years: $1628.89
```

---

## 8. Powers of 2 — Binary Connection

Powers of 2 are important in computers because computers use binary (base 2).

```python
for i in range(11):
    print(f"2^{i} = {2 ** i}")
```

Output:
```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1024
```

1 KB = 2¹⁰ = 1024 bytes. 1 MB = 2²⁰ bytes. 1 GB = 2³⁰ bytes.

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| exponent | số mũ | The small number that says how many times to multiply |
| power | lũy thừa | The result of multiplying a number by itself repeatedly |
| base | cơ số | The number being multiplied (in 2³, the base is 2) |
| squared | bình phương | Raised to the power of 2 (e.g., 5² = 25) |
| cubed | lập phương | Raised to the power of 3 (e.g., 2³ = 8) |
| negative exponent | số mũ âm | Means 1 divided by the positive power |
| reciprocal | nghịch đảo | 1 divided by a number (reciprocal of 4 is 1/4) |
| scientific notation | ký hiệu khoa học | Writing numbers as a × 10^b |
| compound interest | lãi kép | Interest calculated on both principal and previous interest |
| binary | nhị phân | Base-2 number system used by computers |
| overflow | tràn số | When a number is too large for a variable to store |
| precision | độ chính xác | How exact a number is |

---

## 10. Summary

✅ `2 ** 3` = 8 (2 to the power 3).
✅ `x ** 0` = 1 for any x.
✅ `2 ** -1` = 0.5 (negative exponent = reciprocal).
✅ `pow(base, exp)` is the same as `base ** exp`.
✅ Python handles very large numbers exactly.
✅ Scientific notation: `1e6` = 1,000,000.
✅ Compound interest: `A = P * (1 + r/100) ** n`.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Square and Cube**

Write a program that reads a number N and prints N squared and N cubed.

- **Input:** One integer N (1 ≤ N ≤ 20).
- **Output:** Two lines: `N squared = ...` and `N cubed = ...`.

**Example:**

| Input | Output |
|-------|--------|
| 4 | N squared = 16 |
| | N cubed = 64 |

---

**Exercise E2. Powers of 10**

Write a program that prints 10⁰ through 10⁶.

- **Input:** None.
- **Output:** 7 lines, each showing `10^k = value`.

**Example:**
```
10^0 = 1
10^1 = 10
10^2 = 100
...
10^6 = 1000000
```

---

**Exercise E3. Zero Power**

Write a program that reads a number N and prints `N ** 0`.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One line: `N^0 = 1`.

**Example:**

| Input | Output |
|-------|--------|
| 42 | 42^0 = 1 |

---

**Exercise E4. Negative Exponent**

Write a program that reads a base B and prints B⁻¹, B⁻², B⁻³.

- **Input:** One integer B (2 ≤ B ≤ 10).
- **Output:** Three lines showing the values.

**Example:**

| Input | Output |
|-------|--------|
| 2 | 2^-1 = 0.5 |
| | 2^-2 = 0.25 |
| | 2^-3 = 0.125 |

---

**Exercise E5. pow() Function**

Write a program that reads base B and exponent E, then prints `pow(B, E)`.

- **Input:** Two integers B (1 ≤ B ≤ 10) and E (0 ≤ E ≤ 10).
- **Output:** One line: `B^E = result`.

**Example:**

| Input | Output |
|-------|--------|
| 3 4 | 3^4 = 81 |

---

**Exercise E6. Large Power**

Write a program that prints the exact value of `2 ** 64`.

- **Input:** None.
- **Output:** The exact value of 2⁶⁴.

**Example:**
```
2^64 = 18446744073709551616
```

---

**Exercise E7. Scientific Notation**

Write a program that prints the values of `1e3`, `2.5e4`, and `1e-2`.

- **Input:** None.
- **Output:** Three lines showing each value.

**Example:**
```
1e3 = 1000.0
2.5e4 = 25000.0
1e-2 = 0.01
```

---

### 🟡 Medium

---

**Exercise M1. Powers of 2 Table**

Write a program that reads N and prints a table of 2⁰ through 2ᴺ.

- **Input:** One integer N (1 ≤ N ≤ 20).
- **Output:** N+1 lines, each showing `2^k = value`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 2^0 = 1 |
| | 2^1 = 2 |
| | 2^2 = 4 |
| | 2^3 = 8 |
| | 2^4 = 16 |
| | 2^5 = 32 |

---

**Exercise M2. Simple Interest vs Compound Interest**

Read principal P, rate R%, and years Y. Print both simple interest and compound interest final amounts.

- **Input:** Three numbers: P (float), R (float), Y (int).
- **Output:** Two lines: simple and compound final amounts, rounded to 2 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 1000 5 10 | Simple: 1500.00 |
| | Compound: 1628.89 |

---

**Exercise M3. Doubling Sequence**

Read a starting value S and print the sequence of doubling it 8 times (S, S×2, S×4, ..., S×2⁸).

- **Input:** One integer S (1 ≤ S ≤ 100).
- **Output:** 9 lines showing each value.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 3 |
| | 6 |
| | 12 |
| | 24 |
| | 48 |
| | 96 |
| | 192 |
| | 384 |
| | 768 |

---

**Exercise M4. Sum of Powers**

Read N and print the sum of 1² + 2² + 3² + ... + N².

- **Input:** One integer N (1 ≤ N ≤ 100).
- **Output:** One line: `Sum = value`.

**Example:**

| Input | Output |
|-------|--------|
| 4 | Sum = 30 |

*Explanation: 1 + 4 + 9 + 16 = 30.*

---

**Exercise M5. Power Comparison**

Read two numbers A and B. Print which is larger: A² or B³.

- **Input:** Two integers A and B (1 ≤ A, B ≤ 20).
- **Output:** One line showing which is larger (or "equal").

**Example:**

| Input | Output |
|-------|--------|
| 3 2 | A^2 = 9, B^3 = 8, A^2 is larger |
| 2 2 | A^2 = 4, B^3 = 8, B^3 is larger |

---

**Exercise M6. Memory Size**

Write a program that prints the size in bytes for 1 KB, 1 MB, 1 GB, and 1 TB using powers of 2.

- **Input:** None.
- **Output:** Four lines.

**Example:**
```
1 KB = 1024 bytes
1 MB = 1048576 bytes
1 GB = 1073741824 bytes
1 TB = 1099511627776 bytes
```

---

**Exercise M7. Bacteria Growth**

Bacteria double every hour. Read the initial count N and hours H. Print the count after each hour.

- **Input:** Two integers N (1 ≤ N ≤ 100) and H (1 ≤ H ≤ 10).
- **Output:** H lines, each showing `Hour k: count`.

**Example:**

| Input | Output |
|-------|--------|
| 5 4 | Hour 1: 10 |
| | Hour 2: 20 |
| | Hour 3: 40 |
| | Hour 4: 80 |

---

### 🔴 Hard

---

**Exercise H1. Powers of 2 (0 to N)**

*Print all powers of 2 from 2⁰ to 2ᴺ.*

Read N and print 2⁰, 2¹, 2², ..., 2ᴺ, one per line.

- **Input:** One integer N (0 ≤ N ≤ 30).
- **Output:** N+1 lines, each showing the value of 2^k.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 1 |
| | 2 |
| | 4 |
| | 8 |
| | 16 |

---

**Exercise H2. Compound Interest**

*Calculate compound interest.*

Read principal P, annual rate R (as a percentage), and years Y. Print the final amount rounded to 2 decimal places.

- **Input:** Three values on one line: P (float), R (float), Y (int).
- **Output:** One line: `Final amount: X.XX`.

**Example:**

| Input | Output |
|-------|--------|
| 1000 5 10 | Final amount: 1628.89 |
| 500 10 3 | Final amount: 665.50 |

---

**Exercise H3. Doubling Problem**

*How many times must you double 1 to reach at least N?*

Read N. Starting from 1, count how many times you must double to reach a value ≥ N.

- **Input:** One integer N (2 ≤ N ≤ 1000000).
- **Output:** One integer — the number of doublings needed.

**Example:**

| Input | Output |
|-------|--------|
| 8 | 3 |
| 100 | 7 |
| 1000 | 10 |

*Explanation: 1 → 2 → 4 → 8 (3 doublings to reach 8).*

---

**Exercise H4. Binary to Decimal**

*Convert a 4-bit binary number to decimal using powers of 2.*

Read 4 digits (each 0 or 1) on one line separated by spaces. Convert to decimal using: d3×2³ + d2×2² + d1×2¹ + d0×2⁰.

- **Input:** Four integers (each 0 or 1) on one line.
- **Output:** One integer — the decimal value.

**Example:**

| Input | Output |
|-------|--------|
| 1 0 1 1 | 11 |
| 1 1 1 1 | 15 |
| 0 1 0 0 | 4 |

*Explanation: 1×8 + 0×4 + 1×2 + 1×1 = 11.*

---

**Exercise H5. Scientific Notation**

*Print a number in scientific notation.*

Read a positive number N (as a float). Print it in the form `a × 10^b` where 1 ≤ a < 10, rounded to 2 decimal places.

- **Input:** One positive float N.
- **Output:** One line in the format `a × 10^b`.

**Example:**

| Input | Output |
|-------|--------|
| 12345 | 1.23 × 10^4 |
| 0.0056 | 5.60 × 10^-3 |
| 100 | 1.00 × 10^2 |

---

**Exercise H6. Power Tower**

*Compute a^(b^c).*

Read three integers a, b, c. Compute a raised to the power of (b raised to the power of c).

- **Input:** Three integers a, b, c (1 ≤ a, b, c ≤ 5).
- **Output:** One integer — the result.

**Example:**

| Input | Output |
|-------|--------|
| 2 3 2 | 512 |
| 3 2 3 | 6561 |

*Explanation: 2^(3^2) = 2^9 = 512.*

---

**Exercise H7. Bacteria Growth**

*Bacteria double every hour. Find the final count.*

A scientist starts with N bacteria. They double every hour. After H hours, how many bacteria are there?

- **Input:** Two integers N (1 ≤ N ≤ 1000) and H (1 ≤ H ≤ 20).
- **Output:** One integer — the final count.

**Example:**

| Input | Output |
|-------|--------|
| 10 5 | 320 |
| 1 10 | 1024 |

*Explanation: 10 × 2⁵ = 10 × 32 = 320.*
