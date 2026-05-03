# Lesson 7 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Both Positive

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > 0 and b > 0:
    print("yes")
else:
    print("no")
```

### E2. Either Zero

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == 0 or b == 0:
    print("yes")
else:
    print("no")
```

### E3. Not Negative

```python
n = int(input("Enter a number: "))
if not (n < 0):
    print("yes")
else:
    print("no")
```

### E4. Teen

```python
age = int(input("Enter age: "))
if age >= 13 and age <= 19:
    print("teen")
else:
    print("not teen")
```

### E5. Pass Both

```python
s1 = int(input("Enter first score: "))
s2 = int(input("Enter second score: "))
if s1 >= 50 and s2 >= 50:
    print("pass")
else:
    print("fail")
```

### E6. Weekend

```python
day = int(input("Enter day number (1-7): "))
if day == 6 or day == 7:
    print("weekend")
else:
    print("weekday")
```

### E7. Not Equal to Five

```python
n = int(input("Enter a number: "))
if n != 5:
    print("yes")
else:
    print("no")
```

---

## 🟡 Medium

### M1. Number in Range

```python
n = int(input("Enter a number: "))
if n >= 1 and n <= 100:
    print("in range")
else:
    print("out of range")
```

### M2. Divisible by Both

```python
n = int(input("Enter a number: "))
if n % 2 == 0 and n % 3 == 0:
    print("yes")
else:
    print("no")
```

### M3. Vowel Check

```python
letter = input("Enter a letter: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("vowel")
else:
    print("consonant")
```

### M4. Valid Password

```python
password = input("Enter password: ")
if len(password) >= 6 and password != "password":
    print("valid")
else:
    print("invalid")
```

### M5. Leap Year (with and/or)

```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")
```

### M6. Triangle Valid (with and)

```python
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
if a + b > c and a + c > b and b + c > a:
    print("valid")
else:
    print("invalid")
```

### M7. Grade and Attendance

```python
score = int(input("Enter score: "))
attendance = int(input("Enter attendance %: "))
if score >= 60 and attendance >= 75:
    print("pass")
else:
    print("fail")
```

---

## 🔴 Hard

### H1. Number in Range

```python
# Number in Range
# Valid range: 1 to 100 inclusive.

n = int(input("Enter a number: "))

if n >= 1 and n <= 100:
    print("in range")
else:
    print("out of range")
```

**How it works:** Both conditions must be True at the same time. `n >= 1` checks the lower bound. `n <= 100` checks the upper bound. `and` requires both to be True.

### H2. Divisible by Both 3 and 5

```python
# Divisible by Both 3 and 5

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("yes")
else:
    print("no")
```

**How it works:** Check both divisibility conditions with `and`. Alternatively, `n % 15 == 0` works because any number divisible by both 3 and 5 is also divisible by 15.

### H3. Vowel Check

```python
# Vowel Check
# Vowels: a, e, i, o, u

letter = input("Enter a lowercase letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("vowel")
else:
    print("consonant")
```

**How it works:** Use `or` to check all five vowels. If the letter matches any one of them, it is a vowel.

### H4. Right Triangle

```python
# Right Triangle
# Check if a^2 + b^2 == c^2 (c is the hypotenuse)

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c (largest): "))

if a * a + b * b == c * c:
    print("right triangle")
else:
    print("not a right triangle")
```

**How it works:** The Pythagorean theorem states a² + b² = c² for a right triangle. We use `*` for squaring since we haven't learned `**` in this context, but `a**2` also works.

### H5. Login Check

```python
# Login Check
# Both username AND password must be correct.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("welcome")
else:
    print("wrong")
```

**How it works:** Both conditions must be True. If either the username or the password is wrong, the `and` expression is False and we print "wrong".

### H6. Ticket Discount

```python
# Ticket Discount
# Adults (18-60): 100000 dong
# Children (<18) or seniors (>60): 50000 dong

age = int(input("Enter age: "))

if age < 18 or age > 60:
    print(50000)
else:
    print(100000)
```

**How it works:** Use `or` to check if the person is either a child OR a senior. If either condition is True, they get the half price. Otherwise (they are an adult), they pay full price.

### H7. Three Numbers — Find the Largest

```python
# Three Numbers — Find the Largest
# Check each number: is it >= both others?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
```

**How it works:** For each number, check if it is greater than or equal to both of the other two. Use `and` to combine the two comparisons. The first number that passes both checks is the largest. If `a` and `b` are equal and both are the largest, `a` is printed (which is correct since they have the same value).

---
