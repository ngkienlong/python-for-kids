# Lesson 33: Answers 🧠

---

## 🟢 Easy

**E1.**
```python
# Pseudocode:
# 1. Read N
# 2. Read N numbers into a list
# 3. Calculate sum
# 4. Print sum

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
print(sum(numbers))
```

**E2.**
```python
# Bug: range(1, n) misses n. Fix: range(1, n+1)
n = int(input())
total = 0
for i in range(1, n + 1):   # FIXED
    total += i
print(total)
```

**E3.**
```python
n = int(input())
if n == 0:
    print("No numbers")
else:
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    print(max(numbers))
```

**E4.**
```python
def is_even(n):
    return n % 2 == 0

# Test cases
print(is_even(4))    # True
print(is_even(7))    # False
print(is_even(0))    # True
print(is_even(-2))   # True
print(is_even(13))   # False
```

**E5.**
```python
# Trace:
# x = 5, y = 3
# x = x + y = 5 + 3 = 8
# y = x - y = 8 - 3 = 5
# x = x - y = 8 - 5 = 3
# Result: x = 3, y = 5  (the values are swapped!)
x = 5
y = 3
x = x + y
y = x - y
x = x - y
print(x, y)   # 3 5
```

**E6.**
```python
# Pseudocode:
# 1. Read N
# 2. Read N numbers
# 3. Set count = 0
# 4. For each number: if > 10, count += 1
# 5. Print count

n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num > 10:
        count += 1
print(count)
```

**E7.**
```python
a = int(input())
b = int(input())
if b == 0:
    print("Cannot divide by zero")
else:
    print(a / b)
```

---

## 🟡 Medium

**M1.**
```python
# Pseudocode:
# 1. Read N numbers into a list
# 2. Find the maximum
# 3. Find the largest number that is less than the maximum
# 4. Print it

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Find second largest
second = None
for num in numbers:
    if num < maximum:
        if second is None or num > second:
            second = num

print(second)
```

**M2.**
```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_values = [100, 90, 89, 80, 79, 70, 69, 60, 59, 0]
for score in test_values:
    print(score, "->", grade(score))
```

**M3.**
```python
# Bug: range(5) gives 0,1,2,3,4. Fix: range(1, 6)
for i in range(1, 6):   # FIXED
    print(i)
```

**M4.**
```python
n = int(input())
if n == 0:
    print("No data")
elif n == 1:
    num = float(input())
    print(num)
else:
    numbers = []
    for i in range(n):
        numbers.append(float(input()))
    print(sum(numbers) / n)
```

**M5.**
```python
def is_palindrome(s):
    return s == s[::-1]

words = ["racecar", "hello", "level", "python", "madam"]
for word in words:
    print(word, "->", is_palindrome(word))
```

**M6.**
```python
# Pseudocode:
# 1. Read N numbers
# 2. Calculate average
# 3. Count numbers > average
# 4. Print count

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

average = sum(numbers) / n
count = 0
for num in numbers:
    if num > average:
        count += 1
print(count)
```

**M7.**
```python
# Bug: range(4) goes to index 3, but list only has indices 0,1,2
numbers = [10, 20, 30]
for i in range(len(numbers)):   # FIXED
    print(numbers[i])
```

---

## 🔴 Hard

**H1.**
```python
# Two Sum: find two numbers that add up to T
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
t = int(input())

found = False
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] + numbers[j] == t:
            print(i, j)
            found = True
            break
    if found:
        break

if not found:
    print("No solution")
```
*Explanation: Use two nested loops to check every pair of indices (i, j) where i < j. If their sum equals T, print the indices.*

**H2.**
```python
# Rotate list K positions to the right
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
k = int(input())

k = k % n   # handle k > n
rotated = numbers[n - k:] + numbers[:n - k]
print(rotated)
```
*Explanation: Rotating right by K means the last K elements move to the front. Use slicing: `numbers[n-k:]` is the last K elements, `numbers[:n-k]` is the rest.*

**H3.**
```python
# Run-length encoding
s = input()
result = ""
i = 0
while i < len(s):
    char = s[i]
    count = 1
    while i + count < len(s) and s[i + count] == char:
        count += 1
    result += str(count) + char
    i += count
print(result)
```
*Explanation: Use a pointer i. For each position, count how many consecutive identical characters follow. Append count+char to result, then advance i by count.*

**H4.**
```python
# Missing number using sum formula
n = int(input())
expected_sum = n * (n + 1) // 2
actual_sum = 0
for i in range(n - 1):
    actual_sum += int(input())
print(expected_sum - actual_sum)
```
*Explanation: The sum of 1 to N is N*(N+1)/2. Subtract the sum of the given numbers to find the missing one.*

**H5.**
```python
# All palindrome numbers from 1 to N
n = int(input())
for i in range(1, n + 1):
    s = str(i)
    if s == s[::-1]:
        print(i)
```

**H6.**
```python
# Anagram check
word1 = input()
word2 = input()
if sorted(word1) == sorted(word2):
    print("anagram")
else:
    print("not anagram")
```
*Explanation: Sort both words. If the sorted versions are equal, the words use the same letters with the same counts — they are anagrams.*

**H7.**
```python
# Longest increasing run
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

if n == 0:
    print(0)
else:
    max_length = 1
    current_length = 1
    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1
    print(max_length)
```
*Explanation: Track the current run length. When the next number is larger, extend the run. When it is not, reset to 1. Keep track of the maximum run length seen.*
