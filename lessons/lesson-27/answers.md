# Lesson 27: Answers 🔢

---

## 🟢 Easy

**E1.**
```python
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)
```

**E2.**
```python
numbers = [-3, 5, -1, 8, 0, -2, 7]
for num in numbers:
    if num > 0:
        print(num)
```

**E3.**
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num * num
print(total)
```

**E4.**
```python
temperatures = [23, 17, 31, 28, 15, 25, 19]
print(max(temperatures) - min(temperatures))
```

**E5.**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
```

**E6.**
```python
numbers = [5, 10, 15, 20, 25]
running = 0
for num in numbers:
    running += num
    print(running)
```

**E7.**
```python
numbers = [3, 6, 9, 12]
doubled = [x * 2 for x in numbers]
print(doubled)
```

---

## 🟡 Medium

**M1.**
```python
numbers = []
for i in range(5):
    numbers.append(int(input()))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
```

**M2.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for num in numbers:
    if num % 2 == 0:
        print(num)
```

**M3.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
average = sum(numbers) / len(numbers)
for num in numbers:
    if num > average:
        print(num)
```

**M4.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
maximum = max(numbers)
for num in numbers:
    print(round(num / maximum, 2))
```

**M5.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
running = 0
for num in numbers:
    running += num
    print(running)
```

**M6.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
d = int(input())
count = 0
for num in numbers:
    if num % d == 0:
        count += 1
print(count)
```

**M7.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
squares = [x * x for x in numbers]
print(squares)
```

---

## 🔴 Hard

**H1.**
```python
# Full statistics
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

total = sum(numbers)
average = total / n
minimum = min(numbers)
maximum = max(numbers)
data_range = maximum - minimum

print("Sum:", total)
print("Average:", round(average, 2))
print("Min:", minimum)
print("Max:", maximum)
print("Range:", data_range)
```

**H2.**
```python
# Print only even numbers
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for num in numbers:
    if num % 2 == 0:
        print(num)
```

**H3.**
```python
# Count numbers above average
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

**H4.**
```python
# Sum of squares
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
total = 0
for num in numbers:
    total += num * num
print(total)
```

**H5.**
```python
# Normalize
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
maximum = max(numbers)
for num in numbers:
    print(round(num / maximum, 2))
```
*Explanation: Divide each value by the maximum. All results will be between 0.0 and 1.0.*

**H6.**
```python
# Cumulative sum
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
running = 0
for num in numbers:
    running += num
    print(running)
```
*Explanation: Keep a running total. After adding each number, print the current total.*

**H7.**
```python
# Count increases
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
count = 0
for i in range(n - 1):
    if numbers[i + 1] > numbers[i]:
        count += 1
print(count)
```
*Explanation: Compare each pair of adjacent elements. If the next one is larger, it is an increase. Loop from index 0 to n-2 (so i+1 is always valid).*
