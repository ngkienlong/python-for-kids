# Lesson 10: Answers — Nested Loops

---

## 🟢 Easy

**E1. Rectangle of Stars**
```python
for i in range(3):
    for j in range(6):
        print("*", end="")
    print()
```

**E2. Number Grid**
```python
for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()
```

**E3. Right Triangle**
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

**E4. Multiplication Table (3×3)**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

**E5. Count Pairs**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

**E6. Reverse Triangle**
```python
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

**E7. Square Numbers Grid**
```python
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end=" ")
    print()
```

---

## 🟡 Medium

**M1. Full Multiplication Table (5×5)**
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
```

**M2. Hollow Rectangle**
```python
rows = 4
cols = 6
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**M3. Number Triangle**
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**M4. Diagonal Pattern**
```python
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end="")
        else:
            print(".", end="")
    print()
```

**M5. Sum of Each Row**
```python
for i in range(1, 5):
    row_sum = 0
    for j in range(1, 5):
        row_sum = row_sum + i * j
    print("Row", i, "sum:", row_sum)
```

**M6. Staircase**
```python
for i in range(1, 6):
    print("#" * i)
```

**M7. Checkerboard**
```python
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
```

---

## 🔴 Hard

**H1. Full Multiplication Table**
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(str(i * j).rjust(4), end="")
    print()
```
*`rjust(4)` right-aligns the number in a field of 4 characters.*

**H2. Right Triangle of Stars**
```python
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
```

**H3. Hollow Rectangle**
```python
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```
*Print `*` on the border (first/last row or first/last column), space everywhere else.*

**H4. Count Even Pairs**
```python
n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i + j) % 2 == 0:
            count = count + 1
print(count)
```
*i + j is even when both are odd or both are even. Use i < j by starting j at i+1.*

**H5. Diamond Pattern**
```python
n = int(input())
half = n // 2
# Top half (including middle)
for i in range(half + 1):
    spaces = half - i
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
# Bottom half
for i in range(half - 1, -1, -1):
    spaces = half - i
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
```
*The middle row has n stars. Each row above/below has 2 fewer stars and 1 more space.*

**H6. Sum of Multiplication Table**
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total = total + i * j
print(total)
```
*Add every i×j value to the total. The mathematical formula is (n*(n+1)/2)^2.*

**H7. Pascal's Triangle**
```python
n = int(input())
row = [1]
for i in range(n):
    print(" ".join(str(x) for x in row))
    new_row = [1]
    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j + 1])
    new_row.append(1)
    row = new_row
```
*Each new row starts and ends with 1. Middle values are the sum of the two values above.*
