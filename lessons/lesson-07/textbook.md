# Lesson 7: Logic — And, Or, Not 🔗

> **Goal:** Combine conditions using `and`, `or`, and `not` to write more powerful and readable programs.

---

## 1. Why Combine Conditions?

Sometimes one condition is not enough. For example:

- "You can ride the roller coaster if you are **at least 10 years old AND at least 120 cm tall**."
- "You get a discount if you are a student **OR** a senior."
- "The alarm rings if the door is **NOT** locked."

In Scratch, you used the **"and"**, **"or"**, and **"not"** blocks. Python has the same operators!

| Scratch | Python |
|---------|--------|
| `<A> and <B>` block | `A and B` |
| `<A> or <B>` block | `A or B` |
| `not <A>` block | `not A` |

---

## 2. The `and` Operator

`and` returns `True` only if **both** conditions are True.

```python
age = 15
height = 130

if age >= 10 and height >= 120:
    print("You can ride!")
else:
    print("Sorry, you cannot ride.")
```

**Output:** `You can ride!` (because 15 ≥ 10 AND 130 ≥ 120 — both True)

### Truth table for `and`:

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

`and` is True **only** when both sides are True. If either side is False, the result is False.

---

## 3. The `or` Operator

`or` returns `True` if **at least one** condition is True.

```python
age = 65
is_student = False

if age < 18 or is_student:
    print("You get a discount!")
else:
    print("Full price.")
```

**Output:** `You get a discount!` (because 65 < 18 is False, but `is_student` is also False... wait, let's fix the example)

```python
age = 65

if age < 18 or age >= 60:
    print("You get a discount!")
else:
    print("Full price.")
```

**Output:** `You get a discount!` (because 65 ≥ 60 is True — one condition is enough)

### Truth table for `or`:

| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

`or` is False **only** when both sides are False.

---

## 4. The `not` Operator

`not` **flips** a boolean value: True becomes False, and False becomes True.

```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
else:
    print("Stay inside.")
```

**Output:** `Let's go outside!` (because `not False` = `True`)

### Truth table for `not`:

| A | not A |
|---|-------|
| True | **False** |
| False | **True** |

---

## 5. Combining Multiple Conditions

You can chain multiple `and`/`or` in one condition:

```python
x = 7

# Check if x is between 1 and 10 (inclusive)
if x >= 1 and x <= 10:
    print("In range")
else:
    print("Out of range")
```

```python
score = 75
attendance = 80

# Pass if score >= 60 AND attendance >= 75
if score >= 60 and attendance >= 75:
    print("Pass")
else:
    print("Fail")
```

---

## 6. Operator Precedence

When you mix `and`, `or`, and `not`, Python evaluates them in this order:

1. `not` (highest priority — evaluated first)
2. `and`
3. `or` (lowest priority — evaluated last)

```python
# This:
True or False and False
# is the same as:
True or (False and False)   # → True or False → True

# Use parentheses to make it clear!
(True or False) and False   # → True and False → False
```

> 💡 **Tip:** When in doubt, use parentheses `()` to make the order clear. It also makes your code easier to read.

---

## 7. Short-Circuit Evaluation

Python is smart — it stops evaluating as soon as it knows the answer.

- For `and`: if the **left side is False**, Python skips the right side (the result is already False).
- For `or`: if the **left side is True**, Python skips the right side (the result is already True).

```python
x = 0

# Python checks x != 0 first.
# If x == 0, it is False, so Python skips 10 / x (avoids division by zero!).
if x != 0 and 10 / x > 2:
    print("yes")
else:
    print("no")
```

This is called **short-circuit evaluation**. It is useful for avoiding errors.

---

## 8. Practical Examples

### Check if a number is in a range:

```python
n = int(input("Enter a number: "))
if n >= 1 and n <= 100:
    print("In range")
else:
    print("Out of range")
```

### Check if a character is a vowel:

```python
letter = input("Enter a letter: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("vowel")
else:
    print("consonant")
```

### Check login:

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome!")
else:
    print("Wrong username or password.")
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| logical operator | toán tử logic | and, or, not |
| and | và | True only if both conditions are True |
| or | hoặc | True if at least one condition is True |
| not | không / phủ định | Flips True to False and vice versa |
| truth table | bảng chân trị | A table showing all possible True/False combinations |
| combine | kết hợp | Join two conditions together |
| condition | điều kiện | An expression that is True or False |
| both | cả hai | Two things at the same time |
| either | một trong hai | At least one of two things |
| negate | phủ định | Flip True to False or False to True |
| short-circuit | ngắn mạch | Stop evaluating early when the result is known |
| precedence | thứ tự ưu tiên | The order in which operators are evaluated |

---

## 10. Summary

✅ `and` — both conditions must be True.
✅ `or` — at least one condition must be True.
✅ `not` — flips True to False and False to True.
✅ Use parentheses `()` to make complex conditions clear.
✅ Precedence order: `not` → `and` → `or`.
✅ Short-circuit: Python stops early when the result is already known.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Both Positive**

Read two numbers. Print `yes` if both are positive (greater than 0), otherwise print `no`.

- **Input:** Two integers, one per line.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 5 | yes |
| -1 / 5 | no |
| 0 / 5 | no |

---

**Exercise E2. Either Zero**

Read two numbers. Print `yes` if at least one of them is 0, otherwise print `no`.

- **Input:** Two integers, one per line.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 0 / 5 | yes |
| 3 / 0 | yes |
| 3 / 5 | no |
| 0 / 0 | yes |

---

**Exercise E3. Not Negative**

Read a number. Print `yes` if it is NOT negative (i.e., 0 or positive), otherwise print `no`.

- **Input:** One integer.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | yes |
| 0 | yes |
| -3 | no |

---

**Exercise E4. Teen**

Read an age. Print `teen` if the age is between 13 and 19 (inclusive), otherwise print `not teen`.

- **Input:** One integer.
- **Output:** `teen` or `not teen`.

**Example:**

| Input | Output |
|-------|--------|
| 15 | teen |
| 12 | not teen |
| 19 | teen |
| 20 | not teen |

---

**Exercise E5. Pass Both**

Read two scores. Print `pass` if both scores are 50 or above, otherwise print `fail`.

- **Input:** Two integers, one per line.
- **Output:** `pass` or `fail`.

**Example:**

| Input | Output |
|-------|--------|
| 70 / 80 | pass |
| 70 / 40 | fail |
| 30 / 30 | fail |

---

**Exercise E6. Weekend**

Read a day number (1 = Monday, 7 = Sunday). Print `weekend` if it is Saturday (6) or Sunday (7), otherwise print `weekday`.

- **Input:** One integer (1–7).
- **Output:** `weekend` or `weekday`.

**Example:**

| Input | Output |
|-------|--------|
| 6 | weekend |
| 7 | weekend |
| 3 | weekday |

---

**Exercise E7. Not Equal to Five**

Read a number. Print `yes` if it is NOT equal to 5, otherwise print `no`.

- **Input:** One integer.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 3 | yes |
| 5 | no |
| 10 | yes |

---

### 🟡 Medium

---

**Exercise M1. Number in Range**

Read a number. Print `in range` if it is between 1 and 100 (inclusive), otherwise print `out of range`.

- **Input:** One integer.
- **Output:** `in range` or `out of range`.

**Example:**

| Input | Output |
|-------|--------|
| 50 | in range |
| 0 | out of range |
| 100 | in range |
| 101 | out of range |

---

**Exercise M2. Divisible by Both**

Read a number. Print `yes` if it is divisible by both 2 and 3, otherwise print `no`.

- **Input:** One integer.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 6 | yes |
| 4 | no |
| 9 | no |
| 12 | yes |

---

**Exercise M3. Vowel Check**

Read a single lowercase letter. Print `vowel` if it is a, e, i, o, or u, otherwise print `consonant`.

- **Input:** One lowercase letter.
- **Output:** `vowel` or `consonant`.

**Example:**

| Input | Output |
|-------|--------|
| a | vowel |
| b | consonant |
| u | vowel |

---

**Exercise M4. Valid Password**

Read a password. Print `valid` if it has at least 6 characters AND does not equal `password`, otherwise print `invalid`.

- **Input:** One string.
- **Output:** `valid` or `invalid`.

**Example:**

| Input | Output |
|-------|--------|
| hello123 | valid |
| hi | invalid |
| password | invalid |

---

**Exercise M5. Leap Year (with and/or)**

A year is a leap year if it is divisible by 4 but NOT by 100, OR divisible by 400. Use `and`, `or`, `not` to write this in one condition.

- **Input:** One integer — the year.
- **Output:** `leap year` or `not leap year`.

**Example:**

| Input | Output |
|-------|--------|
| 2024 | leap year |
| 1900 | not leap year |
| 2000 | leap year |
| 2023 | not leap year |

---

**Exercise M6. Triangle Valid (with and)**

Read three side lengths. Print `valid` if all three triangle inequality conditions are met (sum of any two sides > third side), otherwise print `invalid`. Use `and` to combine the three conditions.

- **Input:** Three integers on separate lines.
- **Output:** `valid` or `invalid`.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 4 / 5 | valid |
| 1 / 2 / 10 | invalid |

---

**Exercise M7. Grade and Attendance**

A student passes a course if their score is at least 60 AND their attendance is at least 75%. Read both values and print `pass` or `fail`.

- **Input:** Two integers — score (0–100), then attendance percentage (0–100).
- **Output:** `pass` or `fail`.

**Example:**

| Input | Output |
|-------|--------|
| 70 / 80 | pass |
| 70 / 60 | fail |
| 50 / 90 | fail |

---

### 🔴 Hard

---

**Exercise H1. Number in Range**

A game only accepts scores between 1 and 100 (inclusive). Write a program that reads a number and prints `in range` if it is valid, or `out of range` if it is not.

- **Input:** One integer.
- **Output:** `in range` or `out of range`.

**Example:**

| Input | Output |
|-------|--------|
| 50 | in range |
| 0 | out of range |
| 100 | in range |
| 150 | out of range |

**Explanation:** Use `and` to check both conditions: `n >= 1 and n <= 100`.

---

**Exercise H2. Divisible by Both 3 and 5**

A math teacher asks students to find numbers that are divisible by both 3 and 5. Write a program that reads a number and prints `yes` if it is divisible by both, or `no` otherwise.

- **Input:** One integer.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 15 | yes |
| 9 | no |
| 10 | no |
| 30 | yes |

**Explanation:** A number divisible by both 3 and 5 is also divisible by 15. You can check `n % 3 == 0 and n % 5 == 0`, or simply `n % 15 == 0`.

---

**Exercise H3. Vowel Check**

An English teacher wants a program to check if a letter is a vowel. Write a program that reads a single lowercase letter and prints `vowel` if it is a, e, i, o, or u, otherwise prints `consonant`.

- **Input:** One lowercase letter.
- **Output:** `vowel` or `consonant`.

**Example:**

| Input | Output |
|-------|--------|
| a | vowel |
| e | vowel |
| b | consonant |
| z | consonant |

**Explanation:** Use `or` to check all five vowels: `letter == "a" or letter == "e" or ...`

---

**Exercise H4. Right Triangle**

In a right triangle, the square of the longest side (hypotenuse) equals the sum of the squares of the other two sides: a² + b² = c².

Write a program that reads three side lengths (where c is the largest) and prints `right triangle` if they satisfy the Pythagorean theorem, or `not a right triangle` otherwise.

- **Input:** Three integers on separate lines — a, b, c (where c is the largest side).
- **Output:** `right triangle` or `not a right triangle`.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 4 / 5 | right triangle |
| 5 / 12 / 13 | right triangle |
| 3 / 4 / 6 | not a right triangle |

**Explanation:** Check if `a * a + b * b == c * c`.

---

**Exercise H5. Login Check**

A school computer system requires a username and password. The correct credentials are: username = `admin`, password = `1234`. Write a program that reads both and prints `welcome` if both are correct, or `wrong` if either is incorrect.

- **Input:** Two lines — username, then password.
- **Output:** `welcome` or `wrong`.

**Example:**

| Input | Output |
|-------|--------|
| admin / 1234 | welcome |
| admin / 5678 | wrong |
| user / 1234 | wrong |

**Explanation:** Both conditions must be True: `username == "admin" and password == "1234"`.

---

**Exercise H6. Ticket Discount**

A museum charges 100,000 dong for adults (ages 18–60). Children (under 18) and seniors (over 60) pay half price: 50,000 dong.

Write a program that reads a person's age and prints the ticket price.

- **Input:** One integer — the age.
- **Output:** The ticket price in dong.

**Example:**

| Input | Output |
|-------|--------|
| 25 | 100000 |
| 10 | 50000 |
| 65 | 50000 |
| 18 | 100000 |
| 60 | 100000 |

**Explanation:** Use `or` to check if the person is a child OR a senior: `age < 18 or age > 60`.

---

**Exercise H7. Three Numbers — Find the Largest**

Read three numbers. Print the largest one. Use only `if`, `elif`, `else`, and `and`/`or` — no built-in `max()` function.

- **Input:** Three integers, one per line.
- **Output:** The largest number.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 7 / 5 | 7 |
| 10 / 2 / 8 | 10 |
| 4 / 4 / 4 | 4 |
| 1 / 9 / 9 | 9 |

**Explanation:** Check each number: is it greater than or equal to both others? Use `and` to combine the two comparisons.

---
