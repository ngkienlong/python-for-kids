# Lesson 27: Lists + Math 🔢

> **Goal:** Calculate sum, average, filter numbers, use list comprehension, and compute basic statistics.

---

## 1. Sum and Average

Python has a built-in `sum()` function:

```python
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)       # 150
print("Average:", average) # 30.0
```

---

## 2. Filter Numbers with a Loop

Find only the numbers that meet a condition:

```python
numbers = [-3, 5, -1, 8, 0, -2, 7]

# Filter: keep only positive numbers
positives = []
for num in numbers:
    if num > 0:
        positives.append(num)

print(positives)   # [5, 8, 7]
```

---

## 3. List Comprehension — A Shortcut

List comprehension creates a new list in one line:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Get only even numbers
evens = [x for x in numbers if x % 2 == 0]
print(evens)   # [2, 4, 6, 8]

# Double every number
doubled = [x * 2 for x in numbers]
print(doubled)   # [2, 4, 6, 8, 10, 12, 14, 16]
```

Think of it as: "Give me `x` for each `x` in `numbers`, but only if the condition is true."

---

## 4. Range of a List

The **range** of a dataset = maximum − minimum:

```python
numbers = [3, 7, 1, 9, 5]
data_range = max(numbers) - min(numbers)
print("Range:", data_range)   # 8
```

---

## 5. Sum of Squares

```python
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum([x * x for x in numbers])
print("Sum of squares:", sum_of_squares)   # 55
```

---

## 6. Running Total (Cumulative Sum)

A running total shows the sum so far at each step:

```python
numbers = [10, 20, 30, 40, 50]
running = 0
for num in numbers:
    running += num
    print(running)
```

**Output:**
```
10
30
60
100
150
```

---

## 7. Normalize a List

Normalization divides each value by the maximum, so all values are between 0 and 1:

```python
numbers = [10, 20, 50, 30, 40]
maximum = max(numbers)
normalized = [x / maximum for x in numbers]
print(normalized)   # [0.2, 0.4, 1.0, 0.6, 0.8]
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| sum | tổng | The total of all values added together |
| average | trung bình | Sum divided by count |
| mean | giá trị trung bình | Same as average |
| filter | lọc | Keep only items that meet a condition |
| range | khoảng | max minus min |
| variance | phương sai | How spread out the numbers are |
| statistics | thống kê | Math about data (sum, average, etc.) |
| comprehension | rút gọn | A short way to create a list |
| aggregate | tổng hợp | Combine many values into one (sum, average) |
| running total | tổng tích lũy | The sum so far at each step |

---

## 9. Summary

✅ `sum(list)` adds all items.
✅ Average = `sum(list) / len(list)`.
✅ Filter with a loop: `if condition: result.append(item)`.
✅ List comprehension: `[x for x in list if condition]`.
✅ Range = `max(list) - min(list)`.
✅ Running total: add each item to a running variable.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Sum and Average**

Create a list: `numbers = [10, 20, 30, 40, 50]`. Print the sum and average.

- **Input:** None.
- **Output:**
```
Sum: 150
Average: 30.0
```

---

**Exercise E2. Filter Positive**

Create a list: `numbers = [-3, 5, -1, 8, 0, -2, 7]`. Print only the positive numbers.

- **Input:** None.
- **Output:**
```
5
8
7
```

---

**Exercise E3. Sum of Squares**

Create a list: `numbers = [1, 2, 3, 4, 5]`. Print the sum of squares (1² + 2² + 3² + 4² + 5²).

- **Input:** None.
- **Output:**
```
55
```

---

**Exercise E4. Range**

Create a list: `temperatures = [23, 17, 31, 28, 15, 25, 19]`. Print the range (max - min).

- **Input:** None.
- **Output:**
```
16
```

---

**Exercise E5. List Comprehension — Evens**

Create a list: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Use list comprehension to create a list of only even numbers. Print it.

- **Input:** None.
- **Output:**
```
[2, 4, 6, 8, 10]
```

---

**Exercise E6. Running Total**

Create a list: `numbers = [5, 10, 15, 20, 25]`. Print the running total at each step.

- **Input:** None.
- **Output:**
```
5
15
30
50
75
```

---

**Exercise E7. Double with Comprehension**

Create a list: `numbers = [3, 6, 9, 12]`. Use list comprehension to create a new list where each number is doubled. Print it.

- **Input:** None.
- **Output:**
```
[6, 12, 18, 24]
```

---

### 🟡 Medium

---

**Exercise M1. Stats Report**

Read 5 numbers. Print their sum, average, min, and max.

- **Input:** 5 numbers (one per line).
- **Output:** 4 lines.

**Example:**

| Input | Output |
|-------|--------|
| 10 | Sum: 50 |
| 5 | Average: 10.0 |
| 15 | Min: 5 |
| 8 | Max: 15 |
| 12 | |

---

**Exercise M2. Filter Even Numbers**

Read N numbers. Print only the even ones.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Even numbers, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 4 |
| 3 | 8 |
| 4 | 6 |
| 7 | |
| 8 | |
| 6 | |
| 1 | |

---

**Exercise M3. Above Average**

Read N numbers. Print only those that are above the average.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Numbers above average, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 8 |
| 4 | 9 |
| 8 | |
| 2 | |
| 9 | |
| 2 | |

---

**Exercise M4. Normalize**

Read N numbers. Divide each by the maximum. Print the normalized values (2 decimal places).

- **Input:** First line: N. Next N lines: positive numbers.
- **Output:** Normalized values, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 0.2 |
| 10 | 0.4 |
| 20 | 1.0 |
| 50 | 0.6 |
| 30 | |

---

**Exercise M5. Cumulative Sum**

Read N numbers. Print the cumulative sum at each step.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Cumulative sums, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 10 |
| 10 | 30 |
| 20 | 60 |
| 30 | 100 |
| 40 | |

---

**Exercise M6. Count Multiples**

Read N numbers and a divisor D. Count how many numbers in the list are divisible by D.

- **Input:** First line: N. Next N lines: numbers. Last line: D.
- **Output:** The count.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 3 |
| 6 | |
| 9 | |
| 4 | |
| 12 | |
| 7 | |
| 3 | |
| 3 | |

---

**Exercise M7. Squares List**

Read N numbers. Print a new list where each number is replaced by its square.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The list of squares.

**Example:**

| Input | Output |
|-------|--------|
| 4 | [1, 4, 9, 16] |
| 1 | |
| 2 | |
| 3 | |
| 4 | |

---

### 🔴 Hard

---

**Exercise H1. Full Statistics**

Read N numbers. Print: sum, average (2 decimal places), min, max, and range (max - min).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Five lines.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Sum: 45 |
| 5 | Average: 9.0 |
| 10 | Min: 5 |
| 8 | Max: 12 |
| 12 | Range: 7 |
| 10 | |

**Explanation:** Sum=45, Average=9.0, Min=5, Max=12, Range=12-5=7.

---

**Exercise H2. Print Only Even Numbers**

Read N numbers. Print only the even ones, one per line.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Even numbers only.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 4 |
| 3 | 8 |
| 4 | 6 |
| 7 | 10 |
| 8 | |
| 6 | |
| 1 | |
| 10 | |

**Explanation:** Filter numbers where `num % 2 == 0`.

---

**Exercise H3. Above Average**

Read N numbers. Print how many are strictly above the average.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The count.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 3 |
| 4 | |
| 8 | |
| 6 | |
| 10 | |
| 2 | |
| 9 | |

**Explanation:** Average = 39/6 = 6.5. Numbers above 6.5: 8, 10, 9 → count = 3.

---

**Exercise H4. Sum of Squares**

Read N numbers. Print the sum of their squares.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The sum of squares.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 30 |
| 1 | |
| 2 | |
| 3 | |
| 4 | |

**Explanation:** 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30.

---

**Exercise H5. Normalize**

Read N positive numbers. Normalize each by dividing by the maximum. Print each normalized value rounded to 2 decimal places.

- **Input:** First line: N. Next N lines: positive numbers.
- **Output:** Normalized values, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 0.2 |
| 10 | 0.4 |
| 20 | 1.0 |
| 50 | 0.6 |
| 30 | |
| 40 | 0.8 |

**Explanation:** Max = 50. Each value divided by 50: 10/50=0.2, 20/50=0.4, etc.

---

**Exercise H6. Cumulative Sum**

Read N numbers. Print the cumulative sum at each step (running total).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Cumulative sums, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 5 |
| 5 | 15 |
| 10 | 45 |
| 30 | 85 |
| 40 | 135 |
| 50 | |

**Explanation:** 5, 5+10=15, 15+30=45, 45+40=85, 85+50=135.

---

**Exercise H7. Count Increases**

Read N numbers. Count how many times the value increases from one element to the next (i.e., `list[i+1] > list[i]`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The count of increases.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 3 |
| 3 | |
| 5 | |
| 2 | |
| 8 | |
| 7 | |
| 9 | |

**Explanation:** 3→5 (increase), 5→2 (decrease), 2→8 (increase), 8→7 (decrease), 7→9 (increase). Count = 3.
