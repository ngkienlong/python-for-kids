# Lesson 1 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Say Hello

```python
print("Hello")
```

### E2. Your Name

```python
print("An")  # Replace "An" with your name
```

### E3. Three Lines

```python
print("I like Python")
print("Python is fun")
print("I am a coder")
```

### E4. A Number

```python
print(2025)
```

### E5. Math Result

```python
print(10 + 25)
```

### E6. Empty Line

```python
print("Hello")
print()
print("World")
```

### E7. Star Box

```python
print("*****")
print("*   *")
print("*   *")
print("*****")
```

---

## 🟡 Medium

### M1. Greeting Card

```python
print("+------------------+")
print("|  Happy Birthday! |")
print("|    Dear An       |")
print("+------------------+")
```

### M2. Math Table

```python
print("10 + 5 =", 10 + 5)
print("10 - 5 =", 10 - 5)
print("10 * 5 =", 10 * 5)
```

### M3. My Info

```python
print("Name: An")
print("Age: 8")
print("School: ABC Primary School")
print("Hobby: coding")
```

### M4. Triangle

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
```

### M5. Number Pyramid

```python
print("1")
print("12")
print("123")
print("1234")
print("12345")
```

### M6. House

```python
print("   /\\")
print("  /  \\")
print(" /    \\")
print("+------+")
print("|      |")
print("|  []  |")
print("+------+")
```

### M7. Multiplication

```python
print(123 * 456)
```

---

## 🔴 Hard

### H1. Planting Trees

```python
# Planting Trees
# A tree every 10 meters, starting at 10 m.
# Number of trees = N // 10

n = 100  # Change this to test with different values
trees = n // 10
print(trees)
```

**How it works:** If the road is N meters, trees are at 10, 20, ..., up to the largest multiple of 10 that is ≤ N. That count is `N // 10`.

### H2. Candy Sharing

```python
# Candy Sharing
# Share N candies among 3 friends equally.

n = 10  # Change this to test
each = n // 3   # Each friend gets this many
left = n % 3    # Leftover candies
print(each)
print(left)
```

**How it works:** `//` gives the quotient (how many each friend gets). `%` gives the remainder (leftover).

### H3. Fence Posts

```python
# Fence Posts
# Square garden, side = S meters.
# Posts every 1 meter along each side.

s = 4  # Change this to test
posts = 4 * s
print(posts)
```

**How it works:** Each side has S+1 posts, but 4 corners are shared. Total = 4 × (S+1) - 4 = 4 × S.

### H4. Book Pages

```python
# Book Pages
# Count total digits used to number pages 1 to N.

n = 11  # Change this to test

# Pages 1-9: 1 digit each
if n <= 9:
    digits = n
elif n <= 99:
    # 9 pages with 1 digit + remaining pages with 2 digits
    digits = 9 + (n - 9) * 2
else:
    # 9 pages with 1 digit + 90 pages with 2 digits + remaining with 3 digits
    digits = 9 + 90 * 2 + (n - 99) * 3

print(digits)
```

**How it works:**
- Pages 1–9: 9 × 1 = 9 digits.
- Pages 10–99: 90 × 2 = 180 digits.
- Pages 100+: each uses 3 digits.

For N = 11: 9 + (11 - 9) × 2 = 9 + 4 = 13.

### H5. Clock

```python
# Clock
# Convert total minutes since midnight to H:MM format.

m = 150  # Change this to test

hours = m // 60
minutes = m % 60

# Print with format: minutes always 2 digits
if minutes < 10:
    print(str(hours) + ":0" + str(minutes))
else:
    print(str(hours) + ":" + str(minutes))
```

**How it works:** Divide by 60 to get hours, remainder is minutes. Use `//` and `%`.

For M = 150: 150 // 60 = 2 hours, 150 % 60 = 30 minutes → 2:30.

> **Note:** Exercises H4 and H5 use `if/else` which you will learn in Lesson 5. For now, it's OK to just understand the math idea. You can come back and solve them properly after Lesson 5!

---
