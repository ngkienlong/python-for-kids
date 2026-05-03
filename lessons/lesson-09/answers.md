# Lesson 9: Answers — While Loop

---

## 🟢 Easy

**E1. Count to 10**
```python
count = 1
while count <= 10:
    print(count)
    count = count + 1
```

**E2. Count Down**
```python
count = 5
while count >= 1:
    print(count)
    count = count - 1
print("Done!")
```

**E3. Sum to 100**
```python
total = 0
i = 1
while total < 100:
    total = total + i
    i = i + 1
print(total)
```

**E4. Powers of 2**
```python
n = 1
while n < 1000:
    print(n)
    n = n * 2
```

**E5. Break at 7**
```python
count = 1
while True:
    if count == 7:
        break
    print(count)
    count = count + 1
```

**E6. Repeat Until Positive**
```python
n = int(input())
while n <= 0:
    n = int(input())
print(n)
```

**E7. Multiply Up**
```python
n = 1
while n <= 100:
    n = n * 2
print(n)
```

---

## 🟡 Medium

**M1. Guess the Number**
```python
secret = 7
guess = int(input())
while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input())
print("Correct!")
```

**M2. Sum of Positives**
```python
total = 0
n = int(input())
while n != 0:
    if n > 0:
        total = total + n
    n = int(input())
print(total)
```

**M3. Count Digits**
```python
n = int(input())
count = 0
temp = n
while temp > 0:
    count = count + 1
    temp = temp // 10
print(count)
```

**M4. Fibonacci Sequence**
```python
a = 1
b = 1
while a < 100:
    print(a)
    a, b = b, a + b
```

**M5. Divisor Check**
```python
n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i + 1
```

**M6. Reverse Digits**
```python
n = int(input())
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10
print(reversed_n)
```

**M7. Collatz Steps**
```python
n = int(input())
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    steps = steps + 1
print(steps)
```

---

## 🔴 Hard

**H1. Sum Until Zero**
```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```
*Read numbers one by one. Add each to total. Stop when 0 is entered.*

**H2. Count Digits**
```python
n = int(input())
count = 0
temp = n
while temp > 0:
    count = count + 1
    temp = temp // 10
print(count)
```
*Divide by 10 repeatedly. Each division removes one digit. Count how many times you divide.*

**H3. Collatz Sequence**
```python
n = int(input())
print(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(n)
```
*Print N first, then apply the rule and print each new value until reaching 1.*

**H4. Reverse a Number**
```python
n = int(input())
reversed_n = 0
while n > 0:
    digit = n % 10          # get last digit
    reversed_n = reversed_n * 10 + digit  # append to reversed number
    n = n // 10             # remove last digit
print(reversed_n)
```
*Extract digits from right to left using `% 10`, build the reversed number by shifting left (`* 10`) and adding.*

**H5. Find First Multiple**
```python
n = int(input())
k = int(input())
multiple = k
while multiple <= n:
    multiple = multiple + k
print(multiple)
```
*Start at K and keep adding K until the multiple exceeds N.*

**H6. Power Without `**`**
```python
base = int(input())
exp = int(input())
result = 1
count = 0
while count < exp:
    result = result * base
    count = count + 1
print(result)
```
*Multiply result by base, exp times. Start result at 1 (so base^0 = 1 works correctly).*

**H7. Number of Divisors**
```python
n = int(input())
count = 0
i = 1
while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1
print(count)
```
*Check every number from 1 to N. If it divides N evenly (remainder 0), count it.*
