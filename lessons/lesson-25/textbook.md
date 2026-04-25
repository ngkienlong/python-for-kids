# Lesson 25: Loop Through Lists 🔄

> **Goal:** Use `for` loops to iterate over lists, loop with index, find min/max, and search in a list.

---

## 1. Why Loop Through a List?

If a list has 100 items, you don't want to write `print(list[0])`, `print(list[1])`, ... 100 times!
A loop lets you process every item automatically.

> 💡 **Scratch connection:** In Scratch, "for each item in list" → In Python, `for item in list:`.

---

## 2. `for item in list` — Loop Over Items

The simplest way to loop through a list:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

Python automatically gives you each item one by one. The variable `fruit` holds the current item.

---

## 3. `for i in range(len(list))` — Loop With Index

Sometimes you need the index (position) too:

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

**Output:**
```
0 apple
1 banana
2 cherry
```

Use this when you need to know the position of each item.

---

## 4. Find the Minimum

```python
numbers = [5, 3, 8, 1, 9, 2]

# Start by assuming the first item is the smallest
minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num   # found a smaller number!

print("Minimum:", minimum)   # 1
```

---

## 5. Find the Maximum

```python
numbers = [5, 3, 8, 1, 9, 2]

# Start by assuming the first item is the largest
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num   # found a larger number!

print("Maximum:", maximum)   # 9
```

---

## 6. Search in a List

```python
fruits = ["apple", "banana", "cherry", "mango"]
target = "cherry"
found = False

for i in range(len(fruits)):
    if fruits[i] == target:
        found = True
        print("Found", target, "at index", i)

if not found:
    print(target, "not found")
```

---

## 7. Count Occurrences

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 1, 3]
target = 1
count = 0

for num in numbers:
    if num == target:
        count += 1

print(target, "appears", count, "times")   # 1 appears 3 times
```

---

## 8. Sum and Average

```python
scores = [85, 92, 78, 95, 88]

total = 0
for score in scores:
    total += score

average = total / len(scores)
print("Sum:", total)
print("Average:", average)
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| iterate | lặp qua | Go through each item one by one |
| traverse | duyệt qua | Visit every item in a collection |
| element | phần tử | One item in the list |
| index | chỉ số | The position number of an item |
| minimum | giá trị nhỏ nhất | The smallest value |
| maximum | giá trị lớn nhất | The largest value |
| search | tìm kiếm | Look for a specific item |
| count | đếm | How many times something appears |
| occurrence | lần xuất hiện | One time that something appears |
| linear search | tìm kiếm tuyến tính | Check each item one by one from start to end |

---

## 10. Summary

✅ `for item in list:` gives you each item directly.
✅ `for i in range(len(list)):` gives you the index too.
✅ To find min/max: start with `list[0]`, compare each item.
✅ To search: loop and check `if item == target`.
✅ To count: use a counter variable and `+= 1`.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Print All Items**

Create a list: `animals = ["cat", "dog", "bird", "fish"]`. Use a `for` loop to print each animal on its own line.

- **Input:** None.
- **Output:**
```
cat
dog
bird
fish
```

---

**Exercise E2. Print With Index**

Create a list: `colors = ["red", "green", "blue", "yellow"]`. Use `for i in range(len(colors))` to print each color with its index.

- **Input:** None.
- **Output:**
```
0 red
1 green
2 blue
3 yellow
```

---

**Exercise E3. Sum of List**

Create a list: `numbers = [10, 20, 30, 40, 50]`. Use a loop to calculate and print the sum.

- **Input:** None.
- **Output:**
```
150
```

---

**Exercise E4. Count Even Numbers**

Create a list: `numbers = [1, 2, 3, 4, 5, 6, 7, 8]`. Count and print how many numbers are even.

- **Input:** None.
- **Output:**
```
4
```

---

**Exercise E5. Find Maximum**

Create a list: `scores = [72, 95, 88, 61, 79]`. Find and print the maximum score without using `max()`.

- **Input:** None.
- **Output:**
```
95
```

---

**Exercise E6. Print Doubled**

Create a list: `numbers = [3, 5, 7, 9]`. Print each number doubled.

- **Input:** None.
- **Output:**
```
6
10
14
18
```

---

**Exercise E7. Count Occurrences**

Create a list: `letters = ["a", "b", "a", "c", "a", "b"]`. Count how many times "a" appears.

- **Input:** None.
- **Output:**
```
3
```

---

### 🟡 Medium

---

**Exercise M1. Print Numbered List**

Read N items from the user. Print them as a numbered list (1. item, 2. item, ...).

- **Input:** First line: N. Next N lines: item names.
- **Output:** Numbered list.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 1. apple |
| apple | 2. banana |
| banana | 3. cherry |
| cherry | |

---

**Exercise M2. Find Minimum**

Read N numbers. Find and print the minimum without using `min()`.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The minimum.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 7 | |
| 3 | |
| 9 | |
| 5 | |
| 6 | |

---

**Exercise M3. Search**

Read N names and a target name. Print "found" if the target is in the list, else "not found".

- **Input:** First line: N. Next N lines: names. Last line: target name.
- **Output:** "found" or "not found".

**Example:**

| Input | Output |
|-------|--------|
| 4 | found |
| Alice | |
| Bob | |
| Charlie | |
| Diana | |
| Bob | |

---

**Exercise M4. Count Above 50**

Read N numbers. Count and print how many are greater than 50.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The count.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 30 | |
| 70 | |
| 55 | |
| 20 | |
| 80 | |

---

**Exercise M5. Print in Reverse with Loop**

Read N numbers. Print them in reverse order using a loop (do NOT use `reverse()`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Numbers in reverse order.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 40 |
| 10 | 30 |
| 20 | 20 |
| 30 | 10 |
| 40 | |

---

**Exercise M6. Average**

Read N numbers. Print their average (rounded to 2 decimal places).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The average.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 5.5 |
| 4 | |
| 6 | |
| 5 | |
| 7 | |

---

**Exercise M7. Print Only Positive**

Read N numbers. Print only the positive ones.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Positive numbers, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 5 |
| 5 | 3 |
| -2 | 8 |
| 3 | |
| -7 | |
| 8 | |

---

### 🔴 Hard

---

**Exercise H1. Sum and Average**

Read N numbers into a list. Print their sum and average (rounded to 2 decimal places).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Two lines: sum, then average.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Sum: 45 |
| 5 | Average: 9.0 |
| 10 | |
| 8 | |
| 12 | |
| 10 | |

**Explanation:** Sum = 5+10+8+12+10 = 45. Average = 45/5 = 9.0.

---

**Exercise H2. Find Maximum**

Read N numbers into a list. Find and print the maximum value (do NOT use `max()`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The maximum value.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 95 |
| 72 | |
| 95 | |
| 88 | |
| 61 | |
| 79 | |
| 84 | |

**Explanation:** Start with `maximum = numbers[0]`, then compare each item.

---

**Exercise H3. Find Minimum**

Read N numbers into a list. Find and print the minimum value (do NOT use `min()`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The minimum value.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 7 | |
| 3 | |
| 9 | |
| 5 | |
| 6 | |

**Explanation:** Start with `minimum = numbers[0]`, then compare each item.

---

**Exercise H4. Search with Index**

Read N numbers and a target T. If T is in the list, print "Found at index X". If not, print "Not found".

- **Input:** First line: N. Next N lines: numbers. Last line: T.
- **Output:** "Found at index X" or "Not found".

**Example:**

| Input | Output |
|-------|--------|
| 5 | Found at index 2 |
| 10 | |
| 20 | |
| 30 | |
| 40 | |
| 50 | |
| 30 | |

**Explanation:** 30 is at index 2 (0-indexed).

---

**Exercise H5. Count Above Average**

Read N numbers. Calculate the average, then print how many numbers are above the average.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The count of numbers above average.

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

**Exercise H6. Reverse with Loop**

Read N numbers. Print them in reverse order using a loop (do NOT use `reverse()`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Numbers in reverse order, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 5 |
| 1 | 4 |
| 2 | 3 |
| 3 | 2 |
| 4 | 1 |
| 5 | |

**Explanation:** Loop `i` from `n-1` down to `0` and print `numbers[i]`.

---

**Exercise H7. Second Largest**

Read N numbers. Find and print the second largest number (assume all numbers are different).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The second largest number.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 88 |
| 72 | |
| 95 | |
| 88 | |
| 61 | |
| 79 | |

**Explanation:** Sorted descending: 95, 88, 79, 72, 61. Second largest = 88.
