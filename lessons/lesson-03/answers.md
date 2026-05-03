# Lesson 3 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. My Info

```python
name = "An"
age = 8
city = "Ho Chi Minh City"

print(name)
print(age)
print(city)
```

### E2. Rectangle Area

```python
width = 12
height = 7
area = width * height
print(area)
```

### E3. Update a Variable

```python
score = 0
score = score + 10
score = score + 5
score = score - 3
print(score)
```

### E4. Swap

```python
a = 3
b = 9

temp = a
a = b
b = temp

print(a)
print(b)
```

### E5. Circle Perimeter

```python
pi = 3.14159
r = 5
perimeter = 2 * pi * r
print(perimeter)
```

### E6. Seconds in a Week

```python
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_week = 7

total = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_week
print(total)
```

### E7. Type Check

```python
x = 8
y = 1.75
z = "An"

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
```

---

## 🟡 Medium

### M1. Temperature Converter

```python
celsius = 100
fahrenheit = celsius * 9 / 5 + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
```

### M2. Speed, Distance, Time

```python
speed = 60
time = 2.5
distance = speed * time

print("Distance:", distance, "km")
```

### M3. Piggy Bank

```python
savings = 50000
allowance = 20000
weeks = 4

total = savings + allowance * weeks
print(total)
```

### M4. Average Score

```python
s1 = 8
s2 = 9
s3 = 7
s4 = 10
s5 = 6

average = (s1 + s2 + s3 + s4 + s5) / 5
print(average)
```

### M5. Pythagorean Check

```python
a = 3
b = 4
c = 5

print("a*a + b*b =", a*a + b*b)
print("c*c =", c*c)
```

### M6. Ticket Price

```python
adult_price = 80000
child_price = 50000
adults = 2
children = 3

total = adult_price * adults + child_price * children
print("Total:", total, "dong")
```

### M7. Body Mass Index

```python
weight = 30
height = 1.35

bmi = weight / (height * height)
print("BMI:", round(bmi, 2))
```

---

## 🔴 Hard

### H1. Buying Fruit

```python
# Buying Fruit
# A kg of apples at P1 dong/kg, B kg of oranges at P2 dong/kg.
# Pay with 500000 dong. How much change?

a = 2
p1 = 15000
b = 3
p2 = 20000

total_cost = a * p1 + b * p2
change = 500000 - total_cost
print(change)
```

**How it works:** Calculate total cost first, then subtract from 500000.

### H2. Average Speed

```python
# Average Speed
# Total time = D1/V1 + D2/V2

d1 = 120
v1 = 60
d2 = 80
v2 = 40

time = d1 / v1 + d2 / v2
print(time)
```

**How it works:** Time = distance / speed. Add the two times together.

### H3. Staircase Tiles

```python
# Staircase Tiles
# Total tiles = 1 + 2 + ... + N = N * (N + 1) / 2

n = 4  # Change this to test

total = n * (n + 1) // 2
print(total)
```

**How it works:** The sum 1 + 2 + ... + N has a famous formula: N × (N + 1) / 2. This is called the **triangular number** formula.

### H4. Savings Goal

```python
# Savings Goal
# How many full weeks to save (G - S) dong at W dong/week?

g = 500000   # goal
s = 200000   # already saved
w = 50000    # weekly savings

needed = g - s
# Ceiling division: round up if not exact
weeks = (needed + w - 1) // w
print(weeks)
```

**How it works:** `needed = g - s` is how much more she needs. Ceiling division `(needed + w - 1) // w` rounds up to the next whole week.

For example: 300000 / 50000 = 6.0 exactly → 6 weeks.
If needed = 310000: 310000 / 50000 = 6.2 → need 7 weeks. `(310000 + 49999) // 50000 = 359999 // 50000 = 7`. ✅

### H5. Paint a Wall

```python
# Paint a Wall
# How many cans to cover W * H square meters, each can covers A m²?

w = 10
h = 3
a = 8

area = w * h
# Ceiling division: round up
cans = (area + a - 1) // a
print(cans)
```

**How it works:** Same ceiling division trick as H4. `(area + a - 1) // a` always rounds up.

For 30 m² with 8 m²/can: (30 + 7) // 8 = 37 // 8 = 4. ✅

### H6. Digit Sum Divisibility

```python
# Digit Sum Divisibility

n = 123  # Change this to test

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

digit_sum = hundreds + tens + ones
remainder = digit_sum % 3

print(digit_sum)
print(remainder)
```

**How it works:** Extract digits (from Lesson 2), add them, then check divisibility with `%`.

### H7. Bouncing Ball

```python
# Bouncing Ball
# Ball dropped from H meters, bounces 3 times (each bounce = half height).

h = 100  # Change this to test

h1 = h / 2    # height after bounce 1
h2 = h1 / 2   # height after bounce 2
h3 = h2 / 2   # height after bounce 3

# Total = initial drop + 2 * each bounce height
total = h + 2 * h1 + 2 * h2 + 2 * h3
print(total)
```

**How it works:**
- Initial drop: H meters down.
- Each bounce: ball goes up then comes back down (2 × bounce height).
- Total = 100 + 2×50 + 2×25 + 2×12.5 = 100 + 100 + 50 + 25 = 275.0.

---
