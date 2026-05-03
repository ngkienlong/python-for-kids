# Lesson 26: List Operations ✂️

> **Goal:** Use `sort()`, `reverse()`, `remove()`, `insert()`, `pop()`, `count()`, `index()`, and list slicing.

---

## 1. Sort a List — `sort()`

`sort()` rearranges items in **ascending** order (smallest to largest):

```python
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers)   # [1, 2, 3, 5, 8, 9]
```

Sort in **descending** order (largest to smallest):

```python
numbers.sort(reverse=True)
print(numbers)   # [9, 8, 5, 3, 2, 1]
```

> ⚠️ `sort()` changes the list **in place** — the original list is modified!

---

## 2. Reverse a List — `reverse()`

`reverse()` flips the order of items:

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)   # ['cherry', 'banana', 'apple']
```

---

## 3. Remove an Item — `remove()`

`remove(value)` removes the **first occurrence** of a value:

```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.remove(1)
print(numbers)   # [3, 4, 1, 5, 9]  (only first 1 is removed)
```

---

## 4. Insert an Item — `insert()`

`insert(index, value)` adds an item at a specific position:

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")   # insert "banana" at index 1
print(fruits)   # ['apple', 'banana', 'cherry']
```

---

## 5. Remove and Return Last Item — `pop()`

`pop()` removes and returns the last item:

```python
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print(last)     # cherry
print(fruits)   # ['apple', 'banana']
```

You can also pop at a specific index: `fruits.pop(0)` removes the first item.

---

## 6. Count Occurrences — `count()`

`count(value)` counts how many times a value appears:

```python
numbers = [1, 2, 1, 3, 1, 4]
print(numbers.count(1))   # 3
print(numbers.count(2))   # 1
```

---

## 7. Find Index — `index()`

`index(value)` returns the index of the **first occurrence**:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))   # 1
print(fruits.index("cherry"))   # 2
```

---

## 8. Slicing — Get Part of a List

Slicing lets you get a portion of a list:

```python
numbers = [10, 20, 30, 40, 50]
#           0    1    2    3    4

print(numbers[1:4])    # [20, 30, 40]  (index 1, 2, 3 — not including 4)
print(numbers[0:3])    # [10, 20, 30]
print(numbers[2:])     # [30, 40, 50]  (from index 2 to end)
print(numbers[:3])     # [10, 20, 30]  (from start to index 2)
print(numbers[:])      # [10, 20, 30, 40, 50]  (full copy)
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| sort | sắp xếp | Arrange items in order |
| reverse | đảo ngược | Flip the order of items |
| remove | xóa | Delete an item from the list |
| insert | chèn | Add an item at a specific position |
| pop | lấy ra | Remove and return an item (usually the last) |
| count | đếm | Count how many times a value appears |
| index | chỉ số | Find the position of a value |
| slice | cắt | Get a portion of a list |
| ascending | tăng dần | From smallest to largest |
| descending | giảm dần | From largest to smallest |
| in-place | tại chỗ | Modifies the original list directly |
| copy | bản sao | A new list with the same items |

---

## 10. Summary

✅ `list.sort()` sorts ascending; `list.sort(reverse=True)` sorts descending.
✅ `list.reverse()` reverses the list in place.
✅ `list.remove(v)` removes the first occurrence of value v.
✅ `list.insert(i, v)` inserts value v at index i.
✅ `list.pop()` removes and returns the last item.
✅ `list.count(v)` counts occurrences of v.
✅ `list.index(v)` returns the index of the first v.
✅ `list[1:4]` returns items at index 1, 2, 3.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Sort Ascending**

Create a list: `numbers = [5, 2, 8, 1, 9, 3, 7]`. Sort it and print.

- **Input:** None.
- **Output:**
```
[1, 2, 3, 5, 7, 8, 9]
```

---

**Exercise E2. Sort Descending**

Create a list: `numbers = [5, 2, 8, 1, 9, 3, 7]`. Sort it in descending order and print.

- **Input:** None.
- **Output:**
```
[9, 8, 7, 5, 3, 2, 1]
```

---

**Exercise E3. Reverse**

Create a list: `fruits = ["apple", "banana", "cherry", "mango"]`. Reverse it and print.

- **Input:** None.
- **Output:**
```
['mango', 'cherry', 'banana', 'apple']
```

---

**Exercise E4. Remove**

Create a list: `colors = ["red", "blue", "green", "blue", "yellow"]`. Remove "blue" and print.

- **Input:** None.
- **Output:**
```
['red', 'green', 'blue', 'yellow']
```

---

**Exercise E5. Insert**

Create a list: `numbers = [1, 2, 4, 5]`. Insert the number 3 at index 2. Print the result.

- **Input:** None.
- **Output:**
```
[1, 2, 3, 4, 5]
```

---

**Exercise E6. Pop**

Create a list: `items = ["pen", "book", "ruler", "eraser"]`. Pop the last item and print both the popped item and the remaining list.

- **Input:** None.
- **Output:**
```
eraser
['pen', 'book', 'ruler']
```

---

**Exercise E7. Slice**

Create a list: `numbers = [10, 20, 30, 40, 50, 60, 70]`. Print the slice from index 2 to index 5 (not including 5).

- **Input:** None.
- **Output:**
```
[30, 40, 50]
```

---

### 🟡 Medium

---

**Exercise M1. Sort and Print Top 3**

Create a list: `scores = [72, 95, 88, 61, 79, 84, 91]`. Sort descending and print the top 3 scores.

- **Input:** None.
- **Output:**
```
95
91
88
```

---

**Exercise M2. Count and Index**

Create a list: `letters = ["a", "b", "c", "a", "d", "a"]`. Print how many times "a" appears and the index of the first "a".

- **Input:** None.
- **Output:**
```
Count: 3
First index: 0
```

---

**Exercise M3. Remove All of One Value**

Create a list: `numbers = [1, 2, 3, 2, 4, 2, 5]`. Remove all occurrences of 2. Print the result.

- **Input:** None.
- **Output:**
```
[1, 3, 4, 5]
```

---

**Exercise M4. Insert at Position**

Read a list of 5 numbers, a position K, and a value V. Insert V at position K. Print the result.

- **Input:** 5 numbers (one per line), then K, then V.
- **Output:** The new list.

**Example:**

| Input | Output |
|-------|--------|
| 10 | [10, 20, 99, 30, 40, 50] |
| 20 | |
| 30 | |
| 40 | |
| 50 | |
| 2 | |
| 99 | |

---

**Exercise M5. Slice Middle**

Create a list: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Print the middle 4 elements (index 3 to 6 inclusive).

- **Input:** None.
- **Output:**
```
[4, 5, 6, 7]
```

---

**Exercise M6. Sort Names**

Read 5 names from the user. Sort them alphabetically and print.

- **Input:** 5 lines, each with a name.
- **Output:** Sorted names, one per line.

**Example:**

| Input | Output |
|-------|--------|
| Charlie | Alice |
| Alice | Bob |
| Eve | Charlie |
| Bob | Diana |
| Diana | Eve |

---

**Exercise M7. Pop Until Empty**

Create a list: `stack = [1, 2, 3, 4, 5]`. Use a loop to pop and print each item until the list is empty.

- **Input:** None.
- **Output:**
```
5
4
3
2
1
```

---

### 🔴 Hard

---

**Exercise H1. Sort N Numbers**

Read N numbers into a list. Sort them in ascending order and print.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The sorted list.

**Example:**

| Input | Output |
|-------|--------|
| 5 | [1, 3, 5, 7, 9] |
| 9 | |
| 3 | |
| 7 | |
| 1 | |
| 5 | |

**Explanation:** Use `list.sort()` after building the list.

---

**Exercise H2. Top 3 Largest**

Read N numbers. Print the top 3 largest values (sort descending, take first 3).

- **Input:** First line: N (N ≥ 3). Next N lines: numbers.
- **Output:** Three lines: 1st largest, 2nd largest, 3rd largest.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 95 |
| 72 | 88 |
| 95 | 84 |
| 88 | |
| 61 | |
| 79 | |
| 84 | |

**Explanation:** Sort descending: [95, 88, 84, 79, 72, 61]. Print first 3.

---

**Exercise H3. Remove All Occurrences of V**

Read N numbers and a value V. Remove all occurrences of V from the list. Print the result.

- **Input:** First line: N. Next N lines: numbers. Last line: V.
- **Output:** The list after removing all V's.

**Example:**

| Input | Output |
|-------|--------|
| 7 | [1, 3, 4, 5] |
| 1 | |
| 2 | |
| 3 | |
| 2 | |
| 4 | |
| 2 | |
| 5 | |
| 2 | |

**Explanation:** Remove all 2's. Use a loop: while V in list, remove it.

---

**Exercise H4. Insert at Position K**

Read N numbers, a position K, and a value V. Insert V at position K. Print the result.

- **Input:** First line: N. Next N lines: numbers. Then K. Then V.
- **Output:** The new list.

**Example:**

| Input | Output |
|-------|--------|
| 4 | [10, 20, 99, 30, 40] |
| 10 | |
| 20 | |
| 30 | |
| 40 | |
| 2 | |
| 99 | |

**Explanation:** `list.insert(2, 99)` inserts 99 at index 2.

---

**Exercise H5. Median**

Read N numbers. Sort them and print the median (middle value). If N is even, print the average of the two middle values.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The median.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 7 |
| 3 | |
| 7 | |
| 1 | |
| 9 | |
| 5 | |

| Input | Output |
|-------|--------|
| 4 | 6.0 |
| 3 | |
| 9 | |
| 5 | |
| 7 | |

**Explanation:** For odd N: median = sorted[N//2]. For even N: median = (sorted[N//2 - 1] + sorted[N//2]) / 2.

---

**Exercise H6. Mode (Most Frequent)**

Read N numbers. Find and print the mode (the value that appears most often). If there is a tie, print the smallest.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The mode.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 3 |
| 1 | |
| 3 | |
| 2 | |
| 3 | |
| 1 | |
| 3 | |
| 2 | |

**Explanation:** 3 appears 3 times, 1 appears 2 times, 2 appears 2 times. Mode = 3.

---

**Exercise H7. Remove Duplicates**

Read N numbers. Remove all duplicates (keep only the first occurrence of each value). Print the result.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The list with duplicates removed, in original order.

**Example:**

| Input | Output |
|-------|--------|
| 7 | [1, 2, 3, 4] |
| 1 | |
| 2 | |
| 3 | |
| 2 | |
| 1 | |
| 4 | |
| 3 | |

**Explanation:** Keep only the first occurrence of each number.
