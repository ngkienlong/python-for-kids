# Lesson 31: Functions + Math 🔢

> **Goal:** Write math helper functions, build a mini calculator, and get a gentle introduction to recursion.

---

## 1. Math Helper Functions

Functions are perfect for math calculations you use often:

```python
import math

def area_circle(r):
    return math.pi * r * r

def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

print(area_circle(5))        # 78.54...
print(hypotenuse(3, 4))      # 5.0
print(is_perfect_square(16)) # True
print(is_perfect_square(10)) # False
```

---

## 2. Functions Calling Other Functions

Functions can call other functions:

```python
def bmi(weight, height):
    return weight / (height * height)

def bmi_category(weight, height):
    b = bmi(weight, height)   # call bmi() from inside bmi_category()
    if b < 18.5:
        return "Underweight"
    elif b < 25:
        return "Normal"
    elif b < 30:
        return "Overweight"
    else:
        return "Obese"

print(bmi_category(60, 1.70))   # Normal
```

---

## 3. Mini Calculator with Functions

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

# Menu-driven calculator
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose: "))
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
```

---

## 4. Introduction to Recursion

**Recursion** means a function calls itself. It needs a **base case** to stop.

```python
def factorial(n):
    if n == 0:          # base case: stop here
        return 1
    return n * factorial(n - 1)   # recursive call

print(factorial(5))   # 5 × 4 × 3 × 2 × 1 = 120
print(factorial(0))   # 1
```

How it works:
```
factorial(4)
= 4 × factorial(3)
= 4 × 3 × factorial(2)
= 4 × 3 × 2 × factorial(1)
= 4 × 3 × 2 × 1 × factorial(0)
= 4 × 3 × 2 × 1 × 1
= 24
```

> ⚠️ Always have a base case! Without it, the function calls itself forever.

---

## 5. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| helper function | hàm hỗ trợ | A function that does one small task |
| calculator | máy tính | A program that performs math operations |
| menu | menu | A list of choices for the user |
| recursive | đệ quy | A function that calls itself |
| base case | trường hợp cơ sở | The condition that stops recursion |
| call stack | ngăn xếp lời gọi | The list of function calls waiting to finish |
| organize | tổ chức | Arrange code into logical sections |
| decompose | phân tách | Break a big problem into smaller parts |
| modular | mô-đun hóa | Organized into separate, reusable pieces |
| reuse | tái sử dụng | Use the same function in multiple places |

---

## 6. Summary

✅ Write math helper functions for calculations you use often.
✅ Functions can call other functions.
✅ A menu-driven calculator uses functions for each operation.
✅ Recursion: a function calls itself with a smaller input.
✅ Every recursive function needs a base case to stop.

---

## 7. Homework

### 🟢 Easy

---

**Exercise E1. Area Functions**

Write `area_square(s)`, `area_rectangle(w, h)`, and `area_triangle(b, h)`. Test each with sample values.

- **Input:** None (hardcode values).
- **Output:** Three areas.

**Example:**
```
Area of square (5): 25
Area of rectangle (4, 6): 24
Area of triangle (3, 8): 12.0
```

---

**Exercise E2. Is Divisible**

Write `is_divisible(n, d)` that returns `True` if n is divisible by d. Test with several pairs.

- **Input:** None.
- **Output:** True/False for each pair.

**Example:**
```
10 divisible by 2: True
10 divisible by 3: False
15 divisible by 5: True
```

---

**Exercise E3. Factorial**

Write `factorial(n)` using a loop (not recursion). Print factorial of 1 through 7.

- **Input:** None.
- **Output:**
```
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
```

---

**Exercise E4. Power Function**

Write `power(base, exp)` using a loop. Print 2^0 through 2^10.

- **Input:** None.
- **Output:**
```
2^0 = 1
2^1 = 2
...
2^10 = 1024
```

---

**Exercise E5. Is Prime**

Write `is_prime(n)`. Print all primes from 2 to 30.

- **Input:** None.
- **Output:**
```
2 3 5 7 11 13 17 19 23 29
```

---

**Exercise E6. Digit Sum**

Write `digit_sum(n)` that returns the sum of digits. Test with 123, 456, 9999.

- **Input:** None.
- **Output:**
```
digit_sum(123) = 6
digit_sum(456) = 15
digit_sum(9999) = 36
```

---

**Exercise E7. Recursive Factorial**

Write `factorial(n)` using recursion. Print factorial of 0 through 6.

- **Input:** None.
- **Output:**
```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
```

---

### 🟡 Medium

---

**Exercise M1. Simple Calculator**

Write functions `add`, `subtract`, `multiply`, `divide`. Read two numbers and an operator (+, -, *, /). Print the result.

- **Input:** Two numbers (one per line), then an operator.
- **Output:** The result.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 30.0 |
| 3 | |
| * | |

---

**Exercise M2. GCD**

Write `gcd(a, b)` using the Euclidean algorithm (while a != b: if a > b: a -= b else: b -= a). Read two numbers, print their GCD.

- **Input:** Two integers.
- **Output:** Their GCD.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 4 |
| 8 | |

---

**Exercise M3. Perfect Number**

Write `is_perfect(n)` that returns True if n equals the sum of its proper divisors (e.g., 6 = 1+2+3). Print all perfect numbers up to 500.

- **Input:** None.
- **Output:**
```
6
28
496
```

---

**Exercise M4. Collatz**

Write `collatz_steps(n)` that counts how many steps the Collatz sequence takes to reach 1 (if even: n//2, if odd: 3n+1). Read N, print the steps.

- **Input:** One integer N.
- **Output:** Number of steps.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 8 |

---

**Exercise M5. Fibonacci with Function**

Write `fibonacci(n)` that returns the nth Fibonacci number. Print fib(1) through fib(10).

- **Input:** None.
- **Output:**
```
fib(1) = 1
fib(2) = 1
...
fib(10) = 55
```

---

**Exercise M6. BMI Calculator**

Write `bmi(weight, height)` and `bmi_category(bmi_value)`. Read weight (kg) and height (m), print BMI and category.

- **Input:** Two numbers: weight and height.
- **Output:** BMI (2 decimal places) and category.

**Example:**

| Input | Output |
|-------|--------|
| 60 | BMI: 20.76 |
| 1.70 | Category: Normal |

---

**Exercise M7. Number to Words (1-10)**

Write `number_to_word(n)` that returns the English word for numbers 1-10. Read N numbers, print each as a word.

- **Input:** First line: N. Next N lines: numbers (1-10).
- **Output:** The word for each number.

**Example:**

| Input | Output |
|-------|--------|
| 3 | three |
| 3 | seven |
| 7 | one |
| 1 | |

---

### 🔴 Hard

---

**Exercise H1. Full Calculator**

Write functions for +, -, *, /. Read an operator and two numbers. Print the result. Handle division by zero.

- **Input:** First line: operator (+, -, *, /). Next two lines: numbers.
- **Output:** The result (2 decimal places), or an error message.

**Example:**

| Input | Output |
|-------|--------|
| + | 27.0 |
| 15 | |
| 12 | |

| Input | Output |
|-------|--------|
| / | Error: division by zero |
| 5 | |
| 0 | |

**Explanation:** Use if/elif to call the right function based on the operator.

---

**Exercise H2. Perfect Numbers**

Write `is_perfect(n)` that checks if n is a perfect number. Find all perfect numbers up to 1000.

- **Input:** None.
- **Output:** All perfect numbers up to 1000.

**Example:**
```
6
28
496
```

**Explanation:** A perfect number equals the sum of its proper divisors (all divisors except itself).

---

**Exercise H3. GCD and LCM**

Write `gcd(a, b)` using the Euclidean algorithm. Write `lcm(a, b)` using the formula: lcm = a * b // gcd(a, b). Read two numbers, print both GCD and LCM.

- **Input:** Two integers.
- **Output:** GCD and LCM.

**Example:**

| Input | Output |
|-------|--------|
| 12 | GCD: 4 |
| 8 | LCM: 24 |

**Explanation:** gcd(12, 8) = 4. lcm(12, 8) = 12 * 8 // 4 = 24.

---

**Exercise H4. Nth Prime**

Write `is_prime(n)` and `nth_prime(n)` that returns the nth prime number. Read N, print the Nth prime.

- **Input:** One integer N.
- **Output:** The Nth prime number.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 11 |
| 1 | 2 |

**Explanation:** Primes: 2, 3, 5, 7, 11, ... The 5th prime is 11.

---

**Exercise H5. Collatz Length**

Write `collatz_length(n)` that returns how many steps the Collatz sequence takes to reach 1. Read N, print the length.

- **Input:** One integer N (N ≥ 1).
- **Output:** The number of steps.

**Example:**

| Input | Output |
|-------|--------|
| 27 | 111 |
| 1 | 0 |

**Explanation:** Starting from 27, the Collatz sequence takes 111 steps to reach 1.

---

**Exercise H6. Digit Reverse**

Write `digit_reverse(n)` that reverses the digits of n. Read N numbers, print each reversed.

- **Input:** First line: N. Next N lines: positive integers.
- **Output:** Each number with digits reversed.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 321 |
| 123 | 54 |
| 45 | 9 |
| 9 | |

**Explanation:** 123 → 321, 45 → 54, 9 → 9.

---

**Exercise H7. Palindrome Numbers**

Write `is_palindrome(n)` that checks if n reads the same forwards and backwards. Read N, print all palindromes from 1 to N.

- **Input:** One integer N.
- **Output:** All palindrome numbers from 1 to N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 25 | 1 |
| | 2 |
| | 3 |
| | 4 |
| | 5 |
| | 6 |
| | 7 |
| | 8 |
| | 9 |
| | 11 |
| | 22 |

**Explanation:** Single-digit numbers are all palindromes. 11 and 22 are also palindromes up to 25.
