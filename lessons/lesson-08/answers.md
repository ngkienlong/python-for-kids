# Lesson 8: Answers — For Loop

---

## 🟢 Easy

**E1. Count to Ten**
```python
for i in range(1, 11):
    print(i)
```

**E2. Count Down**
```python
for i in range(5, 0, -1):
    print(i)
print("Go!")
```

**E3. Even Numbers**
```python
for i in range(2, 21, 2):
    print(i)
```

**E4. Print Stars**
```python
for i in range(1, 6):
    print("*" * i)
```

**E5. Sum 1 to 5**
```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)
```

**E6. Multiples of 3**
```python
for i in range(3, 31, 3):
    print(i)
```

**E7. Print Loop Variable**
```python
for i in range(0, 11, 2):
    print(i)
```

---

## 🟡 Medium

**M1. Sum of Odd Numbers**
```python
total = 0
for i in range(1, 20, 2):
    total = total + i
print(total)
```

**M2. Multiplication Row**
```python
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
```

**M3. Squares**
```python
for i in range(1, 9):
    print(i * i)
```

**M4. Reverse Triangle**
```python
for i in range(5, 0, -1):
    print("*" * i)
```

**M5. Count Characters**
```python
for i in range(1, 11):
    print(i, "A")
```

**M6. Product**
```python
product = 1
for i in range(1, 6):
    product = product * i
print(product)
```

**M7. Number Pattern**
```python
for i in range(1, 6):
    print(str(i) * i)
```

---

## 🔴 Hard

**H1. Sum of 1 to N**
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)
```
*Use an accumulator starting at 0. Add each i from 1 to N.*

**H2. Multiplication Table Row**
```python
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```
*Loop from 1 to 10, print N × i each time.*

**H3. Count Multiples**
```python
n, k = int(input()), int(input())
count = 0
for i in range(1, n + 1):
    if i % k == 0:
        count = count + 1
print(count)
```
*Check each number from 1 to N — if it divides evenly by K, count it.*

**H4. Factorial**
```python
n = int(input())
result = 1
for i in range(1, n + 1):
    result = result * i
print(result)
```
*Start with 1 (not 0!), multiply by each number from 1 to N.*

**H5. Sum of Even Numbers**
```python
n = int(input())
total = 0
for i in range(2, n + 1, 2):
    total = total + i
print(total)
```
*Use `range(2, n+1, 2)` to step through even numbers only.*

**H6. Number Triangle**
```python
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)
```
*For row i, print the digit i repeated i times using string multiplication.*

**H7. Digit Sum**
```python
n = int(input())
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10
print(total)
```
*Use `% 10` to get the last digit, `// 10` to remove it. Repeat until N becomes 0.*
