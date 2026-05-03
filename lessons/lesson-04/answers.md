# Lesson 4 — Answers

> ⚠️ Try to solve the exercises yourself first! Only check answers when you are stuck.

---

## 🟢 Easy

### E1. Say My Name

```python
name = input("Enter your name: ")
print("Hello,", str(name) + "!")
```

### E2. Double a Number

```python
n = int(input("Enter a number: "))
print(n * 2)
```

### E3. Sum of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
```

### E4. Name and Age

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, "is", age, "years old.")
```

### E5. Square Area

```python
side = int(input("Enter side length: "))
print(side * side)
```

### E6. Multiply Three Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(a * b * c)
```

### E7. Greeting with City

```python
name = input("Enter your name: ")
city = input("Enter your city: ")
print("Hi " + name + ", welcome from " + city + "!")
```

---

## 🟡 Medium

### M1. Average of Three

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print((a + b + c) / 3)
```

### M2. Rectangle

```python
width = int(input("Enter width: "))
height = int(input("Enter height: "))
print(width * height)
print(2 * width + 2 * height)
```

### M3. Celsius to Fahrenheit

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)
```

### M4. Seconds to Minutes

```python
total_seconds = int(input("Enter total seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(minutes)
print(seconds)
```

### M5. Circle

```python
pi = 3.14159
radius = float(input("Enter radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print(area)
print(circumference)
```

### M6. Tip Calculator

```python
bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
tip = bill * tip_percent / 100
total = bill + tip
print(tip)
print(total)
```

### M7. Power

```python
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(base ** exponent)
```

---

## 🔴 Hard

### H1. Age Calculator

```python
# Age Calculator
# Current year is 2025. Read birth year, print age.

birth_year = int(input("Enter birth year: "))
current_year = 2025
age = current_year - birth_year
print(age)
```

**How it works:** Subtract the birth year from 2025 to get the age.

### H2. Rectangle Dimensions

```python
# Rectangle Dimensions
# Read width and height, print area and perimeter.

width = int(input("Enter width: "))
height = int(input("Enter height: "))

area = width * height
perimeter = 2 * (width + height)

print(area)
print(perimeter)
```

**How it works:** Area = W × H. Perimeter = 2 × (W + H).

### H3. Seconds Converter

```python
# Seconds Converter
# Read total seconds, print hours, minutes, seconds.

total = int(input("Enter total seconds: "))

hours = total // 3600
remaining = total % 3600
minutes = remaining // 60
seconds = remaining % 60

print(hours)
print(minutes)
print(seconds)
```

**How it works:** Divide by 3600 to get hours. Take the remainder, divide by 60 to get minutes. The final remainder is seconds.

### H4. Coin Change

```python
# Coin Change
# Give change using fewest coins: 500, 200, 100 dong.

amount = int(input("Enter amount: "))

coins_500 = amount // 500
amount = amount % 500

coins_200 = amount // 200
amount = amount % 200

coins_100 = amount // 100

print(coins_500)
print(coins_200)
print(coins_100)
```

**How it works:** Greedy approach — always use the largest coin first. Use `//` to count coins and `%` to find the remainder.

### H5. BMI Calculator

```python
# BMI Calculator
# BMI = weight / (height * height)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)
print(round(bmi, 2))
```

**How it works:** Apply the BMI formula. `round(bmi, 2)` rounds to 2 decimal places.

### H6. Speed, Distance, Time

```python
# Speed, Distance, Time
# Time = Distance / Speed

distance = float(input("Enter distance in km: "))
speed = float(input("Enter speed in km/h: "))

time = distance / speed
print(time)
```

**How it works:** Rearrange the formula Distance = Speed × Time to get Time = Distance ÷ Speed.

### H7. Temperature Converter

```python
# Temperature Converter
# Convert Celsius to Fahrenheit and Kelvin.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(fahrenheit)
print(kelvin)
```

**How it works:** Apply both formulas. Fahrenheit = C × 9/5 + 32. Kelvin = C + 273.15.

---
