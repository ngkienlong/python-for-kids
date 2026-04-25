# Lesson 2 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Add Two Numbers

```python
print(25 + 17)
```

### E2. Subtract

```python
print(100 - 37)
```

### E3. Multiply

```python
print(12 * 9)
```

### E4. Divide

```python
print(100 / 8)
```

### E5. Floor Division

```python
print(100 // 8)
```

### E6. Remainder

```python
print(100 % 8)
```

### E7. All Operators

```python
print("20 + 7 =", 20 + 7)
print("20 - 7 =", 20 - 7)
print("20 * 7 =", 20 * 7)
print("20 / 7 =", 20 / 7)
print("20 // 7 =", 20 // 7)
print("20 % 7 =", 20 % 7)
```

---

## 🟡 Medium

### M1. Parentheses Matter

```python
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
print(10 - 6 / 2)      # 7.0
print((10 - 6) / 2)    # 2.0
print(8 + 2 * 5 - 1)   # 17
```

### M2. Seconds in a Day

```python
print(24 * 60 * 60)
```

### M3. Average

```python
print((85 + 92 + 78) / 3)
```

### M4. Temperature Converter

```python
print(37 * 9 / 5 + 32)
```

### M5. Rectangle

```python
width = 15
height = 8
print("Area =", width * height)
print("Perimeter =", 2 * width + 2 * height)
```

> Note: We use variables here for clarity. Variables are taught in Lesson 3. You can also write `print("Area =", 15 * 8)` directly.

### M6. Even or Odd Check

```python
print("10 % 2 =", 10 % 2)
print("15 % 2 =", 15 % 2)
print("22 % 2 =", 22 % 2)
print("33 % 2 =", 33 % 2)
print("100 % 2 =", 100 % 2)
```

### M7. Big Multiplication

```python
print(12345 * 67890)
```

---

## 🔴 Hard

### H1. Coin Change

```python
# Coin Change
# Exchange N dong into 500, 200, 100 coins (largest first).

n = 1900  # Change this to test

# 500-dong coins
coin500 = n // 500
n = n % 500  # remaining money

# 200-dong coins
coin200 = n // 200
n = n % 200  # remaining money

# 100-dong coins
coin100 = n // 100

print(coin500)
print(coin200)
print(coin100)
```

**How it works:** Use `//` to find how many coins fit, then `%` to find the remaining money. Repeat for each coin type.

### H2. Time Breakdown

```python
# Time Breakdown
# Convert N seconds to hours, minutes, seconds.

n = 3661  # Change this to test

hours = n // 3600
n = n % 3600       # remaining seconds after removing hours

minutes = n // 60
seconds = n % 60   # remaining seconds after removing minutes

print(hours, minutes, seconds)
```

**How it works:** 1 hour = 3600 seconds. Find hours first, then work with the remainder.

### H3. Digit Extraction

```python
# Digit Extraction
# Extract hundreds, tens, ones from a 3-digit number.

n = 456  # Change this to test

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

print(hundreds)
print(tens)
print(ones)
```

**How it works:**
- `n // 100` removes the last 2 digits → hundreds.
- `(n // 10) % 10` removes the last digit, then takes the last digit of what's left → tens.
- `n % 10` takes the last digit → ones.

### H4. Sharing Apples

```python
# Sharing Apples
# N apples shared among K students.

n = 23  # Change this to test
k = 5   # Change this to test

each = n // k
leftover = n % k

print(each)
print(leftover)
```

**How it works:** Same idea as candy sharing — `//` for quotient, `%` for remainder.

### H5. Reverse a 3-Digit Number

```python
# Reverse a 3-Digit Number

n = 456  # Change this to test

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

# Build the reversed number
reversed_number = ones * 100 + tens * 10 + hundreds
print(reversed_number)
```

**How it works:** Extract each digit, then put them back in reverse order. Ones become hundreds, hundreds become ones.

### H6. Chessboard Squares

```python
# Chessboard Squares
# Black if (r + c) is even, white if odd.

r = 1  # Change this to test
c = 1  # Change this to test

# (r + c) % 2 tells us: 0 = even = black, 1 = odd = white
result = (r + c) % 2

# For now, just print the result
# 0 means black, 1 means white
print(result)

# After you learn if/else (Lesson 5), you can write:
# if (r + c) % 2 == 0:
#     print("black")
# else:
#     print("white")
```

**How it works:** The sum of row and column determines the color. Even sum = black, odd sum = white.

### H7. Sum of Digits

```python
# Sum of Digits of a 3-digit number.

n = 456  # Change this to test

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

digit_sum = hundreds + tens + ones
print(digit_sum)
```

**How it works:** Extract each digit using `//` and `%`, then add them together. For 456: 4 + 5 + 6 = 15.

---
