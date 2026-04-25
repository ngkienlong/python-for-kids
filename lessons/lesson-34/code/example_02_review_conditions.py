# example_02_review_conditions.py
# Lesson 34: Review — if/elif/else with input

# --- Grade calculator ---
print("=== Grade Calculator ===")
score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score!")
elif score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Great job!"
elif score >= 70:
    grade = "C"
    message = "Good work!"
elif score >= 60:
    grade = "D"
    message = "Keep trying!"
else:
    grade = "F"
    message = "Please study more."

print("Score:", score)
print("Grade:", grade)
print(message)

print()

# --- Temperature classifier ---
print("=== Temperature Classifier ===")
temp = float(input("Enter temperature (°C): "))

if temp >= 35:
    category = "Very Hot"
    advice = "Stay hydrated!"
elif temp >= 25:
    category = "Hot"
    advice = "Wear light clothes."
elif temp >= 15:
    category = "Warm"
    advice = "Nice weather!"
elif temp >= 5:
    category = "Cool"
    advice = "Bring a jacket."
else:
    category = "Cold"
    advice = "Wear a coat!"

print("Temperature:", temp, "°C")
print("Category:", category)
print("Advice:", advice)

print()

# --- Number classifier ---
print("=== Number Classifier ===")
n = int(input("Enter a number: "))

if n > 0:
    print(n, "is positive")
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
    if n > 100:
        print(n, "is large")
elif n < 0:
    print(n, "is negative")
else:
    print("The number is zero")
