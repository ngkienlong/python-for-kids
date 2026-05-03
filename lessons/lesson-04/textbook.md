# Lesson 4: Input — Talking to the Computer ⌨️

> **Goal:** Use `input()` to read data from the user, convert types, and build a simple calculator.

---

## 1. What is Input?

So far, all your programs had fixed values — you typed the numbers directly in the code. But real programs ask the **user** for information!

In Scratch, you used the **"ask and wait"** block to get input from the user. In Python, we use the `input()` function.

| Scratch | Python |
|---------|--------|
| "ask and wait" block | `input()` |
| "answer" variable | the value returned by `input()` |

---

## 2. Basic `input()`

```python
name = input("What is your name? ")
print("Hello,", name)
```

**How it works:**
1. Python shows the message `What is your name? ` on the screen.
2. The program **pauses** and waits for you to type something.
3. When you press **Enter**, Python stores what you typed in the variable `name`.
4. `print()` shows the greeting.

**Example run:**
```
What is your name? An
Hello, An
```

The text inside `input("...")` is called a **prompt** — it tells the user what to type.

---

## 3. `input()` Always Returns a String

This is very important! No matter what the user types, `input()` always gives you a **string** (text).

```python
x = input("Enter a number: ")
print(x)
print(type(x))
```

**Example run:**
```
Enter a number: 42
42
<class 'str'>
```

Even though the user typed `42`, Python stores it as the string `"42"`, not the number `42`. If you try to do math with it, you get an error!

```python
x = input("Enter a number: ")
print(x + 10)   # ❌ Error! Can't add string and number
```

---

## 4. Type Conversion — Changing the Type

To use the input as a number, you must **convert** it. This is called **type conversion** (or **casting**).

| Function | Converts to | Example |
|----------|------------|---------|
| `int()` | Integer (whole number) | `int("42")` → `42` |
| `float()` | Float (decimal number) | `float("3.14")` → `3.14` |
| `str()` | String (text) | `str(42)` → `"42"` |

### Reading an integer:

```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

**Example run:**
```
Enter your age: 10
Next year you will be 11
```

### Reading a float:

```python
height = float(input("Enter your height in meters: "))
print("Your height:", height)
```

**Example run:**
```
Enter your height in meters: 1.35
Your height: 1.35
```

---

## 5. How Type Conversion Works

Think of it like a machine that transforms one thing into another:

```
"42"  →  int()  →  42
"3.14"  →  float()  →  3.14
42  →  str()  →  "42"
```

You can also convert between numbers:

```python
x = int(3.9)    # x = 3  (cuts off the decimal, does NOT round)
y = float(5)    # y = 5.0
```

> ⚠️ `int()` does NOT round — it just removes the decimal part. `int(3.9)` gives `3`, not `4`.

---

## 6. Reading Multiple Inputs

You can call `input()` multiple times to read several values:

```python
first_name = input("First name: ")
last_name = input("Last name: ")
print("Full name:", first_name, last_name)
```

**Example run:**
```
First name: Nguyen
Last name: An
Full name: Nguyen An
```

---

## 7. Build a Calculator

Now let's put it all together and build a simple calculator!

```python
# Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
```

**Example run:**
```
Enter first number: 10
Enter second number: 4
Sum: 14.0
Difference: 6.0
Product: 40.0
Quotient: 2.5
```

---

## 8. Common Mistakes

```python
# Mistake 1: Forgetting to convert
age = input("Age: ")
print(age + 1)          # ❌ TypeError: can only concatenate str to str

# Fix:
age = int(input("Age: "))
print(age + 1)          # ✅

# Mistake 2: Using int() for a decimal
height = int(input("Height: "))   # ❌ If user types 1.75, this crashes!

# Fix:
height = float(input("Height: "))  # ✅

# Mistake 3: Forgetting the prompt message
x = input()             # ✅ Works, but user doesn't know what to type
x = input("Enter x: ")  # ✅ Better — tells the user what to do
```

---

## 9. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| input | đầu vào | Data given to the program by the user |
| output | đầu ra | Data shown by the program |
| prompt | lời nhắc | The message shown before waiting for input |
| type conversion | chuyển đổi kiểu | Changing data from one type to another |
| integer | số nguyên | A whole number (no decimal point) |
| float | số thực | A number with a decimal point |
| string | chuỗi | Text data, written in quotes |
| cast | ép kiểu | Another word for type conversion |
| user | người dùng | The person running the program |
| standard input | đầu vào chuẩn | The keyboard input stream |
| return | trả về | What a function gives back |
| convert | chuyển đổi | Change from one form to another |

---

## 10. Summary

✅ `input()` pauses the program and waits for the user to type something.
✅ `input()` **always returns a string** — even if the user types a number.
✅ Use `int(input())` to read a whole number.
✅ Use `float(input())` to read a decimal number.
✅ The text inside `input("...")` is the prompt — it tells the user what to type.
✅ `int()`, `float()`, `str()` convert between types.

---

## 11. Homework

### 🟢 Easy

---

**Exercise E1. Say My Name**

Ask the user for their name and print a greeting.

- **Input:** One line — the user's name.
- **Output:** One line — a greeting with the name.

**Example:**

| Input | Output |
|-------|--------|
| An | Hello, An! |
| Minh | Hello, Minh! |

---

**Exercise E2. Double a Number**

Ask the user for a whole number. Print the number doubled.

- **Input:** One integer.
- **Output:** The number multiplied by 2.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 10 |
| 13 | 26 |

---

**Exercise E3. Sum of Two Numbers**

Ask the user for two whole numbers (one per line). Print their sum.

- **Input:** Two integers, one per line.
- **Output:** Their sum.

**Example:**

| Input | Output |
|-------|--------|
| 3 / 7 | 10 |
| 100 / 200 | 300 |

---

**Exercise E4. Name and Age**

Ask the user for their name and age. Print a sentence combining both.

- **Input:** Two lines — name, then age.
- **Output:** One sentence.

**Example:**

| Input | Output |
|-------|--------|
| An / 10 | An is 10 years old. |
| Minh / 8 | Minh is 8 years old. |

---

**Exercise E5. Square Area**

Ask the user for the side length of a square. Print the area.

- **Input:** One integer — the side length.
- **Output:** The area (side × side).

**Example:**

| Input | Output |
|-------|--------|
| 5 | 25 |
| 12 | 144 |

---

**Exercise E6. Multiply Three Numbers**

Ask the user for three whole numbers (one per line). Print their product.

- **Input:** Three integers, one per line.
- **Output:** Their product.

**Example:**

| Input | Output |
|-------|--------|
| 2 / 3 / 4 | 24 |
| 5 / 5 / 5 | 125 |

---

**Exercise E7. Greeting with City**

Ask the user for their name and their city. Print a sentence like: `Hi An, welcome from Ho Chi Minh City!`

- **Input:** Two lines — name, then city.
- **Output:** One greeting sentence.

**Example:**

| Input | Output |
|-------|--------|
| An / Ho Chi Minh City | Hi An, welcome from Ho Chi Minh City! |
| Minh / Hanoi | Hi Minh, welcome from Hanoi! |

---

### 🟡 Medium

---

**Exercise M1. Average of Three**

Ask the user for three decimal numbers. Print their average.

- **Input:** Three floats, one per line.
- **Output:** Their average.

**Example:**

| Input | Output |
|-------|--------|
| 7.0 / 8.0 / 9.0 | 8.0 |
| 5.5 / 6.5 / 7.0 | 6.333333333333333 |

---

**Exercise M2. Rectangle**

Ask the user for the width and height of a rectangle. Print the area and perimeter.

- **Input:** Two integers — width, then height.
- **Output:** Two lines: area, then perimeter.

**Example:**

| Input | Output |
|-------|--------|
| 6 / 4 | 24 |
| | 20 |
| 10 / 3 | 30 |
| | 26 |

---

**Exercise M3. Celsius to Fahrenheit**

Ask the user for a temperature in Celsius. Print the temperature in Fahrenheit. Formula: `F = C * 9 / 5 + 32`.

- **Input:** One float — temperature in Celsius.
- **Output:** Temperature in Fahrenheit.

**Example:**

| Input | Output |
|-------|--------|
| 0 | 32.0 |
| 100 | 212.0 |
| 37 | 98.6 |

---

**Exercise M4. Seconds to Minutes**

Ask the user for a number of seconds. Print how many full minutes and remaining seconds.

- **Input:** One integer — total seconds.
- **Output:** Two lines: full minutes, then remaining seconds.

**Example:**

| Input | Output |
|-------|--------|
| 90 | 1 |
| | 30 |
| 125 | 2 |
| | 5 |

---

**Exercise M5. Circle**

Ask the user for the radius of a circle. Print the area and circumference. Use `pi = 3.14159`.

- **Input:** One float — the radius.
- **Output:** Two lines: area, then circumference.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 78.53975 |
| | 31.4159 |

---

**Exercise M6. Tip Calculator**

Ask the user for a bill amount and a tip percentage. Print the tip amount and the total bill.

- **Input:** Two floats — bill amount, then tip percentage.
- **Output:** Two lines: tip amount, then total.

**Example:**

| Input | Output |
|-------|--------|
| 100000 / 10 | 10000.0 |
| | 110000.0 |
| 200000 / 15 | 30000.0 |
| | 230000.0 |

---

**Exercise M7. Power**

Ask the user for a base number and an exponent. Print the result of base raised to the exponent. Use the `**` operator.

- **Input:** Two integers — base, then exponent.
- **Output:** The result.

**Example:**

| Input | Output |
|-------|--------|
| 2 / 10 | 1024 |
| 3 / 4 | 81 |

---

### 🔴 Hard

---

**Exercise H1. Age Calculator**

Hoa is filling out a form and needs to know her age. She knows the year she was born, but not her current age. The current year is **2025**.

Write a program that reads the birth year and prints the person's age.

- **Input:** One integer — the birth year (1900 ≤ year ≤ 2025).
- **Output:** One integer — the age in 2025.

**Example:**

| Input | Output |
|-------|--------|
| 2015 | 10 |
| 2000 | 25 |
| 1990 | 35 |

**Explanation:** Age = 2025 − birth year. If someone was born in 2015, they are 2025 − 2015 = 10 years old.

---

**Exercise H2. Rectangle Dimensions**

A builder needs to quickly calculate the area and perimeter of a rectangular room. Help him by writing a program that reads the width and height, then prints both values.

- **Input:** Two integers on separate lines — width W, then height H (1 ≤ W, H ≤ 1000).
- **Output:** Two lines: area on line 1, perimeter on line 2.

**Example:**

| Input | Output |
|-------|--------|
| 8 / 5 | 40 |
| | 26 |
| 12 / 7 | 84 |
| | 38 |

**Explanation:** Area = W × H. Perimeter = 2 × (W + H).

---

**Exercise H3. Seconds Converter**

An astronaut on a space station needs to convert mission time from total seconds into hours, minutes, and seconds for the mission log.

Write a program that reads a total number of seconds and prints the equivalent hours, minutes, and seconds.

- **Input:** One integer — total seconds (0 ≤ seconds ≤ 86400).
- **Output:** Three lines: hours, then minutes, then seconds.

**Example:**

| Input | Output |
|-------|--------|
| 3661 | 1 |
| | 1 |
| | 1 |
| 7200 | 2 |
| | 0 |
| | 0 |
| 90 | 0 |
| | 1 |
| | 30 |

**Explanation:** 3661 seconds = 1 hour (3600s) + 1 minute (60s) + 1 second. Use `//` and `%`.

---

**Exercise H4. Coin Change**

A vending machine only has coins of 500 dong, 200 dong, and 100 dong. When a customer pays too much, the machine gives change using the **fewest coins possible** — starting with the largest coins first.

Write a program that reads an amount (a multiple of 100) and prints how many of each coin to give.

- **Input:** One integer — the amount in dong (100 ≤ amount ≤ 10000, always a multiple of 100).
- **Output:** Three lines: number of 500-dong coins, number of 200-dong coins, number of 100-dong coins.

**Example:**

| Input | Output |
|-------|--------|
| 1300 | 2 |
| | 1 |
| | 1 |
| 800 | 1 |
| | 1 |
| | 1 |

**Explanation:** For 1300 dong: 2 × 500 = 1000, remainder 300. 1 × 200 = 200, remainder 100. 1 × 100 = 100. Done.

---

**Exercise H5. BMI Calculator**

A school nurse wants a quick tool to calculate students' Body Mass Index (BMI). BMI = weight (kg) ÷ (height (m) × height (m)).

Write a program that reads weight and height, then prints the BMI rounded to 2 decimal places.

- **Input:** Two lines — weight in kg (float), then height in meters (float).
- **Output:** One line — the BMI rounded to 2 decimal places.

**Example:**

| Input | Output |
|-------|--------|
| 30 / 1.35 | 16.46 |
| 50 / 1.60 | 19.53 |
| 70 / 1.75 | 22.86 |

**Explanation:** BMI = weight / (height * height). Use `round(bmi, 2)` to round to 2 decimal places.

---

**Exercise H6. Speed, Distance, Time**

A race car driver wants to know how long it will take to finish a race. He knows the total distance of the track and his average speed.

Write a program that reads the distance (km) and speed (km/h), then prints the time in hours.

- **Input:** Two lines — distance in km (float), then speed in km/h (float).
- **Output:** One line — the time in hours.

**Example:**

| Input | Output |
|-------|--------|
| 300 / 150 | 2.0 |
| 100 / 80 | 1.25 |
| 500 / 200 | 2.5 |

**Explanation:** Time = Distance ÷ Speed.

---

**Exercise H7. Temperature Converter**

A scientist needs to convert temperatures between different scales. She wants to convert from Celsius to both Fahrenheit and Kelvin at the same time.

Write a program that reads a temperature in Celsius and prints the equivalent in Fahrenheit and Kelvin.

- **Input:** One float — temperature in Celsius.
- **Output:** Two lines: Fahrenheit on line 1, Kelvin on line 2.

**Formulas:**
- Fahrenheit = Celsius × 9 / 5 + 32
- Kelvin = Celsius + 273.15

**Example:**

| Input | Output |
|-------|--------|
| 0 | 32.0 |
| | 273.15 |
| 100 | 212.0 |
| | 373.15 |
| -40 | -40.0 |
| | 233.15 |

---
