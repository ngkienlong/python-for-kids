# Lesson 11: Loop Challenges 🏆

> **Goal:** Combine loops with conditions to filter numbers, find min/max, check primes, and solve FizzBuzz.

---

## 1. `if` Inside a Loop — Filtering

You can put an `if` statement inside a loop to only process certain values.

```python
# Print only even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

**Output:**
```
2
4
6
8
10
```

This is called **filtering** — you loop through all values but only act on the ones that match a condition.

---

## 2. Counting with a Condition

```python
# Count how many numbers from 1 to 20 are divisible by 3
count = 0
for i in range(1, 21):
    if i % 3 == 0:
        count = count + 1
print("Count:", count)
```

**Output:**
```
Count: 6
```

---

## 3. Finding Minimum and Maximum

```python
# Find the largest number from 1 to N that is divisible by 7
n = 50
largest = 0
for i in range(1, n + 1):
    if i % 7 == 0:
        largest = i    # keep updating — last one will be the largest
print("Largest multiple of 7 up to", n, ":", largest)
```

**Output:**
```
Largest multiple of 7 up to 50 : 49
```

---

## 4. FizzBuzz

FizzBuzz is a classic programming challenge:
- Print "Fizz" if the number is divisible by 3.
- Print "Buzz" if the number is divisible by 5.
- Print "FizzBuzz" if divisible by both 3 and 5.
- Otherwise print the number.

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

> ⚠️ Check `i % 3 == 0 and i % 5 == 0` **first** — otherwise "FizzBuzz" cases get caught by the earlier conditions.

---

## 5. Prime Number Check

A **prime number** is a number greater than 1 that has no divisors other than 1 and itself.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False    # found a divisor — not prime
    return True             # no divisors found — it's prime

# Test
for num in range(2, 20):
    if is_prime(num):
        print(num, "is prime")
```

**Output:**
```
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
```

*(We will learn `def` properly in Lesson 28. For now, just use the loop directly.)*

---

## 6. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| filter | lọc | Keep only values that match a condition |
| count | đếm | Keep track of how many items match |
| accumulate | tích lũy | Add up values over multiple iterations |
| prime | số nguyên tố | A number with exactly 2 divisors: 1 and itself |
| divisor | ước số | A number that divides another evenly |
| FizzBuzz | FizzBuzz | A classic coding challenge using divisibility |
| pattern | mẫu | A repeated structure in numbers or output |
| sequence | dãy số | Numbers arranged in a specific order |
| minimum | giá trị nhỏ nhất | The smallest value |
| maximum | giá trị lớn nhất | The largest value |

---

## 7. Summary

✅ Use `if` inside a loop to filter values.
✅ Use a counter variable to count how many values match a condition.
✅ To find the maximum: update a variable whenever you find a larger value.
✅ FizzBuzz: check divisible by both 3 and 5 first, then 3, then 5.
✅ Prime check: try dividing by every number from 2 to n-1.

---

## 8. Homework

### 🟢 Easy

---

**Exercise E1. Print Odd Numbers**

Print all odd numbers from 1 to 20.

- **Input:** None.
- **Output:**
```
1
3
5
7
9
11
13
15
17
19
```

---

**Exercise E2. Count Multiples of 4**

Count how many multiples of 4 are there from 1 to 40. Print the count.

- **Input:** None.
- **Output:**
```
10
```

---

**Exercise E3. Sum of Multiples of 5**

Calculate the sum of all multiples of 5 from 1 to 50.

- **Input:** None.
- **Output:**
```
275
```

---

**Exercise E4. FizzBuzz (1 to 15)**

Print FizzBuzz for numbers 1 to 15.

- **Input:** None.
- **Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

**Exercise E5. Find Maximum**

Find the largest multiple of 7 that is less than or equal to 100.

- **Input:** None.
- **Output:**
```
98
```

---

**Exercise E6. Count Primes to 20**

Count how many prime numbers are there from 2 to 20.

- **Input:** None.
- **Output:**
```
8
```

*(Primes: 2, 3, 5, 7, 11, 13, 17, 19.)*

---

**Exercise E7. Print Squares Under 100**

Print all perfect squares (1, 4, 9, 16, ...) that are less than 100.

- **Input:** None.
- **Output:**
```
1
4
9
16
25
36
49
64
81
```

---

### 🟡 Medium

---

**Exercise M1. Sum of Primes**

Calculate the sum of all prime numbers from 2 to 50.

- **Input:** None.
- **Output:**
```
328
```

---

**Exercise M2. Digit Sum of All Numbers**

Calculate the sum of digit-sums of all numbers from 1 to 20. (Digit sum of 15 = 1+5 = 6.)

- **Input:** None.
- **Output:**
```
102
```

---

**Exercise M3. Count Numbers with Digit Sum 10**

Count how many numbers from 1 to 100 have a digit sum equal to 10.

- **Input:** None.
- **Output:**
```
4
```

*(Numbers: 19, 28, 37, 46, 55, 64, 73, 82, 91, 100 — wait, 100 has digit sum 1. Let me recount: 19→10✓, 28→10✓, 37→10✓, 46→10✓, 55→10✓, 64→10✓, 73→10✓, 82→10✓, 91→10✓ → 9 numbers.)*

- **Output:**
```
9
```

---

**Exercise M4. Longest Even Run**

Find the longest consecutive sequence of even numbers from 1 to 30. (Hint: even numbers are never consecutive, so find the longest run of numbers where each is even — actually find the count of even numbers.)

Print all even numbers from 1 to 30 and their count.

- **Input:** None.
- **Output:** Print each even number, then print the total count.

---

**Exercise M5. Find Min and Max**

Read 5 numbers from the user (one per line). Find and print the minimum and maximum.

- **Input:** 5 integers.
- **Output:** Two lines: the minimum and the maximum.

**Example:**

| Input | Output |
|-------|--------|
| 3 7 1 9 4 | 1 |
| | 9 |

---

**Exercise M6. Numbers Not Divisible by 2 or 3**

Print all numbers from 1 to 30 that are not divisible by 2 or 3.

- **Input:** None.
- **Output:**
```
1
5
7
11
13
17
19
23
25
29
```

---

**Exercise M7. Abundant Numbers**

A number N is "abundant" if the sum of its proper divisors (divisors less than N) is greater than N. Find all abundant numbers from 1 to 50.

- **Input:** None.
- **Output:** All abundant numbers from 1 to 50, one per line.

*(First few: 12, 18, 20, 24, ...)*

---

### 🔴 Hard

---

**Exercise H1. FizzBuzz 1 to N**

A teacher plays FizzBuzz with her class. She calls out numbers from 1 to N. Students say "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the number otherwise. Write the program.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** N lines of FizzBuzz output.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 1 |
| | 2 |
| | Fizz |
| | 4 |
| | Buzz |
| | Fizz |
| | 7 |

---

**Exercise H2. Count Primes Up to N**

A mathematician wants to know how many prime numbers exist from 2 to N. Write a program to count them.

- **Input:** One integer N (2 ≤ N ≤ 1000).
- **Output:** One integer — the count of prime numbers from 2 to N.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 4 |
| 20 | 8 |
| 100 | 25 |

**Explanation:** Primes up to 10: 2, 3, 5, 7 → 4 primes.

---

**Exercise H3. Sum of Digit Sums**

A student adds up the digit-sums of all numbers from 1 to N. For example, for N=12: digit sums are 1,2,3,4,5,6,7,8,9,1,2,3 → total = 51. Write a program to calculate this.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** One integer — the sum of all digit-sums from 1 to N.

**Example:**

| Input | Output |
|-------|--------|
| 9 | 45 |
| 12 | 51 |
| 100 | 901 |

---

**Exercise H4. Largest Divisor**

A locksmith needs to find the largest divisor of a lock code N (other than N itself). Write a program to find it.

- **Input:** One integer N (2 ≤ N ≤ 1000000).
- **Output:** One integer — the largest divisor of N other than N itself.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 6 |
| 7 | 1 |
| 100 | 50 |

**Explanation:** Divisors of 12: 1, 2, 3, 4, 6, 12. Largest other than 12 is 6.

---

**Exercise H5. Goldbach Check**

Goldbach's conjecture says every even number ≥ 4 can be written as the sum of two prime numbers. Given an even number N, find two primes that add up to N.

- **Input:** One even integer N (4 ≤ N ≤ 1000).
- **Output:** Two primes p and q such that p + q = N (print the smallest p first).

**Example:**

| Input | Output |
|-------|--------|
| 10 | 3 7 |
| 28 | 5 23 |
| 4 | 2 2 |

---

**Exercise H6. Count Perfect Squares**

A student counts how many perfect squares (1, 4, 9, 16, ...) exist from 1 to N. Write a program to count them.

- **Input:** One integer N (1 ≤ N ≤ 1000000).
- **Output:** One integer — the count of perfect squares from 1 to N.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 3 |
| 100 | 10 |
| 1000 | 31 |

**Explanation:** Perfect squares up to 10: 1, 4, 9 → 3.

---

**Exercise H7. Longest Run**

A weather station records N temperature readings. Find the longest consecutive run of the same temperature value.

- **Input:** First line: integer N (1 ≤ N ≤ 1000). Then N integers, one per line.
- **Output:** One integer — the length of the longest consecutive run of the same number.

**Example:**

| Input | Output |
|-------|--------|
| 8 | 3 |
| 1 | |
| 2 | |
| 2 | |
| 2 | |
| 3 | |
| 3 | |
| 1 | |
| 1 | |

**Explanation:** The run of three 2s is the longest (length 3).
