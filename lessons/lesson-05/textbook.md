# Lesson 5: If — Yes or No? 🔀

> **Goal:** Use `if` and `else` to make decisions in your programs based on conditions.

---

## 1. Making Decisions

Every day you make decisions: "If it is raining, take an umbrella. Otherwise, leave it at home."

Programs make decisions too! In Scratch, you used the **"if/else"** block. In Python, we use `if` and `else`.

| Scratch | Python |
|---------|--------|
| `if <condition>` block | `if condition:` |
| `else` block | `else:` |
| Diamond-shaped condition | Any expression that is True or False |

---

## 2. Comparison Operators

Before we can make decisions, we need to **compare** values. Comparison operators return `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `5 > 3` | `True` |
| `<=` | less than or equal | `5 <= 5` | `True` |
| `>=` | greater than or equal | `6 >= 5` | `True` |

```python
print(5 == 5)    # True
print(5 == 6)    # False
print(3 < 10)    # True
print(10 < 3)    # False
print(7 != 7)    # False
```

> ⚠️ **Important:** `==` (two equals signs) means "is equal to". `=` (one equals sign) means "assign a value". They are different!

---

## 3. Boolean Values: True and False

The result of a comparison is a **boolean** — either `True` or `False`. These are special values in Python (with capital first letters).

```python
x = True
y = False
print(x)          # True
print(type(x))    # <class 'bool'>

result = 10 > 5
print(result)     # True
```

---

## 4. The `if` Statement

The `if` statement runs a block of code **only if** the condition is `True`.

```python
age = 15

if age >= 18:
    print("You can vote!")
```

**Output:** (nothing — because 15 is not ≥ 18)

```python
age = 20

if age >= 18:
    print("You can vote!")
```

**Output:**
```
You can vote!
```

### The structure:

```
if condition:
    code to run if True
    more code if True
```

> 🚨 **CRITICAL: Indentation!** The code inside `if` must be indented — use **4 spaces**. Python uses indentation to know which lines belong to the `if` block. This is different from Scratch, where blocks are visually nested.

---

## 5. The `if`/`else` Statement

`else` runs when the condition is `False`.

```python
age = 15

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
```

**Output:**
```
You cannot vote yet.
```

### The structure:

```
if condition:
    code to run if True
else:
    code to run if False
```

Only **one** branch runs — either the `if` block or the `else` block, never both.

---

## 6. Indentation is Critical

```python
# CORRECT — 4 spaces of indentation
score = 85
if score >= 60:
    print("You passed!")   # 4 spaces before print
else:
    print("Try again.")    # 4 spaces before print

# WRONG — no indentation (causes IndentationError)
if score >= 60:
print("You passed!")       # ❌ Error!
```

> 💡 In Thonny, press **Tab** to indent automatically. Thonny will add 4 spaces for you.

---

## 7. Common Patterns

### Check even or odd:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Compare two numbers:

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("a is larger")
else:
    print("b is larger or equal")
```

### Pass or fail:

```python
score = int(input("Enter your score: "))

if score >= 60:
    print("Pass")
else:
    print("Fail")
```

---

## 8. `if` Without `else`

You don't always need an `else`. Sometimes you only want to do something if a condition is True, and do nothing otherwise.

```python
temperature = int(input("Temperature: "))

if temperature > 35:
    print("Warning: very hot today!")

print("Have a nice day!")   # This always runs
```

---

## 9. Common Mistakes

```python
# Mistake 1: Using = instead of ==
if x = 5:       # ❌ SyntaxError! Use == for comparison
    print("yes")

# Mistake 2: Forgetting the colon :
if x > 5        # ❌ SyntaxError! Need : at the end
    print("yes")

# Mistake 3: Wrong indentation
if x > 5:
print("yes")    # ❌ IndentationError!

# Correct:
if x > 5:
    print("yes")   # ✅ 4 spaces
```

---

## 10. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| condition | điều kiện | An expression that is True or False |
| boolean | kiểu logic | A value that is either True or False |
| True | đúng | The boolean value for "yes" |
| False | sai | The boolean value for "no" |
| comparison | so sánh | Checking if values are equal, greater, etc. |
| indentation | thụt lề | Spaces at the start of a line to show a block |
| block | khối lệnh | A group of lines that belong together |
| branch | nhánh | One path of an if/else decision |
| equal | bằng | Having the same value (`==`) |
| not equal | không bằng | Having different values (`!=`) |
| greater than | lớn hơn | One value is bigger (`>`) |
| less than | nhỏ hơn | One value is smaller (`<`) |

---

## 11. Summary

✅ Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) return `True` or `False`.
✅ `if condition:` runs the indented block only when the condition is `True`.
✅ `else:` runs when the condition is `False`.
✅ **Indentation (4 spaces) is required** — Python uses it to define blocks.
✅ `=` assigns a value. `==` compares two values.
✅ You can use `if` without `else` if you only need to act on the True case.

---

## 12. Homework

### 🟢 Easy

---

**Exercise E1. Positive or Negative**

Read a number. Print `positive` if it is greater than 0, otherwise print `not positive`.

- **Input:** One integer.
- **Output:** `positive` or `not positive`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | positive |
| -3 | not positive |
| 0 | not positive |

---

**Exercise E2. Even or Odd**

Read a whole number. Print `even` if it is divisible by 2, otherwise print `odd`.

- **Input:** One integer.
- **Output:** `even` or `odd`.

**Example:**

| Input | Output |
|-------|--------|
| 4 | even |
| 7 | odd |
| 0 | even |

---

**Exercise E3. Pass or Fail**

Read a score (0–100). Print `pass` if the score is 50 or above, otherwise print `fail`.

- **Input:** One integer (0 ≤ score ≤ 100).
- **Output:** `pass` or `fail`.

**Example:**

| Input | Output |
|-------|--------|
| 75 | pass |
| 49 | fail |
| 50 | pass |

---

**Exercise E4. Zero Check**

Read a number. Print `zero` if it equals 0, otherwise print `not zero`.

- **Input:** One integer.
- **Output:** `zero` or `not zero`.

**Example:**

| Input | Output |
|-------|--------|
| 0 | zero |
| 5 | not zero |
| -1 | not zero |

---

**Exercise E5. Adult or Child**

Read an age. Print `adult` if the age is 18 or more, otherwise print `child`.

- **Input:** One integer.
- **Output:** `adult` or `child`.

**Example:**

| Input | Output |
|-------|--------|
| 20 | adult |
| 10 | child |
| 18 | adult |

---

**Exercise E6. Bigger Number**

Read two numbers. Print `first` if the first number is greater than the second, otherwise print `second`.

- **Input:** Two integers, one per line.
- **Output:** `first` or `second`.

**Example:**

| Input | Output |
|-------|--------|
| 8 / 3 | first |
| 2 / 9 | second |
| 5 / 5 | second |

---

**Exercise E7. Divisible by 5**

Read a number. Print `yes` if it is divisible by 5, otherwise print `no`.

- **Input:** One integer.
- **Output:** `yes` or `no`.

**Example:**

| Input | Output |
|-------|--------|
| 10 | yes |
| 7 | no |
| 25 | yes |

---

### 🟡 Medium

---

**Exercise M1. Maximum of Two**

Read two numbers. Print the larger one. If they are equal, print either one.

- **Input:** Two integers, one per line.
- **Output:** The larger number.

**Example:**

| Input | Output |
|-------|--------|
| 7 / 3 | 7 |
| 4 / 9 | 9 |
| 5 / 5 | 5 |

---

**Exercise M2. Minimum of Two**

Read two numbers. Print the smaller one.

- **Input:** Two integers, one per line.
- **Output:** The smaller number.

**Example:**

| Input | Output |
|-------|--------|
| 7 / 3 | 3 |
| 4 / 9 | 4 |

---

**Exercise M3. Temperature Check**

Read a temperature in Celsius. Print `hot` if it is above 30, otherwise print `cool`.

- **Input:** One integer.
- **Output:** `hot` or `cool`.

**Example:**

| Input | Output |
|-------|--------|
| 35 | hot |
| 20 | cool |
| 30 | cool |

---

**Exercise M4. Divisible by 3**

Read a number. Print `divisible` if it is divisible by 3, otherwise print `not divisible`.

- **Input:** One integer.
- **Output:** `divisible` or `not divisible`.

**Example:**

| Input | Output |
|-------|--------|
| 9 | divisible |
| 10 | not divisible |
| 0 | divisible |

---

**Exercise M5. Same or Different**

Read two numbers. Print `same` if they are equal, otherwise print `different`.

- **Input:** Two integers, one per line.
- **Output:** `same` or `different`.

**Example:**

| Input | Output |
|-------|--------|
| 5 / 5 | same |
| 3 / 7 | different |

---

**Exercise M6. Long or Short**

Read a word (string). Print `long` if it has more than 5 characters, otherwise print `short`.

- **Input:** One word (no spaces).
- **Output:** `long` or `short`.

**Example:**

| Input | Output |
|-------|--------|
| python | long |
| cat | short |
| hello | short |

(Hint: Use `len(word)` to get the number of characters.)

---

**Exercise M7. Profit or Loss**

Read the buying price and selling price of an item. Print `profit` if the selling price is higher, `loss` if lower, or `break even` if they are equal.

- **Input:** Two integers — buying price, then selling price.
- **Output:** `profit`, `loss`, or `break even`.

**Example:**

| Input | Output |
|-------|--------|
| 100 / 150 | profit |
| 200 / 180 | loss |
| 100 / 100 | break even |

---

### 🔴 Hard

---

**Exercise H1. Ticket Price**

A cinema has two ticket prices: children under 12 years old pay **50,000 dong**, and everyone else pays **80,000 dong**. Write a program that reads a person's age and prints the ticket price they must pay.

- **Input:** One integer — the person's age (1 ≤ age ≤ 100).
- **Output:** One integer — the ticket price in dong.

**Example:**

| Input | Output |
|-------|--------|
| 8 | 50000 |
| 15 | 80000 |
| 12 | 80000 |

**Explanation:** Age 8 < 12, so the child pays 50,000. Age 15 ≥ 12, so the person pays 80,000. Age 12 is not less than 12, so they pay 80,000.

---

**Exercise H2. Absolute Value**

In mathematics, the absolute value of a number is its distance from zero — always positive. For example, |−5| = 5 and |3| = 3.

Write a program that reads a number and prints its absolute value **without using the built-in `abs()` function**.

- **Input:** One integer (−1000 ≤ n ≤ 1000).
- **Output:** The absolute value.

**Example:**

| Input | Output |
|-------|--------|
| -5 | 5 |
| 3 | 3 |
| 0 | 0 |

**Explanation:** If the number is negative, multiply by −1 to make it positive. If it is already 0 or positive, print it as is.

---

**Exercise H3. Largest of Two**

Read two numbers. Print the larger one. If they are equal, print that number.

- **Input:** Two integers, one per line.
- **Output:** The larger number.

**Example:**

| Input | Output |
|-------|--------|
| 10 / 7 | 10 |
| 3 / 8 | 8 |
| 6 / 6 | 6 |

**Explanation:** Compare the two numbers. The larger one wins. If equal, either one is fine.

---

**Exercise H4. Leap Year**

A year is a **leap year** if it is divisible by 4 but NOT divisible by 100, OR if it is divisible by 400. Leap years have 366 days instead of 365.

Write a program that reads a year and prints `leap year` or `not leap year`.

- **Input:** One integer — the year (1 ≤ year ≤ 9999).
- **Output:** `leap year` or `not leap year`.

**Example:**

| Input | Output |
|-------|--------|
| 2024 | leap year |
| 2023 | not leap year |
| 1900 | not leap year |
| 2000 | leap year |

**Explanation:** 2024 ÷ 4 = 506 (divisible by 4) and 2024 ÷ 100 = 20.24 (not divisible by 100) → leap year. 1900 ÷ 100 = 19 (divisible by 100) but 1900 ÷ 400 = 4.75 (not divisible by 400) → not a leap year.

(Hint: Use `if/else` with `%`. You may need to think carefully about the logic. You can use `and`/`or` — we will study them properly in Lesson 7, but you can try them here!)

---

**Exercise H5. Triangle Valid**

Three sticks have lengths A, B, and C. They can form a triangle only if the sum of any two sides is **greater than** the third side. This must be true for all three combinations.

Write a program that reads three side lengths and prints `valid` or `invalid`.

- **Input:** Three integers on separate lines — A, B, C (1 ≤ A, B, C ≤ 1000).
- **Output:** `valid` or `invalid`.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 4 / 5 | valid |
| 1 / 2 / 10 | invalid |
| 5 / 5 / 5 | valid |

**Explanation:** For 3, 4, 5: 3+4=7>5 ✅, 3+5=8>4 ✅, 4+5=9>3 ✅ → valid. For 1, 2, 10: 1+2=3 which is NOT > 10 → invalid.

---

**Exercise H6. Grade**

A teacher uses this grading scale: A for 90 and above, B for 80–89, C for 70–79, D for 60–69, F for below 60.

Write a program that reads a score and prints the grade. Use only `if` and `else` (no `elif` — that is Lesson 6!).

- **Input:** One integer — the score (0 ≤ score ≤ 100).
- **Output:** One letter — the grade.

**Example:**

| Input | Output |
|-------|--------|
| 95 | A |
| 83 | B |
| 72 | C |
| 65 | D |
| 45 | F |

(Hint: Nest `if/else` inside another `else`. It gets a bit long, but it works!)

---

**Exercise H7. Discount**

A shop gives a **10% discount** if a customer buys **10 or more** items. Otherwise, no discount. Write a program that reads the price per item and the quantity, then prints the final total price.

- **Input:** Two lines — price per item (integer), then quantity (integer).
- **Output:** The final total price (as a float or integer).

**Example:**

| Input | Output |
|-------|--------|
| 20000 / 10 | 180000.0 |
| 20000 / 5 | 100000 |
| 15000 / 12 | 162000.0 |

**Explanation:** For 10 items at 20,000 each: total = 200,000. With 10% discount: 200,000 × 0.9 = 180,000.

---
