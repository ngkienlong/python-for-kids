# Lesson 25: Answers 🔄

---

## 🟢 Easy

**E1.**
```python
animals = ["cat", "dog", "bird", "fish"]
for animal in animals:
    print(animal)
```

**E2.**
```python
colors = ["red", "green", "blue", "yellow"]
for i in range(len(colors)):
    print(i, colors[i])
```

**E3.**
```python
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(total)
```

**E4.**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(count)
```

**E5.**
```python
scores = [72, 95, 88, 61, 79]
maximum = scores[0]
for score in scores:
    if score > maximum:
        maximum = score
print(maximum)
```

**E6.**
```python
numbers = [3, 5, 7, 9]
for num in numbers:
    print(num * 2)
```

**E7.**
```python
letters = ["a", "b", "a", "c", "a", "b"]
count = 0
for letter in letters:
    if letter == "a":
        count += 1
print(count)
```

---

## 🟡 Medium

**M1.**
```python
n = int(input())
items = []
for i in range(n):
    items.append(input())
for i in range(n):
    print(str(i + 1) + ". " + items[i])
```

**M2.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)
```

**M3.**
```python
n = int(input())
names = []
for i in range(n):
    names.append(input())
target = input()
found = False
for name in names:
    if name == target:
        found = True
if found:
    print("found")
else:
    print("not found")
```

**M4.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
count = 0
for num in numbers:
    if num > 50:
        count += 1
print(count)
```

**M5.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(n - 1, -1, -1):
    print(numbers[i])
```

**M6.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
total = 0
for num in numbers:
    total += num
average = total / n
print(round(average, 2))
```

**M7.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for num in numbers:
    if num > 0:
        print(num)
```

---

## 🔴 Hard

**H1.**
```python
# Sum and average
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

total = 0
for num in numbers:
    total += num
average = total / n

print("Sum:", total)
print("Average:", round(average, 2))
```

**H2.**
```python
# Find maximum without max()
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)
```

**H3.**
```python
# Find minimum without min()
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)
```

**H4.**
```python
# Search with index
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
t = int(input())

found = False
for i in range(len(numbers)):
    if numbers[i] == t:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")
```

**H5.**
```python
# Count numbers above average
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

total = 0
for num in numbers:
    total += num
average = total / n

count = 0
for num in numbers:
    if num > average:
        count += 1
print(count)
```
*Explanation: First calculate the average, then loop again to count how many numbers exceed it.*

**H6.**
```python
# Reverse with loop
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in range(n - 1, -1, -1):
    print(numbers[i])
```
*Explanation: `range(n-1, -1, -1)` counts from the last index down to 0.*

**H7.**
```python
# Second largest number
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find the maximum first
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Find the largest number that is less than the maximum
second = None
for num in numbers:
    if num < maximum:
        if second is None or num > second:
            second = num

print(second)
```
*Explanation: First find the maximum. Then find the largest number that is strictly less than the maximum — that is the second largest.*
