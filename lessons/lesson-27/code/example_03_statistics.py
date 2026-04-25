# example_03_statistics.py
# Lesson 27: Basic statistics on a list

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print("Data:", data)
print()

# Count
n = len(data)
print("Count:", n)

# Sum
total = sum(data)
print("Sum:", total)

# Average (mean)
mean = total / n
print("Mean:", mean)

# Minimum and maximum
minimum = min(data)
maximum = max(data)
print("Min:", minimum)
print("Max:", maximum)

# Range
data_range = maximum - minimum
print("Range:", data_range)

print()

# Count how many are above and below average
above = 0
below = 0
equal = 0
for num in data:
    if num > mean:
        above += 1
    elif num < mean:
        below += 1
    else:
        equal += 1

print("Above mean:", above)
print("Below mean:", below)
print("Equal to mean:", equal)

print()

# Sum of squares (useful in statistics)
sum_sq = sum([x * x for x in data])
print("Sum of squares:", sum_sq)
