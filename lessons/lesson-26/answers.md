# Lesson 26: Answers ✂️

---

## 🟢 Easy

**E1.**
```python
numbers = [5, 2, 8, 1, 9, 3, 7]
numbers.sort()
print(numbers)
```

**E2.**
```python
numbers = [5, 2, 8, 1, 9, 3, 7]
numbers.sort(reverse=True)
print(numbers)
```

**E3.**
```python
fruits = ["apple", "banana", "cherry", "mango"]
fruits.reverse()
print(fruits)
```

**E4.**
```python
colors = ["red", "blue", "green", "blue", "yellow"]
colors.remove("blue")
print(colors)
```

**E5.**
```python
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)
```

**E6.**
```python
items = ["pen", "book", "ruler", "eraser"]
popped = items.pop()
print(popped)
print(items)
```

**E7.**
```python
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])
```

---

## 🟡 Medium

**M1.**
```python
scores = [72, 95, 88, 61, 79, 84, 91]
scores.sort(reverse=True)
print(scores[0])
print(scores[1])
print(scores[2])
```

**M2.**
```python
letters = ["a", "b", "c", "a", "d", "a"]
print("Count:", letters.count("a"))
print("First index:", letters.index("a"))
```

**M3.**
```python
numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
print(numbers)
```

**M4.**
```python
numbers = []
for i in range(5):
    numbers.append(int(input()))
k = int(input())
v = int(input())
numbers.insert(k, v)
print(numbers)
```

**M5.**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:7])
```

**M6.**
```python
names = []
for i in range(5):
    names.append(input())
names.sort()
for name in names:
    print(name)
```

**M7.**
```python
stack = [1, 2, 3, 4, 5]
while len(stack) > 0:
    print(stack.pop())
```

---

## 🔴 Hard

**H1.**
```python
# Sort N numbers
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort()
print(numbers)
```

**H2.**
```python
# Top 3 largest
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort(reverse=True)
print(numbers[0])
print(numbers[1])
print(numbers[2])
```

**H3.**
```python
# Remove all occurrences of V
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
v = int(input())
while v in numbers:
    numbers.remove(v)
print(numbers)
```
*Explanation: Use a while loop to keep removing V as long as it exists in the list.*

**H4.**
```python
# Insert V at position K
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
k = int(input())
v = int(input())
numbers.insert(k, v)
print(numbers)
```

**H5.**
```python
# Find the median
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort()
if n % 2 == 1:
    print(numbers[n // 2])
else:
    mid1 = numbers[n // 2 - 1]
    mid2 = numbers[n // 2]
    print((mid1 + mid2) / 2)
```
*Explanation: After sorting, the median is the middle element. For even N, average the two middle elements.*

**H6.**
```python
# Find the mode (most frequent value)
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()   # sort so ties go to smallest value
mode = numbers[0]
max_count = 0

for num in numbers:
    c = numbers.count(num)
    if c > max_count:
        max_count = c
        mode = num

print(mode)
```
*Explanation: Sort first so that when counts are equal, the smallest value is checked first. Track the value with the highest count.*

**H7.**
```python
# Remove duplicates, keep original order
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)
```
*Explanation: Build a new list. For each number, only add it if it is not already in the new list.*
