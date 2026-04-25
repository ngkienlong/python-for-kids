# Lesson 21: Even, Odd and Divisibility 🔢

> **Goal:** Use the `%` (modulo) operator to check even/odd, test divisibility, find GCD and LCM, and apply divisibility rules.

---

## 1. Even and Odd

A number is **even** if it is divisible by 2 (remainder = 0).
A number is **odd** if it is not divisible by 2 (remainder = 1).

```python
n = 7

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
```

| n | n % 2 | Even or Odd? |
|---|-------|-------------|
| 4 | 0 | Even |
| 7 | 1 | Odd |
| 0 | 0 | Even |
| -3 | 1 | Odd |

---

## 2. Divisibility

A number n is **divisible by k** if `n % k == 0`.

```python
n = 24

print(n % 2 == 0)   # True  (24 is divisible by 2)
print(n % 3 == 0)   # True  (24 is divisible by 3)
print(n % 5 == 0)   # False (24 is not divisible by 5)
print(n % 6 == 0)   # True  (24 is divisible by 6)
```

---

## 3. Divisibility Rules

Some quick rules for checking divisibility:

| Divisible by | Rule | Example |
|-------------|------|---------|
| 2 | Last digit is 0, 2, 4, 6, or 8 | 48 ÷ 2 ✓ |
| 3 | Sum of digits is divisible by 3 | 123: 1+2+3=6 ✓ |
| 5 | Last digit is 0 or 5 | 35 ÷ 5 ✓ |
| 9 | Sum of digits is divisible by 9 | 729: 7+2+9=18 ✓ |
| 10 | Last digit is 0 | 100 ÷ 10 ✓ |

```python
n = 123
digit_sum = 1 + 2 + 3   # = 6
print(digit_sum % 3 == 0)   # True → 123 is divisible by 3
```

---

## 4. GCD — Greatest Common Divisor

The **GCD** of two numbers is the largest number that divides both.

**Euclidean algorithm:**

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 8))    # 4
print(gcd(100, 75))  # 25
```

How it works:
- `gcd(12, 8)`: a=12, b=8 → a=8, b=4 → a=4, b=0 → return 4.

Python also has `math.gcd()`:

```python
import math
print(math.gcd(12, 8))   # 4
```

---

## 5. LCM — Least Common Multiple

The **LCM** of two numbers is the smallest number that is a multiple of both.

Formula: `LCM(a, b) = a × b ÷ GCD(a, b)`

```python
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

print(lcm(4, 6))     # 12
print(lcm(3, 5))     # 15
print(lcm(12, 18))   # 36
```

---

## 6. Finding All Divisors

A **divisor** of n is any number that divides n evenly.

```python
n = 24
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(divisors)   # [1, 2, 3, 4, 6, 8, 12, 24]
```

---

## 7. Perfect Numbers

A **perfect number** equals the sum of its proper divisors (all divisors except itself).

Example: 6 = 1 + 2 + 3 (divisors of 6 are 1, 2, 3, 6; proper divisors are 1, 2, 3).

```python
n = 28
proper_divisors_sum = sum(i for i in range(1, n) if n % i == 0)
if proper_divisors_sum == n:
    print(f"{n} is a perfect number!")
```

Perfect numbers: 6, 28, 496, 8128, ...

---

## 8. Coprime Numbers

Two numbers are **coprime** (or relatively prime) if their GCD = 1.

```python
import math

a = 9
b = 16
if math.gcd(a, b) == 1:
    print(f"{a} and {b} are coprime")
else:
    print(f"{a} and {b} are NOT coprime")
```

---

## 9. Reducing Fractions

To reduce a fraction a/b, divide both by their GCD.

```python
import math

numerator = 12
denominator = 18
g = math.gcd(numerator, denominator)
print(f"{numerator}/{denominator} = {numerator // g}/{denominator // g}")
# 12/18 = 2/3
```

---

## 10. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| even | số chẵn | Divisible by 2 |
| odd | số lẻ | Not divisible by 2 |
| divisible | chia hết | Can be divided with no remainder |
| remainder | số dư | What is left over after division |
| modulo | phép chia lấy dư | The `%` operator — gives the remainder |
| GCD | ước chung lớn nhất | Greatest Common Divisor |
| LCM | bội chung nhỏ nhất | Least Common Multiple |
| Euclidean algorithm | thuật toán Euclid | A method to find GCD using repeated division |
| factor | ước số | A number that divides another evenly |
| multiple | bội số | A number that is a product of another |
| divisibility rule | quy tắc chia hết | A shortcut to check divisibility |
| coprime | nguyên tố cùng nhau | Two numbers whose GCD is 1 |

---

## 11. Summary

✅ Even: `n % 2 == 0`. Odd: `n % 2 != 0`.
✅ Divisible by k: `n % k == 0`.
✅ GCD using Euclidean algorithm: `while b != 0: a, b = b, a % b`.
✅ `math.gcd(a, b)` is the built-in GCD function.
✅ LCM: `a * b // gcd(a, b)`.
✅ Divisors: loop from 1 to n, check `n % i == 0`.
✅ Perfect number: sum of proper divisors equals the number.
✅ Coprime: GCD = 1.
✅ Reduce fraction: divide numerator and denominator by GCD.

---

## 12. Homework

### 🟢 Easy

---

**Exercise E1. Even or Odd**

Read a number N and print "even" or "odd".

- **Input:** One integer N.
- **Output:** `even` or `odd`.

**Example:**

| Input | Output |
|-------|--------|
| 7 | odd |
| 12 | even |

---

**Exercise E2. Divisible by 3**

Read N and print "yes" if N is divisible by 3, "no" otherwise.

- **Input:** One integer N.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 9 | yes |
| 10 | no |

---

**Exercise E3. Remainder**

Read two integers A and B. Print the remainder when A is divided by B.

- **Input:** Two integers A and B on one line.
- **Output:** One integer — the remainder.

**Example:**

| Input | Output |
|-------|--------|
| 17 5 | 2 |

---

**Exercise E4. Count Even Numbers**

Read N and print how many even numbers are from 1 to N.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 5 |
| 7 | 3 |

---

**Exercise E5. Divisibility Check**

Read N. Print "yes" if N is divisible by both 3 and 5, "no" otherwise.

- **Input:** One integer N.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 15 | yes |
| 9 | no |

---

**Exercise E6. Sum of Even Numbers**

Read N and print the sum of all even numbers from 1 to N.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 30 |

*Explanation: 2 + 4 + 6 + 8 + 10 = 30.*

---

**Exercise E7. Last Digit**

Read N and print its last digit.

- **Input:** One positive integer N.
- **Output:** One digit (0–9).

**Example:**

| Input | Output |
|-------|--------|
| 1234 | 4 |
| 100 | 0 |

---

### 🟡 Medium

---

**Exercise M1. GCD (Euclidean)**

Read two integers A and B. Print their GCD using the Euclidean algorithm.

- **Input:** Two integers A and B on one line.
- **Output:** One integer — the GCD.

**Example:**

| Input | Output |
|-------|--------|
| 12 8 | 4 |
| 100 75 | 25 |

---

**Exercise M2. LCM**

Read two integers A and B. Print their LCM.

- **Input:** Two integers A and B on one line.
- **Output:** One integer — the LCM.

**Example:**

| Input | Output |
|-------|--------|
| 4 6 | 12 |
| 3 5 | 15 |

---

**Exercise M3. List Divisors**

Read N and print all divisors of N separated by spaces.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** All divisors of N, separated by spaces.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 1 2 3 4 6 12 |

---

**Exercise M4. Reduce Fraction**

Read numerator and denominator. Print the reduced fraction.

- **Input:** Two integers on one line.
- **Output:** One line: `a/b` (reduced form).

**Example:**

| Input | Output |
|-------|--------|
| 12 18 | 2/3 |
| 6 4 | 3/2 |

---

**Exercise M5. FizzBuzz**

Print numbers from 1 to 30. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for multiples of both print "FizzBuzz".

- **Input:** None.
- **Output:** 30 lines.

**Example:**
```
1
2
Fizz
4
Buzz
Fizz
...
FizzBuzz
```

---

**Exercise M6. Sum of Multiples**

Read N and K. Print the sum of all multiples of K from 1 to N.

- **Input:** Two integers N and K on one line.
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 20 3 | 63 |

*Explanation: 3 + 6 + 9 + 12 + 15 + 18 = 63.*

---

**Exercise M7. Count Divisors**

Read N and print how many divisors N has.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** One integer.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 6 |
| 7 | 2 |

---

### 🔴 Hard

---

**Exercise H1. GCD**

*Find the Greatest Common Divisor.*

Read two integers A and B. Print their GCD using the Euclidean algorithm (do not use `math.gcd`).

- **Input:** Two integers A and B on one line (1 ≤ A, B ≤ 10^6).
- **Output:** One integer — the GCD.

**Example:**

| Input | Output |
|-------|--------|
| 48 18 | 6 |
| 1000 250 | 250 |

---

**Exercise H2. LCM**

*Find the Least Common Multiple.*

Read two integers A and B. Print their LCM.

- **Input:** Two integers A and B on one line (1 ≤ A, B ≤ 10^6).
- **Output:** One integer — the LCM.

**Example:**

| Input | Output |
|-------|--------|
| 12 18 | 36 |
| 7 5 | 35 |

---

**Exercise H3. Count Divisors**

*Find all divisors of a number.*

Read N. Print all divisors of N, one per line, in ascending order.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** All divisors of N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 24 | 1 |
| | 2 |
| | 3 |
| | 4 |
| | 6 |
| | 8 |
| | 12 |
| | 24 |

---

**Exercise H4. Perfect Number Check**

*Check if a number is perfect.*

A perfect number equals the sum of its proper divisors (all divisors except itself). Read N and print "perfect" or "not perfect".

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** `perfect` or `not perfect`.

**Example:**

| Input | Output |
|-------|--------|
| 6 | perfect |
| 28 | perfect |
| 12 | not perfect |

---

**Exercise H5. Coprime Check**

*Check if two numbers are coprime.*

Read A and B. Print "coprime" if GCD(A, B) = 1, otherwise print "not coprime".

- **Input:** Two integers A and B on one line.
- **Output:** `coprime` or `not coprime`.

**Example:**

| Input | Output |
|-------|--------|
| 9 16 | coprime |
| 6 9 | not coprime |

---

**Exercise H6. Sum of Multiples**

*Sum all multiples of K up to N.*

Read N and K. Print the sum of all multiples of K from 1 to N (inclusive).

- **Input:** Two integers N and K on one line (1 ≤ K ≤ N ≤ 10^6).
- **Output:** One integer — the sum.

**Example:**

| Input | Output |
|-------|--------|
| 10 2 | 30 |
| 100 7 | 735 |

---

**Exercise H7. Reduce Fraction**

*Simplify a fraction to its lowest terms.*

Read numerator P and denominator Q. Print the reduced fraction P/Q.

- **Input:** Two integers P and Q on one line (Q ≠ 0).
- **Output:** One line: `P/Q` in reduced form.

**Example:**

| Input | Output |
|-------|--------|
| 24 36 | 2/3 |
| 100 75 | 4/3 |
| 7 14 | 1/2 |
