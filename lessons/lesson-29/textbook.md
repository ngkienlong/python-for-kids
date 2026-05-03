# Lesson 29: Parameters and Return 📤

> **Goal:** Write functions that accept parameters and return values.

---

## 1. Parameters — Give Information to a Function

A **parameter** is a variable that receives a value when the function is called.

> 💡 **Scratch connection:** In Scratch, "My Blocks" can have inputs. In Python, those inputs are called **parameters**.

```python
def greet(name):        # 'name' is a parameter
    print("Hello,", name)

greet("Alice")          # "Alice" is the argument
greet("Bob")            # "Bob" is the argument
```

**Output:**
```
Hello, Alice
Hello, Bob
```

---

## 2. Multiple Parameters

A function can have more than one parameter:

```python
def add(a, b):
    print(a + b)

add(3, 5)    # prints 8
add(10, 20)  # prints 30
```

---

## 3. Return — Send a Value Back

`return` sends a value back to the caller:

```python
def add(a, b):
    return a + b       # send the result back

result = add(3, 5)     # result = 8
print(result)          # 8
```

Without `return`, a function gives back `None`:

```python
def greet(name):
    print("Hello,", name)

x = greet("Alice")   # prints "Hello, Alice"
print(x)             # None  (no return value)
```

---

## 4. Use the Return Value

```python
def square(n):
    return n * n

print(square(4))        # 16
print(square(7))        # 49

# Store and use the result
area = square(5)
print("Area:", area)    # Area: 25
```

---

## 5. Default Parameter Values

You can give a parameter a default value:

```python
def greet(name="friend"):
    print("Hello,", name)

greet("Alice")    # Hello, Alice
greet()           # Hello, friend  (uses default)
```

---

## 6. Functions That Calculate

```python
def area_rectangle(width, height):
    return width * height

def perimeter_rectangle(width, height):
    return 2 * (width + height)

w = 5
h = 3
print("Area:", area_rectangle(w, h))           # 15
print("Perimeter:", perimeter_rectangle(w, h)) # 16
```

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| parameter | tham số | A variable in the function definition |
| argument | đối số | The actual value passed when calling |
| return | trả về | Send a value back from the function |
| value | giá trị | A piece of data (number, string, etc.) |
| caller | nơi gọi | The code that calls the function |
| default | mặc định | A value used when no argument is given |
| multiple | nhiều | More than one |
| pass | truyền | Give a value to a function |
| receive | nhận | Get a value in a parameter |
| output | đầu ra | What the function produces |
| None | rỗng | The value returned when there is no return |
| signature | chữ ký hàm | The function name and its parameters |

---

## 8. Summary

✅ `def greet(name):` — `name` is a parameter.
✅ `greet("Alice")` — "Alice" is the argument.
✅ `return value` sends a value back to the caller.
✅ `result = add(3, 5)` stores the returned value.
✅ Functions without `return` give back `None`.
✅ Default parameters: `def greet(name="friend"):`.

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Greet by Name**

Write a function `greet(name)` that prints "Hello, [name]!". Call it with 3 different names.

- **Input:** None (hardcode the names).
- **Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

---

**Exercise E2. Square**

Write a function `square(n)` that returns n². Print the squares of 3, 5, and 7.

- **Input:** None.
- **Output:**
```
9
25
49
```

---

**Exercise E3. Add Two Numbers**

Write a function `add(a, b)` that returns a + b. Read two numbers and print their sum.

- **Input:** Two integers.
- **Output:** Their sum.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 8 |
| 5 | |

---

**Exercise E4. Is Even**

Write a function `is_even(n)` that returns `True` if n is even, `False` otherwise. Test it with 4, 7, and 10.

- **Input:** None.
- **Output:**
```
True
False
True
```

---

**Exercise E5. Area of Rectangle**

Write a function `area(width, height)` that returns width × height. Read width and height, print the area.

- **Input:** Two integers: width and height.
- **Output:** The area.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 15 |
| 3 | |

---

**Exercise E6. Default Greeting**

Write a function `greet(name="friend")` with a default parameter. Call it once with a name and once without.

- **Input:** None.
- **Output:**
```
Hello, Alice!
Hello, friend!
```

---

**Exercise E7. Absolute Value**

Write a function `my_abs(n)` that returns the absolute value of n (without using `abs()`). Test with -5, 3, and -8.

- **Input:** None.
- **Output:**
```
5
3
8
```

---

### 🟡 Medium

---

**Exercise M1. Max of Two**

Write a function `max_two(a, b)` that returns the larger of two numbers. Read two numbers and print the larger one.

- **Input:** Two integers.
- **Output:** The larger number.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 12 |
| 12 | |

---

**Exercise M2. Temperature Converter**

Write `celsius_to_fahrenheit(c)` that returns c × 9/5 + 32. Read a temperature in Celsius, print it in Fahrenheit.

- **Input:** One number (Celsius).
- **Output:** The temperature in Fahrenheit.

**Example:**

| Input | Output |
|-------|--------|
| 100 | 212.0 |
| 0 | 32.0 |

---

**Exercise M3. Power Function**

Write a function `power(base, exp)` that returns base^exp (without using `**`). Use a loop. Read base and exp, print the result.

- **Input:** Two integers: base and exp (exp ≥ 0).
- **Output:** base raised to the power of exp.

**Example:**

| Input | Output |
|-------|--------|
| 2 | 8 |
| 3 | |

---

**Exercise M4. Classify Number**

Write a function `classify(n)` that returns "positive", "negative", or "zero". Read N numbers and print the classification of each.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Classification of each number.

**Example:**

| Input | Output |
|-------|--------|
| 4 | positive |
| 5 | negative |
| -3 | zero |
| 0 | positive |
| 7 | |

---

**Exercise M5. Perimeter and Area**

Write `area_circle(r)` that returns π × r² (use 3.14159 for π) and `perimeter_circle(r)` that returns 2 × π × r. Read r, print both.

- **Input:** One number (radius).
- **Output:** Area and perimeter (2 decimal places).

**Example:**

| Input | Output |
|-------|--------|
| 5 | Area: 78.54 |
| | Perimeter: 31.42 |

---

**Exercise M6. Repeat String**

Write a function `repeat(text, times)` that returns the text repeated `times` times. Read text and times, print the result.

- **Input:** One string, then one integer.
- **Output:** The repeated string.

**Example:**

| Input | Output |
|-------|--------|
| ha | hahaha |
| 3 | |

---

**Exercise M7. Grade Function**

Write a function `get_grade(score)` that returns "A" (≥90), "B" (≥80), "C" (≥70), "D" (≥60), or "F" (<60). Read N scores and print each grade.

- **Input:** First line: N. Next N lines: scores.
- **Output:** Grade for each score.

**Example:**

| Input | Output |
|-------|--------|
| 3 | A |
| 95 | C |
| 72 | F |
| 55 | |

---

### 🔴 Hard

---

**Exercise H1. Add Function**

Write `add(a, b)` that returns a + b. Read two numbers, print the result.

- **Input:** Two integers.
- **Output:** Their sum.

**Example:**

| Input | Output |
|-------|--------|
| 15 | 27 |
| 12 | |

**Explanation:** Simple function with two parameters and a return value.

---

**Exercise H2. Is Even — Filter List**

Write `is_even(n)` that returns `True` if n is even. Read N numbers. Print only the even ones.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Even numbers, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 4 |
| 3 | 8 |
| 4 | 6 |
| 7 | |
| 8 | |
| 6 | |
| 1 | |

**Explanation:** Call `is_even(num)` for each number in the list.

---

**Exercise H3. Temperature Converter**

Write `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`. Read a temperature and a direction ("C" or "F"). Convert and print.

- **Input:** First line: temperature (number). Second line: direction ("C" to convert to F, "F" to convert to C).
- **Output:** The converted temperature (2 decimal places).

**Example:**

| Input | Output |
|-------|--------|
| 100 | 212.0 |
| C | |

| Input | Output |
|-------|--------|
| 32 | 0.0 |
| F | |

**Explanation:** If direction is "C", call `celsius_to_fahrenheit`. If "F", call `fahrenheit_to_celsius`.

---

**Exercise H4. Max of Three**

Write `max_of_three(a, b, c)` that returns the largest of three numbers. Read 3 numbers, print the max.

- **Input:** Three integers (one per line).
- **Output:** The largest.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 15 |
| 15 | |
| 3 | |

**Explanation:** Compare a, b, c inside the function and return the largest.

---

**Exercise H5. Is Prime**

Write `is_prime(n)` that returns `True` if n is prime. Read N, print all prime numbers from 2 to N.

- **Input:** One integer N.
- **Output:** All primes from 2 to N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 20 | 2 |
| | 3 |
| | 5 |
| | 7 |
| | 11 |
| | 13 |
| | 17 |
| | 19 |

**Explanation:** A number is prime if it has no divisors other than 1 and itself. Check divisors from 2 to n-1.

---

**Exercise H6. Digit Sum**

Write `digit_sum(n)` that returns the sum of digits of n. Read N numbers, print their digit sums.

- **Input:** First line: N. Next N lines: positive integers.
- **Output:** Digit sum of each number.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 6 |
| 123 | 10 |
| 46 | 9 |
| 9 | |

**Explanation:** 1+2+3=6, 4+6=10, 9=9.

---

**Exercise H7. Fibonacci Function**

Write `fibonacci(n)` that returns the nth Fibonacci number (fib(0)=0, fib(1)=1). Read N, print fib(0) through fib(N).

- **Input:** One integer N.
- **Output:** Fibonacci numbers from fib(0) to fib(N), one per line.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 0 |
| | 1 |
| | 1 |
| | 2 |
| | 3 |
| | 5 |
| | 8 |
| | 13 |

**Explanation:** Use a loop inside `fibonacci(n)` to calculate the nth Fibonacci number. Call it for each i from 0 to N.
