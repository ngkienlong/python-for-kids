# example_01_sum_average.py
# Lesson 27: Calculate sum and average of a list

scores = [85, 92, 78, 95, 88, 76, 91]
print("Scores:", scores)

# Method 1: use built-in sum()
total = sum(scores)
print("Sum:", total)

# Calculate average
average = total / len(scores)
print("Average:", round(average, 2))

print()

# Method 2: calculate sum manually with a loop
manual_total = 0
for score in scores:
    manual_total += score
print("Manual sum:", manual_total)

print()

# Statistics summary
print("=== Statistics ===")
print("Count:", len(scores))
print("Sum:", sum(scores))
print("Average:", round(sum(scores) / len(scores), 2))
print("Min:", min(scores))
print("Max:", max(scores))
print("Range:", max(scores) - min(scores))
