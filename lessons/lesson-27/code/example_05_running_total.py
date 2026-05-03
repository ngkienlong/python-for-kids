# example_05_running_total.py
# Lesson 27: Running total (cumulative sum)
# Shows the sum so far after each item is added

# Daily savings
savings = [10, 25, 5, 30, 15, 20, 50]
print("Daily savings:", savings)
print()

print("Day | Saved | Total so far")
print("-" * 30)

running_total = 0
for i in range(len(savings)):
    running_total += savings[i]
    print("Day", i + 1, "|", savings[i], "|", running_total)

print()
print("Total savings:", running_total)

print()

# Build a list of cumulative sums
numbers = [3, 7, 2, 8, 5]
print("Numbers:", numbers)

cumulative = []
total = 0
for num in numbers:
    total += num
    cumulative.append(total)

print("Cumulative sums:", cumulative)

print()

# Count how many times the value increases
print("Checking increases:")
increases = 0
for i in range(len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        increases += 1
        print(numbers[i], "->", numbers[i + 1], "(increase)")
    else:
        print(numbers[i], "->", numbers[i + 1], "(no increase)")

print("Total increases:", increases)
