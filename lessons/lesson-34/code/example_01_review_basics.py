# example_01_review_basics.py
# Lesson 34: Review — variables, input, math in one program

# --- Variables ---
course_name = "Python for Kids"
lesson_number = 34
pi = 3.14159

print("Course:", course_name)
print("Lesson:", lesson_number)
print("Pi:", pi)

print()

# --- Input and type conversion ---
name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you (cm)? "))

print()
print("=== Your Profile ===")
print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")

# --- Math ---
height_m = height / 100
print("Height in meters:", round(height_m, 2))

# Age in months
age_months = age * 12
print("Age in months:", age_months)

# Days lived (approximate)
age_days = age * 365
print("Approximate days lived:", age_days)

print()
print("Congratulations,", name + "! You've completed", course_name + "!")
