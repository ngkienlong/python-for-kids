# example_05_functions_calling_functions.py
# Lesson 31: Functions that call other functions
# This shows how to build complex programs from simple pieces

# --- BMI Calculator ---

def bmi(weight, height):
    """Calculate Body Mass Index."""
    return weight / (height * height)

def bmi_category(bmi_value):
    """Return the BMI category string."""
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25.0:
        return "Normal weight"
    elif bmi_value < 30.0:
        return "Overweight"
    else:
        return "Obese"

def print_bmi_report(name, weight, height):
    """Print a complete BMI report — calls bmi() and bmi_category()."""
    b = bmi(weight, height)           # call bmi()
    category = bmi_category(b)        # call bmi_category()
    print("Name:", name)
    print("Weight:", weight, "kg")
    print("Height:", height, "m")
    print("BMI:", round(b, 2))
    print("Category:", category)
    print()

# Test with different people
print_bmi_report("Alice", 55, 1.65)
print_bmi_report("Bob", 90, 1.75)
print_bmi_report("Charlie", 45, 1.70)

# --- GCD and LCM ---

def gcd(a, b):
    """Find the Greatest Common Divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Find the Least Common Multiple — calls gcd()."""
    return a * b // gcd(a, b)   # uses gcd() inside!

print("=== GCD and LCM ===")
pairs = [(12, 8), (15, 25), (7, 13), (100, 75)]
for a, b in pairs:
    print("gcd(" + str(a) + ", " + str(b) + ") =", gcd(a, b),
          "  lcm =", lcm(a, b))
