# Lesson 5 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Positive or Negative

```python
n = int(input("Enter a number: "))
if n > 0:
    print("positive")
else:
    print("not positive")
```

### E2. Even or Odd

```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

### E3. Pass or Fail

```python
score = int(input("Enter score: "))
if score >= 50:
    print("pass")
else:
    print("fail")
```

### E4. Zero Check

```python
n = int(input("Enter a number: "))
if n == 0:
    print("zero")
else:
    print("not zero")
```

### E5. Adult or Child

```python
age = int(input("Enter age: "))
if age >= 18:
    print("adult")
else:
    print("child")
```

### E6. Bigger Number

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("first")
else:
    print("second")
```

### E7. Divisible by 5

```python
n = int(input("Enter a number: "))
if n % 5 == 0:
    print("yes")
else:
    print("no")
```

---

## 🟡 Medium

### M1. Maximum of Two

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a)
else:
    print(b)
```

### M2. Minimum of Two

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print(a)
else:
    print(b)
```

### M3. Temperature Check

```python
temp = int(input("Enter temperature: "))
if temp > 30:
    print("hot")
else:
    print("cool")
```

### M4. Divisible by 3

```python
n = int(input("Enter a number: "))
if n % 3 == 0:
    print("divisible")
else:
    print("not divisible")
```

### M5. Same or Different

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("same")
else:
    print("different")
```

### M6. Long or Short

```python
word = input("Enter a word: ")
if len(word) > 5:
    print("long")
else:
    print("short")
```

### M7. Profit or Loss

```python
buy = int(input("Enter buying price: "))
sell = int(input("Enter selling price: "))
if sell > buy:
    print("profit")
else:
    if sell < buy:
        print("loss")
    else:
        print("break even")
```

---

## 🔴 Hard

### H1. Ticket Price

```python
# Ticket Price
# Under 12 → 50000 dong, else → 80000 dong.

age = int(input("Enter age: "))

if age < 12:
    print(50000)
else:
    print(80000)
```

**How it works:** A simple comparison. Age strictly less than 12 gets the child price. Age 12 and above gets the adult price.

### H2. Absolute Value

```python
# Absolute Value
# If negative, multiply by -1. Otherwise keep as is.

n = int(input("Enter a number: "))

if n < 0:
    print(-n)
else:
    print(n)
```

**How it works:** `-n` flips the sign of a negative number. For example, if `n = -5`, then `-n = 5`.

### H3. Largest of Two

```python
# Largest of Two
# Print the larger of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a >= b:
    print(a)
else:
    print(b)
```

**How it works:** If `a >= b`, then `a` is the largest (or they are equal, so either is fine). Otherwise `b` is larger.

### H4. Leap Year

```python
# Leap Year
# Divisible by 4 but not 100, OR divisible by 400.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("leap year")
else:
    if year % 100 == 0:
        print("not leap year")
    else:
        if year % 4 == 0:
            print("leap year")
        else:
            print("not leap year")
```

**How it works:** Check the special cases in order:
1. Divisible by 400 → always a leap year.
2. Divisible by 100 (but not 400) → not a leap year.
3. Divisible by 4 (but not 100) → leap year.
4. Everything else → not a leap year.

### H5. Triangle Valid

```python
# Triangle Valid
# Sum of any two sides must be greater than the third.

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")
```

**How it works:** All three conditions must be true. We nest three `if` statements. (In Lesson 7 we will use `and` to write this more cleanly.)

### H6. Grade

```python
# Grade using only if/else (no elif)
# A≥90, B≥80, C≥70, D≥60, F<60

score = int(input("Enter score: "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")
```

**How it works:** Each `else` block contains another `if/else`. This is called nested if/else. It works, but it gets deeply indented — that is why `elif` (Lesson 6) exists!

### H7. Discount

```python
# Discount
# Buy 10+ items → 10% off. Otherwise full price.

price = int(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if quantity >= 10:
    total = total * 0.9

print(total)
```

**How it works:** Calculate the full total first. If the quantity is 10 or more, multiply by 0.9 (which removes 10%). Otherwise, the total stays the same.

---
