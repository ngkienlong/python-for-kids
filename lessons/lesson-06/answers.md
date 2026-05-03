# Lesson 6 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Traffic Light

```python
color = input("Enter color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
else:
    print("Go")
```

### E2. Day Type

```python
day = int(input("Enter day number (1-7): "))
if day <= 5:
    print("weekday")
else:
    print("weekend")
```

### E3. Number Sign

```python
n = int(input("Enter a number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
```

### E4. Small, Medium, Large

```python
n = int(input("Enter a number: "))
if n < 10:
    print("small")
elif n < 100:
    print("medium")
else:
    print("large")
```

### E5. Vowel or Consonant (simple)

```python
letter = input("Enter a letter: ")
if letter == "a":
    print("vowel")
elif letter == "e":
    print("vowel")
elif letter == "i":
    print("vowel")
elif letter == "o":
    print("vowel")
elif letter == "u":
    print("vowel")
else:
    print("consonant")
```

### E6. Score Message

```python
score = int(input("Enter score: "))
if score >= 90:
    print("excellent")
elif score >= 70:
    print("good")
elif score >= 50:
    print("ok")
else:
    print("poor")
```

### E7. Age Group

```python
age = int(input("Enter age: "))
if age <= 2:
    print("baby")
elif age <= 12:
    print("child")
elif age <= 17:
    print("teen")
elif age <= 64:
    print("adult")
else:
    print("senior")
```

---

## 🟡 Medium

### M1. Grade with Remarks

```python
score = int(input("Enter score: "))
if score >= 90:
    print("A")
    print("Outstanding!")
elif score >= 80:
    print("B")
    print("Well done!")
elif score >= 70:
    print("C")
    print("Good effort.")
elif score >= 60:
    print("D")
    print("Keep trying.")
else:
    print("F")
    print("Please study more.")
```

### M2. Month Name

```python
month = int(input("Enter month (1-12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
else:
    print("December")
```

### M3. Shipping Zone

```python
distance = int(input("Enter distance in km: "))
if distance <= 10:
    print("Zone A")
elif distance <= 50:
    print("Zone B")
elif distance <= 200:
    print("Zone C")
else:
    print("Zone D")
```

### M4. Rock Paper Scissors (one player)

```python
player = input("Enter your choice (rock/paper/scissors): ")
print("Computer: rock")
if player == "rock":
    print("Draw!")
elif player == "scissors":
    print("Computer wins!")
else:
    print("You win!")
```

### M5. Electricity Bill

```python
kwh = int(input("Enter kWh used: "))
if kwh <= 50:
    bill = kwh * 1500
elif kwh <= 100:
    bill = 50 * 1500 + (kwh - 50) * 2000
else:
    bill = 50 * 1500 + 50 * 2000 + (kwh - 100) * 2500
print(bill)
```

### M6. Quadrant

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
else:
    print("Quadrant 4")
```

### M7. Ticket Type

```python
age = int(input("Enter age: "))
if age < 6:
    print(0)
elif age <= 12:
    print(50000)
elif age <= 17:
    print(70000)
else:
    print(100000)
```

---

## 🔴 Hard

### H1. Grade with Elif

```python
# Grade with Elif
# A≥90, B≥80, C≥70, D≥60, F<60

score = int(input("Enter score: "))

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

**How it works:** Each `elif` is only reached if all previous conditions were False. So when we check `score >= 80`, we already know `score < 90`.

### H2. Season

```python
# Season
# Spring: 3-5, Summer: 6-8, Autumn: 9-11, Winter: 12, 1, 2

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

**How it works:** Use `or` to check multiple months for each season. Winter is the `else` case because it covers months 12, 1, and 2 — the remaining months.

### H3. Triangle Type

```python
# Triangle Type
# Equilateral: all sides equal
# Isosceles: exactly two sides equal
# Scalene: all sides different

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a == b and b == c:
    print("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("scalene")
```

**How it works:** Check equilateral first (most specific). If not equilateral, check if any two sides are equal (isosceles). Otherwise, all sides are different (scalene).

### H4. BMI Category

```python
# BMI Category
# Underweight < 18.5, Normal < 25, Overweight < 30, Obese >= 30

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

**How it works:** Calculate BMI first, then compare against the thresholds in order. Each `elif` is only reached if the previous condition was False, so the ranges are automatically correct.

### H5. FizzBuzz Single

```python
# FizzBuzz Single
# Check divisibility by 15 (both 3 and 5) FIRST!

n = int(input("Enter a number: "))

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```

**How it works:** The key insight is to check divisibility by 15 (= 3 × 5) first. If we checked `n % 3 == 0` first, then 15 would print "Fizz" instead of "FizzBuzz". Order matters!

### H6. Shipping Cost

```python
# Shipping Cost
# ≤1kg: 15000, ≤5kg: 25000, ≤10kg: 40000, >10kg: 60000

weight = float(input("Enter weight in kg: "))

if weight <= 1:
    print(15000)
elif weight <= 5:
    print(25000)
elif weight <= 10:
    print(40000)
else:
    print(60000)
```

**How it works:** Check from lightest to heaviest. Each `elif` is only reached if the weight is above the previous threshold.

### H7. Calculator with Operator

```python
# Calculator with Operator
# Read num1, operator, num2. Handle division by zero.

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Error: division by zero")
    else:
        print(num1 / num2)
else:
    print("Unknown operator")
```

**How it works:** Use `elif` to check each operator. For division, use a nested `if` to check if the divisor is zero before dividing.

---
