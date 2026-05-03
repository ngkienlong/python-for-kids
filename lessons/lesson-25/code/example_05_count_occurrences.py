# example_05_count_occurrences.py
# Lesson 25: Count how many times each value appears in a list

# Count occurrences of a specific value
grades = ["A", "B", "A", "C", "A", "B", "A", "C", "B", "A"]
print("Grades:", grades)

count_a = 0
count_b = 0
count_c = 0

for grade in grades:
    if grade == "A":
        count_a += 1
    elif grade == "B":
        count_b += 1
    elif grade == "C":
        count_c += 1

print("A:", count_a, "times")
print("B:", count_b, "times")
print("C:", count_c, "times")

print()

# Count numbers in different ranges
scores = [45, 72, 88, 55, 91, 63, 78, 82, 49, 95]
print("Scores:", scores)

excellent = 0   # 90-100
good = 0        # 70-89
average = 0     # 50-69
poor = 0        # below 50

for score in scores:
    if score >= 90:
        excellent += 1
    elif score >= 70:
        good += 1
    elif score >= 50:
        average += 1
    else:
        poor += 1

print("Excellent (90-100):", excellent)
print("Good (70-89):", good)
print("Average (50-69):", average)
print("Poor (below 50):", poor)

print()

# Sum and average using a loop
numbers = [10, 25, 30, 15, 20]
print("Numbers:", numbers)

total = 0
for num in numbers:
    total += num

avg = total / len(numbers)
print("Sum:", total)
print("Average:", avg)
