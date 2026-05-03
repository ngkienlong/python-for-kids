# example_02_filter_list.py
# Lesson 27: Filter a list — keep only items that meet a condition

numbers = [-5, 3, -1, 8, 0, -2, 7, 4, -9, 6]
print("All numbers:", numbers)

# Filter: keep only positive numbers
positives = []
for num in numbers:
    if num > 0:
        positives.append(num)
print("Positive only:", positives)

# Filter: keep only negative numbers
negatives = []
for num in numbers:
    if num < 0:
        negatives.append(num)
print("Negative only:", negatives)

# Filter: keep only even numbers
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print("Even only:", evens)

print()

# Same filters using list comprehension (shorter!)
positives2 = [x for x in numbers if x > 0]
negatives2 = [x for x in numbers if x < 0]
evens2 = [x for x in numbers if x % 2 == 0]

print("Positives (comprehension):", positives2)
print("Negatives (comprehension):", negatives2)
print("Evens (comprehension):", evens2)

print()

# Filter scores above average
scores = [72, 95, 88, 61, 79, 84, 91, 55, 87]
average = sum(scores) / len(scores)
print("Scores:", scores)
print("Average:", round(average, 2))

above_average = [s for s in scores if s > average]
print("Above average:", above_average)
