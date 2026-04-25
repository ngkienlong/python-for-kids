# Lesson 33: Problem Solving Strategies 🧠

> **Goal:** Learn how to break down problems, plan before coding, debug effectively, and handle edge cases.

---

## 1. The 5-Step Problem Solving Process

When you face a programming problem, follow these steps:

```
Step 1: UNDERSTAND — Read carefully. What is the input? What is the output?
Step 2: PLAN — Write pseudocode or steps in plain English.
Step 3: CODE — Implement step by step.
Step 4: TEST — Try different inputs, including edge cases.
Step 5: DEBUG — Find and fix errors.
```

---

## 2. Step 1: Understand the Problem

Before writing any code, ask yourself:
- What is the **input**? (What does the program receive?)
- What is the **output**? (What should the program print?)
- Are there any **constraints**? (e.g., N ≥ 1, numbers can be negative)
- What are the **edge cases**? (e.g., empty list, N = 0, very large numbers)

---

## 3. Step 2: Plan with Pseudocode

**Pseudocode** is writing your solution in plain English before coding:

```
Problem: Find the largest number in a list of N numbers.

Pseudocode:
1. Read N
2. Read N numbers into a list
3. Set maximum = first number
4. For each number in the list:
   a. If number > maximum, update maximum
5. Print maximum
```

---

## 4. Step 3: Code Step by Step

Translate your pseudocode into Python:

```python
# Step 1: Read N
n = int(input())

# Step 2: Read N numbers
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Step 3: Set maximum = first number
maximum = numbers[0]

# Step 4: Compare each number
for num in numbers:
    if num > maximum:
        maximum = num

# Step 5: Print result
print(maximum)
```

---

## 5. Step 4: Test with Multiple Inputs

Always test your program with:
- **Normal input** — typical case
- **Edge cases** — boundary values
- **Special cases** — all same values, single item, etc.

```python
# Test cases for "find maximum":
# Normal: [3, 7, 1, 9, 5] → 9
# All same: [5, 5, 5] → 5
# Single item: [42] → 42
# Negative numbers: [-3, -1, -7] → -1
```

---

## 6. Step 5: Debug

When your program has a bug:
1. **Read the error message** — it tells you the line and type of error.
2. **Print intermediate values** — add `print()` to see what's happening.
3. **Check types** — is the variable an `int` when you expect a `str`?
4. **Check edge cases** — does it work when N = 0 or the list is empty?

```python
# Debugging with print statements
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    print("DEBUG: added", num)   # temporary debug print
    numbers.append(num)
print("DEBUG: list =", numbers)  # check the list
```

---

## 7. Common Edge Cases

| Situation | Edge Case |
|-----------|-----------|
| List of numbers | Empty list, single item, all same |
| Division | Divisor = 0 |
| Finding max/min | All negative numbers |
| Counting | Count = 0 |
| String | Empty string |
| Loop | N = 0 (loop runs 0 times) |

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| problem solving | giải quyết vấn đề | The process of finding a solution |
| pseudocode | mã giả | Steps written in plain English, not real code |
| algorithm | thuật toán | A step-by-step procedure to solve a problem |
| debug | gỡ lỗi | Find and fix errors in code |
| test case | trường hợp kiểm tra | A specific input used to test the program |
| edge case | trường hợp biên | An unusual or extreme input |
| trace | theo dõi | Follow the code step by step |
| intermediate | trung gian | A value in the middle of a calculation |
| verify | xác minh | Check that the output is correct |
| strategy | chiến lược | A plan for solving a problem |
| decompose | phân tách | Break a big problem into smaller parts |
| step-by-step | từng bước | One step at a time |

---

## 9. Summary

✅ Always understand the problem before coding.
✅ Write pseudocode first — plan in English.
✅ Code step by step, following your plan.
✅ Test with normal inputs AND edge cases.
✅ Debug by printing intermediate values.
✅ Common edge cases: 0, negative numbers, empty input.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Plan First**

Write pseudocode (as comments) for this problem: "Read N numbers, print the sum." Then write the code.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The sum.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 30 |
| 5 | |
| 10 | |
| 8 | |
| 7 | |

---

**Exercise E2. Debug This**

The following code has a bug. Find and fix it:
```python
n = int(input())
total = 0
for i in range(1, n):   # BUG: should be range(1, n+1)
    total += i
print(total)
```
The program should print the sum of 1 + 2 + ... + N.

- **Input:** One integer N.
- **Output:** Sum from 1 to N.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 15 |

---

**Exercise E3. Edge Case — Empty**

Write a program that reads N numbers and prints the maximum. Handle the edge case where N = 0 (print "No numbers").

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The maximum, or "No numbers" if N = 0.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 9 |
| 5 | |
| 9 | |
| 3 | |

| Input | Output |
|-------|--------|
| 0 | No numbers |

---

**Exercise E4. Test Cases**

Write a function `is_even(n)`. Write 5 test cases (print the result for 5 different inputs) to verify it works correctly.

- **Input:** None (hardcode test values).
- **Output:** 5 test results.

---

**Exercise E5. Trace the Code**

Trace this code by hand (write what each variable is after each step), then run it to verify:
```python
x = 5
y = 3
x = x + y
y = x - y
x = x - y
print(x, y)
```

- **Input:** None.
- **Output:** The final values of x and y.

---

**Exercise E6. Plan and Code**

Write pseudocode then code for: "Read N numbers, count how many are greater than 10."

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The count.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 5 | |
| 15 | |
| 12 | |
| 8 | |
| 20 | |

---

**Exercise E7. Debug Division**

The following code crashes when b = 0. Fix it:
```python
a = int(input())
b = int(input())
print(a / b)   # crashes if b = 0
```

- **Input:** Two integers.
- **Output:** a / b, or "Cannot divide by zero" if b = 0.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 2.0 |
| 5 | |

| Input | Output |
|-------|--------|
| 10 | Cannot divide by zero |
| 0 | |

---

### 🟡 Medium

---

**Exercise M1. Step-by-Step Solution**

Solve this problem step by step (write pseudocode as comments): "Read N numbers, print the second largest."

- **Input:** First line: N (N ≥ 2). Next N lines: numbers (all different).
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

---

**Exercise M2. Test All Cases**

Write a function `grade(score)` that returns A/B/C/D/F. Write test cases for: 100, 90, 89, 80, 79, 70, 69, 60, 59, 0.

- **Input:** None (hardcode).
- **Output:** Grade for each test value.

---

**Exercise M3. Debug the Loop**

Find and fix the bug:
```python
# Should print: 1 2 3 4 5
for i in range(5):
    print(i)   # BUG: prints 0 1 2 3 4
```

- **Input:** None.
- **Output:**
```
1
2
3
4
5
```

---

**Exercise M4. Edge Case — Single Item**

Write a program that reads N numbers and prints the average. Handle N = 1 (just print that number) and N = 0 (print "No data").

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The average, or special message.

**Example:**

| Input | Output |
|-------|--------|
| 1 | 7.0 |
| 7 | |

| Input | Output |
|-------|--------|
| 0 | No data |

---

**Exercise M5. Verify with Multiple Tests**

Write `is_palindrome(s)` that checks if a string is a palindrome. Test with: "racecar", "hello", "level", "python", "madam".

- **Input:** None (hardcode).
- **Output:** True/False for each.

---

**Exercise M6. Plan a Complex Problem**

Write pseudocode (as comments) then code for: "Read N numbers, print how many are above average."

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Count of numbers above average.

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

---

**Exercise M7. Debug Index Error**

The following code crashes with an IndexError. Find and fix it:
```python
numbers = [10, 20, 30]
for i in range(4):   # BUG: should be range(3) or range(len(numbers))
    print(numbers[i])
```

- **Input:** None.
- **Output:**
```
10
20
30
```

---

### 🔴 Hard

---

**Exercise H1. Two Sum**

Read N numbers and a target T. Find two numbers in the list that add up to T. Print their indices. If no pair exists, print "No solution".

- **Input:** First line: N. Next N lines: numbers. Last line: T.
- **Output:** "i j" (indices of the two numbers), or "No solution".

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1 3 |
| 2 | |
| 7 | |
| 11 | |
| 15 | |
| 1 | |
| 9 | |

**Explanation:** numbers[1] + numbers[3] = 7 + 15 = 22? No. Let's check: 2+7=9 ✓ → indices 0 and 1. Wait, T=9: 2+7=9 → indices 0 and 1.

---

**Exercise H2. Rotate List**

Read N numbers and K. Rotate the list K positions to the right (the last K elements move to the front).

- **Input:** First line: N. Next N lines: numbers. Last line: K.
- **Output:** The rotated list.

**Example:**

| Input | Output |
|-------|--------|
| 5 | [4, 5, 1, 2, 3] |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 2 | |

**Explanation:** Rotate right by 2: [1,2,3,4,5] → [4,5,1,2,3].

---

**Exercise H3. Run-Length Encoding**

Read a string of letters. Encode it: count consecutive identical characters. "aaabbc" → "3a2b1c".

- **Input:** One string (lowercase letters, no spaces).
- **Output:** The run-length encoded string.

**Example:**

| Input | Output |
|-------|--------|
| aaabbc | 3a2b1c |
| aabbcc | 2a2b2c |
| abcde | 1a1b1c1d1e |

**Explanation:** Count consecutive identical characters and write count + character.

---

**Exercise H4. Missing Number**

Read N-1 numbers from 1 to N with one number missing. Find the missing number.

- **Input:** First line: N. Next N-1 lines: numbers (from 1 to N, one missing).
- **Output:** The missing number.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 3 |
| 1 | |
| 2 | |
| 4 | |
| 5 | |

**Explanation:** Sum of 1 to N = N*(N+1)/2. Subtract the sum of given numbers to find the missing one.

---

**Exercise H5. Palindrome Numbers**

Read N. Print all palindrome numbers from 1 to N.

- **Input:** One integer N.
- **Output:** All palindromes from 1 to N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 30 | 1 |
| | 2 |
| | ... |
| | 9 |
| | 11 |
| | 22 |

**Explanation:** A palindrome reads the same forwards and backwards.

---

**Exercise H6. Anagram Check**

Read two words. Print "anagram" if they use the same letters (same letters, same counts), else "not anagram".

- **Input:** Two lines, each with one word (lowercase).
- **Output:** "anagram" or "not anagram".

**Example:**

| Input | Output |
|-------|--------|
| listen | anagram |
| silent | |

| Input | Output |
|-------|--------|
| hello | not anagram |
| world | |

**Explanation:** Sort both words and compare. If sorted versions are equal, they are anagrams.

---

**Exercise H7. Longest Increasing Run**

Read N numbers. Find the length of the longest consecutive increasing subsequence (run).

- **Input:** First line: N. Next N lines: numbers.
- **Output:** The length of the longest increasing run.

**Example:**

| Input | Output |
|-------|--------|
| 8 | 4 |
| 1 | |
| 3 | |
| 5 | |
| 2 | |
| 8 | |
| 10 | |
| 12 | |
| 4 | |

**Explanation:** Runs: [1,3,5] (length 3), [2,8,10,12] (length 4), [4] (length 1). Longest = 4.
