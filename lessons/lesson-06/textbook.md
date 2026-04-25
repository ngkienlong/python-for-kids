# Lesson 6: If-Elif-Else — Many Choices 🔀🔀🔀

> **Goal:** Use `elif` to handle multiple conditions cleanly, and understand nested `if` statements.

---

## 1. The Problem with Many Choices

In Lesson 5, you learned `if/else` — two choices. But what if you have **more than two** choices?

Imagine a traffic light: it can be red, yellow, or green. With only `if/else`, you would have to nest many levels deep:

```python
# Lesson 5 style — gets messy quickly!
if color == "red":
    print("Stop")
else:
    if color == "yellow":
        print("Slow down")
    else:
        print("Go")
```

Python gives us a cleaner tool: `elif`.

---

## 2. `elif` — Else If

`elif` means "else if" — check another condition if the previous one was False.

```python
color = input("Traffic light color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
else:
    print("Go")
```

**How it works:**
1. Check `color == "red"`. If True → print "Stop", skip the rest.
2. If False → check `color == "yellow"`. If True → print "Slow down", skip the rest.
3. If False → run `else` → print "Go".

**Only ONE branch runs** — the first condition that is True.

---

## 3. The Structure

```
if condition1:
    code for condition1
elif condition2:
    code for condition2
elif condition3:
    code for condition3
else:
    code if none of the above
```

- You can have **as many `elif` as you need**.
- The `else` at the end is optional — it catches everything that didn't match.
- Python checks conditions **from top to bottom** and stops at the first True one.

---

## 4. Grade Example

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Example runs:**

| Input | Output | Why |
|-------|--------|-----|
| 95 | A | 95 ≥ 90 → first condition True |
| 83 | B | 83 < 90, but 83 ≥ 80 → second condition True |
| 55 | F | None of the conditions matched → else |

> 💡 Notice: we don't need to write `score >= 80 and score < 90` for B. Because if we reach the `elif score >= 80` check, we already know `score < 90` (otherwise the first `if` would have caught it).

---

## 5. Only One Branch Runs

This is very important! Even if multiple conditions are True, **only the first True one runs**.

```python
x = 15

if x > 10:
    print("greater than 10")   # This runs
elif x > 5:
    print("greater than 5")    # This is SKIPPED (even though 15 > 5 is True)
else:
    print("5 or less")         # This is SKIPPED
```

**Output:**
```
greater than 10
```

---

## 6. Nested `if`

You can put an `if` statement **inside** another `if` statement. This is called **nested if**.

```python
age = int(input("Enter age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18:
    if has_ticket == "yes":
        print("Welcome! Enjoy the show.")
    else:
        print("Please buy a ticket first.")
else:
    print("Sorry, this show is for adults only.")
```

The inner `if` only runs if the outer `if` is True.

---

## 7. Season Example

```python
month = int(input("Enter month (1-12): "))

if month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Winter")
```

(We will learn `and`/`or` properly in Lesson 7, but you can see how they work here.)

---

## 8. Menu Example

```python
print("=== Menu ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Choose (1-3): "))
a = float(input("Enter a: "))
b = float(input("Enter b: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
else:
    print("Invalid choice!")
```

---

## 9. Common Mistakes

```python
# Mistake 1: elif without if
elif x > 5:     # ❌ SyntaxError! elif must come after if
    print("yes")

# Mistake 2: else with a condition
else x > 5:     # ❌ SyntaxError! else never has a condition
    print("yes")

# Mistake 3: Wrong order (conditions overlap)
score = 85
if score >= 60:
    print("D")   # ❌ This prints "D" for score 85!
elif score >= 80:
    print("B")   # This never runs for 85 because the first if already caught it

# Fix: put more specific conditions first
if score >= 80:
    print("B")   # ✅ Checks 80+ first
elif score >= 60:
    print("D")
```

---

## 10. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| elif | khác nếu | "else if" — check another condition |
| chain | chuỗi | Multiple conditions linked together |
| nested | lồng nhau | An if inside another if |
| branch | nhánh | One path of a multi-way decision |
| condition | điều kiện | An expression that is True or False |
| multiple | nhiều | More than two choices |
| fall-through | rơi xuống | When no condition matches, goes to else |
| default | mặc định | The else case — what happens if nothing matches |

---

## 11. Summary

✅ `elif` lets you check multiple conditions in sequence.
✅ Only the **first True** branch runs — the rest are skipped.
✅ `else` at the end catches everything that didn't match any condition.
✅ Put **more specific** conditions first, **more general** ones later.
✅ Nested `if` = an `if` inside another `if`.
✅ `elif` is cleaner than deeply nested `if/else`.

---

## 12. Homework

### 🟢 Easy

---

**Exercise E1. Traffic Light**

Read a traffic light color (`red`, `yellow`, or `green`). Print the instruction.

- **Input:** One word — the color.
- **Output:** The instruction.

**Example:**

| Input | Output |
|-------|--------|
| red | Stop |
| yellow | Slow down |
| green | Go |

---

**Exercise E2. Day Type**

Read a day number (1 = Monday, 7 = Sunday). Print `weekday` for days 1–5, `weekend` for days 6–7.

- **Input:** One integer (1–7).
- **Output:** `weekday` or `weekend`.

**Example:**

| Input | Output |
|-------|--------|
| 3 | weekday |
| 6 | weekend |
| 7 | weekend |

---

**Exercise E3. Number Sign**

Read a number. Print `positive`, `negative`, or `zero`.

- **Input:** One integer.
- **Output:** `positive`, `negative`, or `zero`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | positive |
| -3 | negative |
| 0 | zero |

---

**Exercise E4. Small, Medium, Large**

Read a number. Print `small` if less than 10, `medium` if 10–99, `large` if 100 or more.

- **Input:** One integer.
- **Output:** `small`, `medium`, or `large`.

**Example:**

| Input | Output |
|-------|--------|
| 5 | small |
| 50 | medium |
| 200 | large |

---

**Exercise E5. Vowel or Consonant (simple)**

Read a single lowercase letter. Print `vowel` if it is `a`, `e`, `i`, `o`, or `u`, otherwise print `consonant`.

- **Input:** One lowercase letter.
- **Output:** `vowel` or `consonant`.

**Example:**

| Input | Output |
|-------|--------|
| a | vowel |
| b | consonant |
| i | vowel |

---

**Exercise E6. Score Message**

Read a score. Print `excellent` if ≥ 90, `good` if ≥ 70, `ok` if ≥ 50, `poor` if below 50.

- **Input:** One integer (0–100).
- **Output:** `excellent`, `good`, `ok`, or `poor`.

**Example:**

| Input | Output |
|-------|--------|
| 95 | excellent |
| 75 | good |
| 55 | ok |
| 30 | poor |

---

**Exercise E7. Age Group**

Read an age. Print `baby` (0–2), `child` (3–12), `teen` (13–17), `adult` (18–64), `senior` (65+).

- **Input:** One integer (0–120).
- **Output:** The age group.

**Example:**

| Input | Output |
|-------|--------|
| 1 | baby |
| 8 | child |
| 15 | teen |
| 30 | adult |
| 70 | senior |

---

### 🟡 Medium

---

**Exercise M1. Grade with Remarks**

Read a score. Print the grade (A/B/C/D/F) AND a remark on the next line.

- **Input:** One integer (0–100).
- **Output:** Two lines — grade, then remark.

**Remarks:** A → "Outstanding!", B → "Well done!", C → "Good effort.", D → "Keep trying.", F → "Please study more."

**Example:**

| Input | Output |
|-------|--------|
| 92 | A |
| | Outstanding! |
| 75 | C |
| | Good effort. |

---

**Exercise M2. Month Name**

Read a month number (1–12). Print the month name.

- **Input:** One integer (1–12).
- **Output:** The month name.

**Example:**

| Input | Output |
|-------|--------|
| 1 | January |
| 7 | July |
| 12 | December |

---

**Exercise M3. Shipping Zone**

Read a distance in km. Print the shipping zone: Zone A (≤ 10 km), Zone B (≤ 50 km), Zone C (≤ 200 km), Zone D (> 200 km).

- **Input:** One integer — distance in km.
- **Output:** The zone.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Zone A |
| 30 | Zone B |
| 100 | Zone C |
| 500 | Zone D |

---

**Exercise M4. Rock Paper Scissors (one player)**

Read a choice (`rock`, `paper`, or `scissors`). Print the computer's choice (always `rock`) and who wins.

- **Input:** One word.
- **Output:** Two lines — computer's choice, then result.

**Example:**

| Input | Output |
|-------|--------|
| rock | Computer: rock |
| | Draw! |
| scissors | Computer: rock |
| | Computer wins! |
| paper | Computer: rock |
| | You win! |

---

**Exercise M5. Electricity Bill**

Read the number of kWh used. Calculate the bill:
- First 50 kWh: 1,500 dong/kWh
- Next 50 kWh (51–100): 2,000 dong/kWh
- Above 100 kWh: 2,500 dong/kWh

- **Input:** One integer — kWh used.
- **Output:** Total bill in dong.

**Example:**

| Input | Output |
|-------|--------|
| 30 | 45000 |
| 80 | 135000 |
| 120 | 225000 |

---

**Exercise M6. Quadrant**

Read two integers x and y (neither is 0). Print which quadrant the point (x, y) is in.

- **Input:** Two integers — x, then y.
- **Output:** `Quadrant 1`, `Quadrant 2`, `Quadrant 3`, or `Quadrant 4`.

(Quadrant 1: x>0, y>0. Quadrant 2: x<0, y>0. Quadrant 3: x<0, y<0. Quadrant 4: x>0, y<0.)

**Example:**

| Input | Output |
|-------|--------|
| 3 / 5 | Quadrant 1 |
| -2 / 4 | Quadrant 2 |
| -1 / -3 | Quadrant 3 |
| 5 / -2 | Quadrant 4 |

---

**Exercise M7. Ticket Type**

A theme park has three ticket types: child (under 6) is free, child (6–12) costs 50,000, teen (13–17) costs 70,000, adult (18+) costs 100,000.

- **Input:** One integer — age.
- **Output:** The ticket price.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 0 |
| 8 | 50000 |
| 15 | 70000 |
| 25 | 100000 |

---

### 🔴 Hard

---

**Exercise H1. Grade with Elif**

A school uses this grading scale: A (90–100), B (80–89), C (70–79), D (60–69), F (0–59). Write a program using `elif` to print the correct grade.

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

---

**Exercise H2. Season**

The four seasons in the Northern Hemisphere are: Spring (March–May), Summer (June–August), Autumn (September–November), Winter (December, January, February).

Write a program that reads a month number and prints the season.

- **Input:** One integer — the month (1 ≤ month ≤ 12).
- **Output:** The season name.

**Example:**

| Input | Output |
|-------|--------|
| 4 | Spring |
| 7 | Summer |
| 10 | Autumn |
| 1 | Winter |
| 12 | Winter |

---

**Exercise H3. Triangle Type**

Given three side lengths, a triangle can be:
- **Equilateral**: all three sides are equal.
- **Isosceles**: exactly two sides are equal.
- **Scalene**: all three sides are different.

Write a program that reads three side lengths and prints the triangle type.

- **Input:** Three integers on separate lines — A, B, C (1 ≤ A, B, C ≤ 1000).
- **Output:** `equilateral`, `isosceles`, or `scalene`.

**Example:**

| Input | Output |
|-------|--------|
| 5 / 5 / 5 | equilateral |
| 3 / 3 / 5 | isosceles |
| 3 / 4 / 5 | scalene |

---

**Exercise H4. BMI Category**

A doctor uses BMI to classify patients. BMI = weight (kg) ÷ (height (m))².

Categories:
- Underweight: BMI < 18.5
- Normal: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obese: BMI ≥ 30

Write a program that reads weight and height, then prints the BMI category.

- **Input:** Two lines — weight in kg (float), then height in meters (float).
- **Output:** The BMI category.

**Example:**

| Input | Output |
|-------|--------|
| 40 / 1.60 | Underweight |
| 65 / 1.70 | Normal |
| 80 / 1.65 | Overweight |
| 100 / 1.70 | Obese |

---

**Exercise H5. FizzBuzz Single**

FizzBuzz is a classic programming puzzle. For a single number:
- If divisible by both 3 and 5 → print `FizzBuzz`
- If divisible by 3 only → print `Fizz`
- If divisible by 5 only → print `Buzz`
- Otherwise → print the number itself

Write a program that reads one number and prints the correct output.

- **Input:** One integer.
- **Output:** `FizzBuzz`, `Fizz`, `Buzz`, or the number.

**Example:**

| Input | Output |
|-------|--------|
| 15 | FizzBuzz |
| 9 | Fizz |
| 10 | Buzz |
| 7 | 7 |

---

**Exercise H6. Shipping Cost**

A delivery company charges based on package weight:
- Up to 1 kg: 15,000 dong
- Up to 5 kg: 25,000 dong
- Up to 10 kg: 40,000 dong
- Over 10 kg: 60,000 dong

Write a program that reads the weight and prints the shipping cost.

- **Input:** One float — weight in kg.
- **Output:** The shipping cost in dong.

**Example:**

| Input | Output |
|-------|--------|
| 0.5 | 15000 |
| 3 | 25000 |
| 8 | 40000 |
| 15 | 60000 |

---

**Exercise H7. Calculator with Operator**

Write a calculator that reads two numbers and an operator, then prints the result. Handle division by zero by printing `Error: division by zero`.

- **Input:** Three lines — first number (float), operator (`+`, `-`, `*`, `/`), second number (float).
- **Output:** The result, or an error message.

**Example:**

| Input | Output |
|-------|--------|
| 10 / + / 5 | 15.0 |
| 10 / - / 3 | 7.0 |
| 6 / * / 7 | 42.0 |
| 10 / / / 2 | 5.0 |
| 10 / / / 0 | Error: division by zero |

---
