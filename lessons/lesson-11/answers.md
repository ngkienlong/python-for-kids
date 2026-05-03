# Lesson 11: Answers — Loop Challenges

---

## 🟢 Easy

**E1. Print Odd Numbers**
```python
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
```

**E2. Count Multiples of 4**
```python
count = 0
for i in range(1, 41):
    if i % 4 == 0:
        count = count + 1
print(count)
```

**E3. Sum of Multiples of 5**
```python
total = 0
for i in range(5, 51, 5):
    total = total + i
print(total)
```

**E4. FizzBuzz (1 to 15)**
```python
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**E5. Find Maximum**
```python
largest = 0
for i in range(1, 101):
    if i % 7 == 0:
        largest = i
print(largest)
```

**E6. Count Primes to 20**
```python
count = 0
for n in range(2, 21):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count = count + 1
print(count)
```

**E7. Print Squares Under 100**
```python
i = 1
while i * i < 100:
    print(i * i)
    i = i + 1
```

---

## 🟡 Medium

**M1. Sum of Primes**
```python
total = 0
for n in range(2, 51):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        total = total + n
print(total)
```

**M2. Digit Sum of All Numbers**
```python
grand_total = 0
for n in range(1, 21):
    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum = digit_sum + temp % 10
        temp = temp // 10
    grand_total = grand_total + digit_sum
print(grand_total)
```

**M3. Count Numbers with Digit Sum 10**
```python
count = 0
for n in range(1, 101):
    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum = digit_sum + temp % 10
        temp = temp // 10
    if digit_sum == 10:
        count = count + 1
print(count)
```

**M4. Even Numbers 1 to 30**
```python
count = 0
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
        count = count + 1
print("Count:", count)
```

**M5. Find Min and Max**
```python
first = int(input())
min_val = first
max_val = first
for i in range(4):
    n = int(input())
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
print(min_val)
print(max_val)
```

**M6. Numbers Not Divisible by 2 or 3**
```python
for i in range(1, 31):
    if i % 2 != 0 and i % 3 != 0:
        print(i)
```

**M7. Abundant Numbers**
```python
for n in range(1, 51):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum = divisor_sum + i
    if divisor_sum > n:
        print(n)
```

---

## 🔴 Hard

**H1. FizzBuzz 1 to N**
```python
n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
*Always check divisible by both 3 AND 5 first, otherwise FizzBuzz cases get caught early.*

**H2. Count Primes Up to N**
```python
n = int(input())
count = 0
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count = count + 1
print(count)
```
*For each number, check if any number from 2 to num-1 divides it. If none do, it's prime.*

**H3. Sum of Digit Sums**
```python
n = int(input())
grand_total = 0
for num in range(1, n + 1):
    temp = num
    while temp > 0:
        grand_total = grand_total + temp % 10
        temp = temp // 10
print(grand_total)
```
*For each number from 1 to N, extract its digits and add them all to the grand total.*

**H4. Largest Divisor**
```python
n = int(input())
largest = 1
for i in range(2, n):
    if n % i == 0:
        largest = i
print(largest)
```
*Loop from 2 to n-1. Every time we find a divisor, update largest. The last one found is the biggest.*

**H5. Goldbach Check**
```python
n = int(input())
for p in range(2, n):
    # Check if p is prime
    p_prime = True
    for i in range(2, p):
        if p % i == 0:
            p_prime = False
            break
    if not p_prime:
        continue
    q = n - p
    # Check if q is prime
    if q < 2:
        continue
    q_prime = True
    for i in range(2, q):
        if q % i == 0:
            q_prime = False
            break
    if q_prime:
        print(p, q)
        break
```
*Try each prime p from 2 upward. Check if n-p is also prime. Print the first pair found.*

**H6. Count Perfect Squares**
```python
n = int(input())
count = 0
i = 1
while i * i <= n:
    count = count + 1
    i = i + 1
print(count)
```
*Count how many integers i satisfy i² ≤ N. Stop when i² exceeds N.*

**H7. Longest Run**
```python
n = int(input())
first = int(input())
current_val = first
current_run = 1
longest_run = 1
for i in range(n - 1):
    val = int(input())
    if val == current_val:
        current_run = current_run + 1
        if current_run > longest_run:
            longest_run = current_run
    else:
        current_val = val
        current_run = 1
print(longest_run)
```
*Track the current run length. When the value changes, reset. Keep updating the longest run seen.*
