# Lesson 24: Answers 📋

---

## 🟢 Easy

**E1.**
```python
colors = ["red", "blue", "green"]
print(colors)
```

**E2.**
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
```

**E3.**
```python
animals = ["cat", "dog", "bird", "fish", "rabbit"]
print(animals[2])
```

**E4.**
```python
scores = [85, 92, 78, 95, 88, 76, 91]
print(len(scores))
```

**E5.**
```python
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
print(numbers)
```

**E6.**
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)
```

**E7.**
```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[-3])
print(days[-2])
print(days[-1])
```

---

## 🟡 Medium

**M1.**
```python
names = []
name1 = input()
name2 = input()
name3 = input()
names.append(name1)
names.append(name2)
names.append(name3)
print(names)
```

**M2.**
```python
colors = ["red", "green", "blue", "yellow", "purple"]
k = int(input())
print(colors[k])
```

**M3.**
```python
items = ["pen", "book"]
item1 = input()
item2 = input()
item3 = input()
items.append(item1)
items.append(item2)
items.append(item3)
print(items)
print(len(items))
```

**M4.**
```python
numbers = [1, 2, 3, 4, 5]
k = int(input())
v = int(input())
numbers[k] = v
print(numbers)
```

**M5.**
```python
prices = [15, 25, 10, 30, 20]
print(sum(prices))
```

**M6.**
```python
numbers = [3, 7, 1, 9, 5]
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[-1])
```

**M7.**
```python
items = ["A", "B", "C", "D"]
temp = items[0]
items[0] = items[-1]
items[-1] = temp
print(items)
```

---

## 🔴 Hard

**H1.**
```python
# Read N numbers into a list
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
print(numbers)
```

**H2.**
```python
# Print first and last element
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
print(numbers[0])
print(numbers[-1])
```

**H3.**
```python
# Print element at position K
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
k = int(input())
print(numbers[k])
```

**H4.**
```python
# Replace element at position K with value V
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
k = int(input())
v = int(input())
numbers[k] = v
print(numbers)
```

**H5.**
```python
# Print list in reverse using negative indexing
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
for i in range(1, n + 1):
    print(numbers[-i])
```
*Explanation: We loop `i` from 1 to N, and print `numbers[-i]`. When i=1, we get the last item; when i=N, we get the first item.*

**H6.**
```python
# Print a numbered shopping list
n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)
for i in range(n):
    print(str(i + 1) + ". " + items[i])
```
*Explanation: Use `i + 1` as the display number since index starts at 0.*

**H7.**
```python
# Count positive, negative, and zero numbers
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
```
*Explanation: Loop through the list and use if/elif/else to classify each number, then print the three counts.*
