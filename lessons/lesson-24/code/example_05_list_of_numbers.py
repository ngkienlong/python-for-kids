# example_05_list_of_numbers.py
# Lesson 24: Working with a list of numbers

# A list of test scores
scores = [85, 92, 78, 95, 88, 76, 91]

print("All scores:", scores)
print("Number of scores:", len(scores))
print("First score:", scores[0])
print("Last score:", scores[-1])

print()

# Find the highest and lowest using built-in functions
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total of all scores:", sum(scores))

print()

# Add a new score
scores.append(83)
print("After adding new score:", scores)
print("Now there are", len(scores), "scores.")

print()

# Change a score (student retook the test)
print("Before correction:", scores)
scores[2] = 85   # student at index 2 improved from 78 to 85
print("After correction:", scores)

print()

# Print each score with its position
print("Score report:")
print("Position 1:", scores[0])
print("Position 2:", scores[1])
print("Position 3:", scores[2])
print("Position 4:", scores[3])
print("Position 5:", scores[4])
