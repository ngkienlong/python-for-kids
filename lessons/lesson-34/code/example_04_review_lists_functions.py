# example_04_review_lists_functions.py
# Lesson 34: Review — lists and functions working together

# --- Functions that work with lists ---

def list_stats(numbers):
    """Return a dictionary of statistics for a list of numbers."""
    if len(numbers) == 0:
        return None
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "range": max(numbers) - min(numbers),
    }

def filter_above(numbers, threshold):
    """Return a new list with only numbers above the threshold."""
    result = []
    for num in numbers:
        if num > threshold:
            result.append(num)
    return result

def normalize(numbers):
    """Return a normalized list (each value divided by the max)."""
    if len(numbers) == 0 or max(numbers) == 0:
        return numbers
    maximum = max(numbers)
    return [round(x / maximum, 2) for x in numbers]

def is_sorted(numbers):
    """Return True if the list is sorted in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# --- Test all functions ---
scores = [72, 95, 88, 61, 79, 84, 91, 55, 87]
print("Scores:", scores)
print()

# Statistics
stats = list_stats(scores)
print("=== Statistics ===")
for key, value in stats.items():
    print(key + ":", round(value, 2) if isinstance(value, float) else value)

print()

# Filter
average = stats["average"]
above_avg = filter_above(scores, average)
print("Above average (", round(average, 1), "):", above_avg)

print()

# Normalize
normalized = normalize(scores)
print("Normalized:", normalized)

print()

# Sort and check
scores_copy = scores[:]
scores_copy.sort()
print("Sorted:", scores_copy)
print("Is sorted?", is_sorted(scores_copy))
print("Original is sorted?", is_sorted(scores))
