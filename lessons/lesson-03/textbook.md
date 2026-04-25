# Lesson 3: Variables — Boxes with Names 📦

> **Goal:** Create variables to store values, update them, and use them in calculations.

---

## 1. What is a Variable?

Imagine a **box** with a label on it. You can put a number (or text) inside the box, and use the label to get it back later.

In Python, a **variable** is a named box that stores a value.

> 💡 **Scratch connection:** Variables in Python work exactly like **"Make a Variable"** in Scratch!

| Scratch | Python |
|---------|--------|
| Make a variable called `score` | `score = 0` |
| Set `score` to 10 | `score = 10` |
| Change `score` by 1 | `score = score + 1` |
| Say `score` | `print(score)` |

---

## 2. Creating a Variable

Use the `=` sign to create a variable and give it a value.

```python
age = 8
name = "An"
score = 100
```

- `age` is a variable that stores the number `8`.
- `name` is a variable that stores the text `"An"`.
- `score` is a variable that stores the number `100`.

The `=` sign means **"store this value"**, not "equals" like in math!

---

## 3. Using a Variable

Once you create a variable, you can use it anywhere:

```python
age = 8
print(age)          # prints: 8
print("I am", age, "years old")  # prints: I am 8 years old
print(age + 2)      # prints: 10
```

**Output:**
```
8
I am 8 years old
10
```

---

## 4. Updating a Variable

You can change the value stored in a variable:

```python
score = 0
print(score)    # 0

score = 10
print(score)    # 10

score = score + 5   # take the old value, add 5, store back
print(score)    # 15
```

> 💡 `score = score + 5` means: "take the current value of `score`, add 5, and store the result back into `score`."

---

## 5. Variable Naming Rules

| Rule | Good ✅ | Bad ❌ |
|------|---------|--------|
| Use letters, numbers, underscore `_` | `my_score`, `player1` | `my score`, `player-1` |
| Cannot start with a number | `score1` | `1score` |
| Case-sensitive | `score` ≠ `Score` | — |
| No spaces | `high_score` | `high score` |
| Use English words | `total_price` | — |

**Good variable names:**
```python
player_name = "An"
total_score = 0
number_of_apples = 5
side_length = 10
```

**Bad variable names (will cause errors):**
```python
1player = "An"      # starts with a number
my score = 0        # has a space
total-score = 0     # has a hyphen
```

---

## 6. Multiple Variables

You can create as many variables as you need:

```python
# Rectangle dimensions
width = 15
height = 8

# Calculate area and perimeter
area = width * height
perimeter = 2 * width + 2 * height

print("Width:", width)
print("Height:", height)
print("Area:", area)
print("Perimeter:", perimeter)
```

**Output:**
```
Width: 15
Height: 8
Area: 120
Perimeter: 46
```

This is much cleaner than writing `print("Area:", 15 * 8)` — if you change the width, you only need to change it in one place!

---

## 7. Swapping Two Variables

What if you want to swap the values of two variables?

```python
a = 5
b = 10

print("Before:", a, b)   # Before: 5 10

# Swap using a temporary variable
temp = a
a = b
b = temp

print("After:", a, b)    # After: 10 5
```

> 💡 Python also has a shortcut for swapping:
> ```python
> a, b = b, a
> ```

---

## 8. Variable Types

Variables can store different types of values:

| Type | Example | Vietnamese |
|------|---------|-----------|
| `int` | `age = 8` | Số nguyên |
| `float` | `height = 1.35` | Số thực |
| `str` | `name = "An"` | Chuỗi ký tự |

```python
age = 8           # int
height = 1.35     # float
name = "An"       # str (string)

print(age)        # 8
print(height)     # 1.35
print(name)       # An
```

You can check the type of a variable with `type()`:

```python
print(type(8))        # <class 'int'>
print(type(1.35))     # <class 'float'>
print(type("An"))     # <class 'str'>
```

---

## 9. Common Mistakes

```python
# Mistake 1: Using a variable before creating it
print(x)        # NameError! x does not exist yet

# Mistake 2: Wrong direction of =
8 = age         # SyntaxError! Left side must be the variable name

# Mistake 3: Forgetting quotes for strings
name = An       # NameError! Python thinks "An" is a variable name
name = "An"     # ✅ Correct
```

---

## 10. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| variable | biến | A named box that stores a value |
| assign | gán | Give a value to a variable (`=`) |
| value | giá trị | The data stored in a variable |
| update | cập nhật | Change the value of a variable |
| store | lưu trữ | Save a value in a variable |
| type | kiểu dữ liệu | The kind of data (int, float, str) |
| string | chuỗi | Text data, written in quotes |
| swap | hoán đổi | Exchange the values of two variables |
| temporary | tạm thời | Used for a short time, then discarded |
| naming convention | quy tắc đặt tên | Rules for how to name variables |

---

## 11. Summary

✅ A variable is a named box that stores a value.
✅ Use `=` to create or update a variable.
✅ Variable names use letters, numbers, and `_`. No spaces. Start with a letter.
✅ You can use a variable in math: `score = score + 10`.
✅ Variables make code easier to read and change.
✅ Types: `int` (whole number), `float` (decimal), `str` (text).

---

## 12. Homework

### 🟢 Easy

---

**Exercise E1. My Info**

Create 3 variables: `name`, `age`, `city`. Assign your own values. Print them.

- **Input:** None.
- **Output:** (example)
```
An
8
Ho Chi Minh City
```

---

**Exercise E2. Rectangle Area**

Create two variables `width = 12` and `height = 7`. Calculate and print the area.

- **Input:** None.
- **Output:**
```
84
```

---

**Exercise E3. Update a Variable**

Start with `score = 0`. Add 10, then add 5, then subtract 3. Print the final score.

- **Input:** None.
- **Output:**
```
12
```

---

**Exercise E4. Swap**

Create `a = 3` and `b = 9`. Swap their values. Print `a` and `b` after the swap.

- **Input:** None.
- **Output:**
```
9
3
```

---

**Exercise E5. Circle Perimeter**

The perimeter of a circle is `C = 2 * pi * r`. Use `pi = 3.14159` and `r = 5`. Print the perimeter.

- **Input:** None.
- **Output:**
```
31.4159
```

---

**Exercise E6. Seconds in a Week**

Use variables to calculate how many seconds are in one week. Store each step in a variable.

- **Input:** None.
- **Output:**
```
604800
```

(Hint: `seconds_per_minute = 60`, `minutes_per_hour = 60`, `hours_per_day = 24`, `days_per_week = 7`.)

---

**Exercise E7. Type Check**

Create one variable of each type: `int`, `float`, `str`. Print each variable and its type.

- **Input:** None.
- **Output:** (example)
```
8
<class 'int'>
1.75
<class 'float'>
An
<class 'str'>
```

---

### 🟡 Medium

---

**Exercise M1. Temperature Converter**

Store the temperature in Celsius in a variable `celsius = 100`. Convert it to Fahrenheit using the formula `F = C * 9 / 5 + 32`. Print both values with labels.

- **Input:** None.
- **Output:**
```
Celsius: 100
Fahrenheit: 212.0
```

---

**Exercise M2. Speed, Distance, Time**

A car travels at `speed = 60` km/h for `time = 2.5` hours. Calculate the distance and print it.

- **Input:** None.
- **Output:**
```
Distance: 150.0 km
```

---

**Exercise M3. Piggy Bank**

You have `savings = 50000` dong. You earn `allowance = 20000` dong per week. After 4 weeks, how much do you have? Print the result.

- **Input:** None.
- **Output:**
```
130000
```

---

**Exercise M4. Average Score**

Store 5 test scores in 5 variables: `s1 = 8`, `s2 = 9`, `s3 = 7`, `s4 = 10`, `s5 = 6`. Calculate and print the average.

- **Input:** None.
- **Output:**
```
8.0
```

---

**Exercise M5. Pythagorean Check**

Store `a = 3`, `b = 4`, `c = 5`. Calculate `a*a + b*b` and `c*c`. Print both. Are they equal?

- **Input:** None.
- **Output:**
```
a*a + b*b = 25
c*c = 25
```

---

**Exercise M6. Ticket Price**

An adult ticket costs `adult_price = 80000` dong. A child ticket costs `child_price = 50000` dong. A family buys `adults = 2` adult tickets and `children = 3` child tickets. Print the total cost.

- **Input:** None.
- **Output:**
```
Total: 310000 dong
```

---

**Exercise M7. Body Mass Index**

BMI = weight (kg) / (height (m) × height (m)).

Store `weight = 30` and `height = 1.35`. Calculate and print the BMI (rounded to 2 decimal places is fine).

- **Input:** None.
- **Output:**
```
BMI: 16.46
```

(Hint: `print("BMI:", round(bmi, 2))`)

---

### 🔴 Hard

---

**Exercise H1. Buying Fruit**

Minh goes to the market. He buys **A** kg of apples at **P1** dong/kg and **B** kg of oranges at **P2** dong/kg. He pays with a **500000-dong** note. How much change does he get?

- **Input:** Four integers on one line: A P1 B P2 (1 ≤ A, B ≤ 10, 1000 ≤ P1, P2 ≤ 50000).
- **Output:** One integer — the change in dong.

**Example:**

| Input | Output |
|-------|--------|
| 2 15000 3 20000 | 410000 |
| 1 50000 1 50000 | 400000 |

**Explanation:** 2 × 15000 + 3 × 20000 = 30000 + 60000 = 90000. Change = 500000 - 90000 = 410000.

(Hint: Set `a = 2`, `p1 = 15000`, `b = 3`, `p2 = 20000` in your code.)

---

**Exercise H2. Average Speed**

A car travels from city A to city B. The first half of the trip (distance **D1** km) is at speed **V1** km/h. The second half (distance **D2** km) is at speed **V2** km/h.

Calculate the **total time** (in hours) for the whole trip.

- **Input:** Four numbers: D1 V1 D2 V2 (1 ≤ D1, D2 ≤ 1000, 1 ≤ V1, V2 ≤ 200).
- **Output:** The total time in hours (as a decimal).

**Example:**

| Input | Output |
|-------|--------|
| 120 60 80 40 | 4.0 |
| 100 50 100 100 | 3.0 |

**Explanation:** Time = distance / speed. Total time = D1/V1 + D2/V2. For example 1: 120/60 + 80/40 = 2 + 2 = 4.0 hours.

(Hint: `time = d1 / v1 + d2 / v2`.)

---

**Exercise H3. Staircase Tiles**

A staircase has **N** steps. Step 1 has 1 tile, step 2 has 2 tiles, ..., step N has N tiles. How many tiles are needed in total?

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One integer — the total number of tiles.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 10 |
| 1 | 1 |
| 10 | 55 |

**Explanation:** For N = 4: 1 + 2 + 3 + 4 = 10. The formula is N × (N + 1) / 2.

(Hint: Use the formula `total = n * (n + 1) // 2`. Set `n = 4` in your code.)

---

**Exercise H4. Savings Goal**

Lan wants to save money to buy a bicycle that costs **G** dong. She already has **S** dong saved. She saves **W** dong every week. How many **full weeks** does she need to save the rest?

- **Input:** Three integers: G S W (1 ≤ S < G ≤ 1000000, 1 ≤ W ≤ 100000).
- **Output:** One integer — the number of full weeks needed.

**Example:**

| Input | Output |
|-------|--------|
| 500000 200000 50000 | 6 |
| 100000 10000 30000 | 3 |

**Explanation:** Lan needs 500000 - 200000 = 300000 more dong. At 50000/week: 300000 / 50000 = 6 weeks.

(Hint: `weeks = (g - s + w - 1) // w` — this rounds up. Or think: `needed = g - s`, then `weeks = needed // w` if it divides evenly, else `weeks = needed // w + 1`.)

---

**Exercise H5. Paint a Wall**

A rectangular wall is **W** meters wide and **H** meters tall. One can of paint covers **A** square meters. How many **full cans** of paint are needed to paint the whole wall?

- **Input:** Three integers: W H A (1 ≤ W, H ≤ 100, 1 ≤ A ≤ 500).
- **Output:** One integer — the number of cans needed (round up if not exact).

**Example:**

| Input | Output |
|-------|--------|
| 10 3 8 | 4 |
| 5 4 10 | 2 |
| 6 6 9 | 4 |

**Explanation:** For 10 × 3 = 30 m². Each can covers 8 m². 30 / 8 = 3.75 → need 4 cans (round up).

(Hint: `cans = (w * h + a - 1) // a` — this is the ceiling division trick.)

---

**Exercise H6. Digit Sum Divisibility**

Given a **3-digit** number N, check if the **sum of its digits** is divisible by 3. Print the digit sum and the remainder when divided by 3.

- **Input:** One integer N (100 ≤ N ≤ 999).
- **Output:** Two lines: the digit sum, then the remainder when divided by 3.

**Example:**

| Input | Output |
|-------|--------|
| 123 | 6 |
| | 0 |
| 456 | 15 |
| | 0 |
| 124 | 7 |
| | 1 |

**Explanation:** For 123: 1 + 2 + 3 = 6. 6 % 3 = 0 (divisible by 3). For 124: 1 + 2 + 4 = 7. 7 % 3 = 1 (not divisible).

(Hint: Extract digits using `//` and `%` from Lesson 2, then add them.)

---

**Exercise H7. Bouncing Ball**

A ball is dropped from a height of **H** meters. Each time it bounces, it reaches **half** the previous height. What is the total distance the ball has traveled after **3 bounces** (3 ups + 3 downs + the initial drop)?

- **Input:** One integer H (1 ≤ H ≤ 1000).
- **Output:** The total distance as a decimal number.

**Example:**

| Input | Output |
|-------|--------|
| 100 | 275.0 |
| 8 | 22.0 |

**Explanation:** For H = 100:
- Drop: 100 m down.
- Bounce 1: 50 m up + 50 m down.
- Bounce 2: 25 m up + 25 m down.
- Bounce 3: 12.5 m up + 12.5 m down.
- Total = 100 + 50 + 50 + 25 + 25 + 12.5 + 12.5 = 275.0 m.

(Hint: Use variables `h1 = H / 2`, `h2 = h1 / 2`, `h3 = h2 / 2`. Total = H + 2*h1 + 2*h2 + 2*h3.)

---
