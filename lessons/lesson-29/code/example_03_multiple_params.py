# example_03_multiple_params.py
# Lesson 29: Functions with multiple parameters

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

# Test all four operations
print("10 + 3 =", add(10, 3))
print("10 - 3 =", subtract(10, 3))
print("10 * 3 =", multiply(10, 3))
print("10 / 3 =", round(divide(10, 3), 2))
print("10 / 0 =", divide(10, 0))

print()

# Function with 3 parameters
def describe_person(name, age, city):
    print(name, "is", age, "years old and lives in", city)

describe_person("Alice", 10, "Hanoi")
describe_person("Bob", 12, "Ho Chi Minh City")
describe_person("Charlie", 9, "Da Nang")

print()

# Rectangle functions
def area_rectangle(width, height):
    return width * height

def perimeter_rectangle(width, height):
    return 2 * (width + height)

w = 6
h = 4
print("Rectangle", w, "x", h)
print("Area:", area_rectangle(w, h))
print("Perimeter:", perimeter_rectangle(w, h))
