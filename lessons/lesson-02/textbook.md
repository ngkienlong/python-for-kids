# Lesson 2: Numbers and Math 🔢

> **Goal:** Use Python as a powerful calculator. Learn math operators and how to combine them with `print()`.

---

## 1. Python is a Super Calculator!

In Scratch, you use the **Operators** blocks (green blocks) to do math.
In Python, you just type the math directly!

Try this in Thonny:

```python
print(3 + 5)
```

**Output:**
```
8
```

Python calculated `3 + 5` and printed the answer. Easy!

---

## 2. Math Operators

Here are the math operators in Python:

| Operator | Name | Example | Result | Scratch |
|----------|------|---------|--------|---------|
| `+` | Addition | `7 + 3` | `10` | (_ + _) block |
| `-` | Subtraction | `7 - 3` | `4` | (_ - _) block |
| `*` | Multiplication | `7 * 3` | `21` | (_ × _) block |
| `/` | Division | `7 / 2` | `3.5` | (_ / _) block |
| `//` | Floor division | `7 // 2` | `3` | — |
| `%` | Modulo (remainder) | `7 % 2` | `1` | (_ mod _) block |

Let's try them all:

```python
print(7 + 3)   # Addition: 10
print(7 - 3)   # Subtraction: 4
print(7 * 3)   # Multiplication: 21
print(7 / 2)   # Division: 3.5
print(7 // 2)  # Floor division: 3 (no decimal)
print(7 % 2)   # Modulo: 1 (remainder)
```

---

## 3. Division: `/` vs `//`

Python has **two kinds** of division:

| Operator | Name | What it does | Example |
|----------|------|-------------|---------|
| `/` | Division | Gives the exact answer (with decimal) | `7 / 2` → `3.5` |
| `//` | Floor division | Gives only the whole number part | `7 // 2` → `3` |

```python
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
```

> 💡 Think of `//` as "how many whole times does it fit?"
> 10 ÷ 3 = 3 whole times (with some left over).

---

## 4. Modulo: `%` (Remainder)

The `%` operator gives the **remainder** after division.

```python
print(10 % 3)   # 1  (because 10 = 3 × 3 + 1)
print(15 % 4)   # 3  (because 15 = 4 × 3 + 3)
print(20 % 5)   # 0  (because 20 = 5 × 4 + 0, no remainder)
```

> 💡 **Useful trick:** If `n % 2 == 0`, the number is **even**. If `n % 2 == 1`, it's **odd**.

```python
print(8 % 2)    # 0 → 8 is even
print(7 % 2)    # 1 → 7 is odd
```

---

## 5. Order of Operations (PEMDAS)

Python follows the same math rules you learn in school:

1. **P**arentheses `()` — first
2. **E**xponents `**` — second (you'll learn this in Lesson 18)
3. **M**ultiplication `*` and **D**ivision `/` — third (left to right)
4. **A**ddition `+` and **S**ubtraction `-` — last (left to right)

```python
print(2 + 3 * 4)       # 14 (not 20! multiplication first)
print((2 + 3) * 4)     # 20 (parentheses first)
print(10 - 2 * 3)      # 4
print((10 - 2) * 3)    # 24
```

> 💡 **Tip:** When in doubt, use parentheses `()` to make it clear!

---

## 6. Integers and Floats

Python has two types of numbers:

| Type | Name | Examples | Vietnamese |
|------|------|---------|-----------|
| `int` | Integer | `5`, `0`, `-3`, `100` | Số nguyên |
| `float` | Float (decimal) | `3.5`, `0.1`, `-2.7` | Số thực (thập phân) |

```python
print(5)      # int (integer)
print(3.5)    # float (decimal number)
print(5 + 0)  # 5 (int)
print(5 + 0.0)# 5.0 (float! because 0.0 is a float)
```

**Rule:** If you mix `int` and `float`, the result is always `float`.

```python
print(5 + 2)    # 7 (int + int = int)
print(5 + 2.0)  # 7.0 (int + float = float)
print(10 / 2)   # 5.0 (/ always gives float!)
print(10 // 2)  # 5 (// gives int when both are int)
```

---

## 7. Negative Numbers

Python handles negative numbers just like math class:

```python
print(-5)         # -5
print(-5 + 3)     # -2
print(3 - 10)     # -7
print(-3 * -2)    # 6 (negative × negative = positive)
print(-10 / 2)    # -5.0
```

---

## 8. Printing Math with Text

You can combine text and math in `print()`:

```python
# Method 1: Use commas
print("5 + 3 =", 5 + 3)

# Method 2: Use string concatenation (joining)
print("The answer is " + str(8))
```

**Output:**
```
5 + 3 = 8
The answer is 8
```

> 💡 With commas, Python adds a space between items automatically.

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| operator | toán tử | A symbol that does math (+, -, *, /) |
| addition | phép cộng | Adding numbers together (+) |
| subtraction | phép trừ | Taking one number from another (-) |
| multiplication | phép nhân | Multiplying numbers (*) |
| division | phép chia | Dividing one number by another (/) |
| floor division | phép chia lấy phần nguyên | Division that gives only the whole part (//) |
| modulo | phép chia lấy dư | The remainder after division (%) |
| remainder | số dư | What is left over after division |
| integer | số nguyên | A whole number (no decimal point) |
| float | số thực | A number with a decimal point |
| parentheses | dấu ngoặc đơn | Round brackets () used to group math |
| negative | số âm | A number less than zero |
| order of operations | thứ tự phép tính | The rules for which math to do first |
| expression | biểu thức | A piece of code that has a value (like `3 + 5`) |

---

## 10. Summary

✅ Python can do math: `+`, `-`, `*`, `/`, `//`, `%`.
✅ `/` gives a decimal answer. `//` gives only the whole number.
✅ `%` gives the remainder after division.
✅ Python follows order of operations (PEMDAS). Use `()` when in doubt.
✅ `int` = whole number, `float` = decimal number.
✅ You can print text and math together using commas.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Add Two Numbers**

Write a program that prints the result of `25 + 17`.

- **Input:** None.
- **Output:** Print the result of 25 + 17.

**Example:**
```
42
```

---

**Exercise E2. Subtract**

Write a program that prints the result of `100 - 37`.

- **Input:** None.
- **Output:** Print the result of 100 - 37.

**Example:**
```
63
```

---

**Exercise E3. Multiply**

Write a program that prints the result of `12 * 9`.

- **Input:** None.
- **Output:** Print the result of 12 × 9.

**Example:**
```
108
```

---

**Exercise E4. Divide**

Write a program that prints the result of `100 / 8`.

- **Input:** None.
- **Output:** Print the result of 100 ÷ 8.

**Example:**
```
12.5
```

---

**Exercise E5. Floor Division**

Write a program that prints the result of `100 // 8`.

- **Input:** None.
- **Output:** Print the result.

**Example:**
```
12
```

---

**Exercise E6. Remainder**

Write a program that prints the remainder when 100 is divided by 8.

- **Input:** None.
- **Output:** Print the remainder of 100 ÷ 8.

**Example:**
```
4
```

---

**Exercise E7. All Operators**

Write a program that prints the results of all 6 operators with numbers 20 and 7:

- **Input:** None.
- **Output:**
```
20 + 7 = 27
20 - 7 = 13
20 * 7 = 140
20 / 7 = 2.857142857142857
20 // 7 = 2
20 % 7 = 6
```

---

### 🟡 Medium

---

**Exercise M1. Parentheses Matter**

What is the output of each line? First **predict** the answer on paper, then check with Python.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 - 6 / 2)
print((10 - 6) / 2)
print(8 + 2 * 5 - 1)
```

- **Input:** None.
- **Output:** Write the 5 results, one per line.

---

**Exercise M2. Seconds in a Day**

Write a program that calculates how many **seconds** are in one day.

- **Input:** None.
- **Output:** Print the number of seconds in one day.

**Example:**
```
86400
```

(Hint: 1 day = 24 hours, 1 hour = 60 minutes, 1 minute = 60 seconds.)

---

**Exercise M3. Average**

Write a program that calculates the average of 3 numbers: 85, 92, and 78.

- **Input:** None.
- **Output:** Print the average.

**Example:**
```
85.0
```

(Hint: Average = sum ÷ count.)

---

**Exercise M4. Temperature Converter**

The formula to convert Celsius to Fahrenheit is: **F = C × 9 / 5 + 32**.

Write a program that converts 37°C (body temperature) to Fahrenheit.

- **Input:** None.
- **Output:** Print the temperature in Fahrenheit.

**Example:**
```
98.6
```

---

**Exercise M5. Rectangle**

A rectangle has width = 15 and height = 8. Write a program that prints:
- The area (width × height).
- The perimeter (2 × width + 2 × height).

- **Input:** None.
- **Output:**
```
Area = 120
Perimeter = 46
```

---

**Exercise M6. Even or Odd Check**

Write a program that prints the remainder when each of these numbers is divided by 2: 10, 15, 22, 33, 100.

- **Input:** None.
- **Output:**
```
10 % 2 = 0
15 % 2 = 1
22 % 2 = 0
33 % 2 = 1
100 % 2 = 0
```

(Hint: 0 means even, 1 means odd.)

---

**Exercise M7. Big Multiplication**

Write a program that prints the result of `12345 * 67890`.

- **Input:** None.
- **Output:** Print the result.

**Example:**
```
838102050
```

---

### 🔴 Hard

---

**Exercise H1. Coin Change**

You have **N** dong (Vietnamese currency). You want to exchange all of it into coins. You have 3 types of coins: 500 dong, 200 dong, and 100 dong.

Use the **largest coins first** (greedy method). How many coins of each type do you get?

- **Input:** One integer N (100 ≤ N ≤ 10000), guaranteed to be a multiple of 100.
- **Output:** Three lines:
  - Line 1: number of 500-dong coins.
  - Line 2: number of 200-dong coins.
  - Line 3: number of 100-dong coins.

**Example:**

| Input | Output |
|-------|--------|
| 1900 | 3 |
| | 2 |
| | 0 |
| 100 | 0 |
| | 0 |
| | 1 |

**Explanation:** For 1900: 1900 // 500 = 3 coins (uses 1500). Remaining = 400. 400 // 200 = 2 coins (uses 400). Remaining = 0. 0 // 100 = 0 coins.

(Hint: Use `//` and `%` step by step. Set `n = 1900` in your code.)

---

**Exercise H2. Time Breakdown**

A movie is **N** seconds long. Convert it to hours, minutes, and seconds.

- **Input:** One integer N (1 ≤ N ≤ 100000) — the length of the movie in seconds.
- **Output:** Three integers on one line, separated by spaces: hours, minutes, seconds.

**Example:**

| Input | Output |
|-------|--------|
| 3661 | 1 1 1 |
| 7200 | 2 0 0 |
| 90 | 0 1 30 |

**Explanation:** 3661 seconds = 1 hour, 1 minute, 1 second.

(Hint: hours = N // 3600. Then find remaining seconds and calculate minutes.)

---

**Exercise H3. Digit Extraction**

Given a **3-digit** number N, print each digit on a separate line (hundreds, tens, ones).

- **Input:** One integer N (100 ≤ N ≤ 999).
- **Output:** Three lines: the hundreds digit, the tens digit, the ones digit.

**Example:**

| Input | Output |
|-------|--------|
| 456 | 4 |
| | 5 |
| | 6 |
| 100 | 1 |
| | 0 |
| | 0 |

**Explanation:** For 456: hundreds = 456 // 100 = 4, tens = (456 // 10) % 10 = 5, ones = 456 % 10 = 6.

(Hint: Use `//` and `%` with 100 and 10.)

---

**Exercise H4. Sharing Apples**

A teacher has **N** apples and **K** students. She gives each student the same number of apples. The leftover apples go back to the teacher.

Print: how many apples each student gets, and how many the teacher keeps.

- **Input:** Two integers N and K (1 ≤ N ≤ 1000, 1 ≤ K ≤ 100).
- **Output:** Two lines:
  - Line 1: apples per student.
  - Line 2: leftover apples.

**Example:**

| Input | Output |
|-------|--------|
| 23 5 | 4 |
| | 3 |
| 10 3 | 3 |
| | 1 |

**Explanation:** 23 apples ÷ 5 students = 4 each, 3 left over.

(Hint: Set `n = 23` and `k = 5` in your code. Use `//` and `%`.)

---

**Exercise H5. Reverse a 3-Digit Number**

Given a **3-digit** number N, print the number with its digits reversed.

- **Input:** One integer N (100 ≤ N ≤ 999).
- **Output:** The reversed number.

**Example:**

| Input | Output |
|-------|--------|
| 456 | 654 |
| 100 | 1 |
| 520 | 25 |

**Explanation:** For 456: ones = 6, tens = 5, hundreds = 4. Reversed = 6 × 100 + 5 × 10 + 4 = 654.

(Hint: Extract each digit using `//` and `%`, then build the reversed number.)

---

**Exercise H6. Chessboard Squares**

A chessboard has 8 rows and 8 columns. Each square is either **black** or **white**. The square at row `r`, column `c` is **black** if `(r + c)` is even, and **white** if `(r + c)` is odd.

Given row `r` and column `c`, print the color of that square.

- **Input:** Two integers r and c (1 ≤ r ≤ 8, 1 ≤ c ≤ 8).
- **Output:** Print `black` or `white`.

**Example:**

| Input | Output |
|-------|--------|
| 1 1 | black |
| 1 2 | white |
| 3 5 | black |

**Explanation:** Row 1, Column 1: 1 + 1 = 2 (even) → black. Row 1, Column 2: 1 + 2 = 3 (odd) → white.

(Hint: Check if `(r + c) % 2 == 0`. You will learn `if/else` in Lesson 5. For now, just print `(r + c) % 2` and think about what 0 and 1 mean.)

---

**Exercise H7. Sum of Digits**

Given a **3-digit** number N, calculate the **sum of its digits**.

- **Input:** One integer N (100 ≤ N ≤ 999).
- **Output:** The sum of the three digits.

**Example:**

| Input | Output |
|-------|--------|
| 456 | 15 |
| 100 | 1 |
| 999 | 27 |

**Explanation:** For 456: 4 + 5 + 6 = 15.

(Hint: Extract each digit using `//` and `%`, then add them together.)

---
