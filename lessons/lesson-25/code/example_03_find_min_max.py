# example_03_find_min_max.py
# Lesson 25: Find minimum and maximum values in a list

temperatures = [23, 17, 31, 28, 15, 25, 19]
print("Temperatures:", temperatures)

# --- Find the MAXIMUM ---
# Start by assuming the first item is the largest
maximum = temperatures[0]

for temp in temperatures:
    if temp > maximum:
        maximum = temp   # found a bigger number, update maximum

print("Highest temperature:", maximum)

# --- Find the MINIMUM ---
# Start by assuming the first item is the smallest
minimum = temperatures[0]

for temp in temperatures:
    if temp < minimum:
        minimum = temp   # found a smaller number, update minimum

print("Lowest temperature:", minimum)

print()

# Find both at the same time
scores = [85, 92, 78, 95, 88, 76, 91]
print("Scores:", scores)

best = scores[0]
worst = scores[0]

for score in scores:
    if score > best:
        best = score
    if score < worst:
        worst = score

print("Best score:", best)
print("Worst score:", worst)
print("Difference:", best - worst)

# Verify with built-in functions
print()
print("Verify with max():", max(scores))
print("Verify with min():", min(scores))
