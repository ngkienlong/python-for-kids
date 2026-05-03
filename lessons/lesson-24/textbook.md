# Lesson 24: Lists — Your First Collection 📋

> **Goal:** Create lists, access items by index, use `len()`, `append()`, and modify list items.

---

## 1. What is a List?

A **list** is a collection of items stored in one variable.

In Scratch, you have a **List** block that stores many values. In Python, we use square brackets `[]`.

| Scratch | Python |
|---------|--------|
| Create a list called "fruits" | `fruits = ["apple", "banana", "cherry"]` |
| Add item to list | `fruits.append("mango")` |
| Item 1 of list | `fruits[0]` |
| Length of list | `len(fruits)` |

---

## 2. Creating a List

```python
# A list of fruit names
fruits = ["apple", "banana", "cherry"]

# A list of numbers
scores = [95, 87, 72, 100, 65]

# A list of mixed types
mixed = ["Alice", 10, 3.14, True]

# An empty list
empty = []
```

---

## 3. Accessing Items — Index

Every item in a list has an **index** (position number). **Index starts at 0!**

```python
fruits = ["apple", "banana", "cherry"]
#          index 0   index 1   index 2
```

```python
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # cherry
```

### Negative Index

You can count from the end using negative numbers:

```python
print(fruits[-1])  # cherry  (last item)
print(fruits[-2])  # banana  (second to last)
print(fruits[-3])  # apple   (third to last)
```

| Index | -3 | -2 | -1 |
|-------|----|----|-----|
| Item  | apple | banana | cherry |
| Index | 0 | 1 | 2 |

---

## 4. Length of a List — `len()`

`len()` tells you how many items are in the list.

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))   # 3

scores = [95, 87, 72, 100, 65]
print(len(scores))   # 5
```

---

## 5. Modifying Items

You can change an item by assigning a new value to its index:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "grape"
print(fruits)   # ['apple', 'grape', 'cherry']
```

---

## 6. Adding Items — `append()`

`append()` adds a new item to the **end** of the list:

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']

fruits.append("kiwi")
print(fruits)   # ['apple', 'banana', 'mango', 'kiwi']
```

---

## 7. Printing a List

```python
fruits = ["apple", "banana", "cherry"]

# Print the whole list
print(fruits)           # ['apple', 'banana', 'cherry']

# Print each item
print(fruits[0])        # apple
print(fruits[1])        # banana
print(fruits[2])        # cherry
```

---

## 8. Lists Can Hold Any Type

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [42, "hello", 3.14, True]
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| list | danh sách | A collection of items in order |
| index | chỉ số | The position number of an item (starts at 0) |
| element | phần tử | One item inside a list |
| item | mục | Same as element |
| append | thêm vào | Add an item to the end of a list |
| length | độ dài | How many items are in the list |
| access | truy cập | Get an item from the list |
| modify | thay đổi | Change an item in the list |
| zero-indexed | chỉ số bắt đầu từ 0 | First item is at index 0, not 1 |
| negative index | chỉ số âm | Count from the end: -1 is last item |
| collection | bộ sưu tập | A group of items stored together |
| sequence | chuỗi | Items stored in a specific order |

---

## 10. Summary

✅ A list stores many items in one variable: `fruits = ["apple", "banana"]`.
✅ Index starts at 0: `fruits[0]` is the first item.
✅ Negative index counts from the end: `fruits[-1]` is the last item.
✅ `len(fruits)` gives the number of items.
✅ `fruits.append("mango")` adds to the end.
✅ `fruits[1] = "grape"` changes an item.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Create and Print**

Create a list with 3 of your favorite colors. Print the whole list.

- **Input:** None.
- **Output:** Print the list.

**Example:**
```
['red', 'blue', 'green']
```

---

**Exercise E2. First and Last**

Create a list: `numbers = [10, 20, 30, 40, 50]`. Print the first item and the last item.

- **Input:** None.
- **Output:**
```
10
50
```

---

**Exercise E3. Access by Index**

Create a list: `animals = ["cat", "dog", "bird", "fish", "rabbit"]`. Print the item at index 2.

- **Input:** None.
- **Output:**
```
bird
```

---

**Exercise E4. Length**

Create a list: `scores = [85, 92, 78, 95, 88, 76, 91]`. Print how many scores are in the list.

- **Input:** None.
- **Output:**
```
7
```

---

**Exercise E5. Append**

Start with an empty list. Append the numbers 1, 2, 3, 4, 5 one by one. Print the final list.

- **Input:** None.
- **Output:**
```
[1, 2, 3, 4, 5]
```

---

**Exercise E6. Modify**

Create a list: `fruits = ["apple", "banana", "cherry"]`. Change "banana" to "mango". Print the new list.

- **Input:** None.
- **Output:**
```
['apple', 'mango', 'cherry']
```

---

**Exercise E7. Negative Index**

Create a list: `days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]`. Use negative indexing to print the last 3 items.

- **Input:** None.
- **Output:**
```
Fri
Sat
Sun
```

---

### 🟡 Medium

---

**Exercise M1. Build a List with Input**

Read 3 names from the user (one per line). Store them in a list. Print the list.

- **Input:** 3 lines, each with a name.
- **Output:** Print the list.

**Example:**

| Input | Output |
|-------|--------|
| Alice | ['Alice', 'Bob', 'Charlie'] |
| Bob | |
| Charlie | |

---

**Exercise M2. Index Check**

Create a list: `colors = ["red", "green", "blue", "yellow", "purple"]`. Read an index from the user. Print the color at that index.

- **Input:** One integer (0 to 4).
- **Output:** The color at that index.

**Example:**

| Input | Output |
|-------|--------|
| 2 | blue |
| 0 | red |

---

**Exercise M3. Append and Length**

Start with a list: `items = ["pen", "book"]`. Read 3 more items from the user and append each one. Print the final list and its length.

- **Input:** 3 lines, each with an item name.
- **Output:** The final list, then its length.

**Example:**

| Input | Output |
|-------|--------|
| ruler | ['pen', 'book', 'ruler', 'eraser', 'bag'] |
| eraser | 5 |
| bag | |

---

**Exercise M4. Replace Item**

Create a list: `numbers = [1, 2, 3, 4, 5]`. Read an index K and a new value V. Replace the item at index K with V. Print the new list.

- **Input:** Two integers: K (index) and V (new value).
- **Output:** The modified list.

**Example:**

| Input | Output |
|-------|--------|
| 2 | [1, 2, 99, 4, 5] |
| 99 | |

---

**Exercise M5. Sum of List**

Create a list: `prices = [15, 25, 10, 30, 20]`. Print the sum of all prices using `sum()`.

- **Input:** None.
- **Output:** The sum.

**Example:**
```
100
```

---

**Exercise M6. List Info**

Create a list of 5 numbers. Print: the list, its length, the first item, and the last item.

- **Input:** None (hardcode the list).
- **Output:** 4 lines.

**Example:**
```
[3, 7, 1, 9, 5]
5
3
5
```

---

**Exercise M7. Swap Items**

Create a list: `items = ["A", "B", "C", "D"]`. Swap the first and last items. Print the new list.

- **Input:** None.
- **Output:**
```
['D', 'B', 'C', 'A']
```

---

### 🔴 Hard

---

**Exercise H1. Read N Numbers into a List**

Read N numbers from the user and store them in a list. Print the list.

- **Input:** First line: integer N. Next N lines: one number each.
- **Output:** The list of numbers.

**Example:**

| Input | Output |
|-------|--------|
| 4 | [10, 20, 30, 40] |
| 10 | |
| 20 | |
| 30 | |
| 40 | |

**Explanation:** Read N, then read N numbers one by one using a loop and `append()`.

---

**Exercise H2. First and Last of N Numbers**

Read N numbers into a list. Print the first and last element.

- **Input:** First line: integer N. Next N lines: one number each.
- **Output:** Two lines: first element, then last element.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 3 | 9 |
| 7 | |
| 1 | |
| 5 | |
| 9 | |

**Explanation:** After building the list, use `list[0]` and `list[-1]`.

---

**Exercise H3. Element at Position K**

Read N numbers into a list. Read a position K (0-indexed). Print the element at position K.

- **Input:** First line: N. Next N lines: numbers. Last line: K.
- **Output:** The element at index K.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1 |
| 3 | |
| 7 | |
| 1 | |
| 5 | |
| 9 | |
| 2 | |

**Explanation:** K=2, so print `list[2]` which is 1.

---

**Exercise H4. Replace at Position K**

Read N numbers into a list. Read position K and new value V. Replace the element at position K with V. Print the new list.

- **Input:** First line: N. Next N lines: numbers. Then K. Then V.
- **Output:** The modified list.

**Example:**

| Input | Output |
|-------|--------|
| 4 | [10, 20, 99, 40] |
| 10 | |
| 20 | |
| 30 | |
| 40 | |
| 2 | |
| 99 | |

**Explanation:** Replace index 2 (value 30) with 99.

---

**Exercise H5. Reverse Using Negative Index**

Read N numbers into a list. Print the list in reverse order using negative indexing (do NOT use `reverse()`).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The numbers in reverse order, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 40 |
| 10 | 30 |
| 20 | 20 |
| 30 | 10 |
| 40 | |

**Explanation:** Print `list[-1]`, `list[-2]`, ..., `list[-N]` using a loop.

---

**Exercise H6. Shopping List**

Read N items from the user. Print a numbered shopping list (1. item1, 2. item2, ...).

- **Input:** First line: N. Next N lines: item names.
- **Output:** Numbered list.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 1. apple |
| apple | 2. banana |
| banana | 3. milk |
| milk | |

**Explanation:** Use index + 1 for the display number.

---

**Exercise H7. Count Positive, Negative, Zero**

Read N numbers into a list. Count how many are positive, negative, and zero. Print the counts.

- **Input:** First line: N. Next N lines: numbers (can be negative).
- **Output:** Three lines: count of positive, negative, zero.

**Example:**

| Input | Output |
|-------|--------|
| 6 | Positive: 3 |
| 5 | Negative: 2 |
| -3 | Zero: 1 |
| 0 | |
| 7 | |
| -1 | |
| 4 | |

**Explanation:** Loop through the list and check each number with `if/elif/else`.
