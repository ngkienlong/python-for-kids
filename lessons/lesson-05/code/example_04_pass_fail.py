# example_04_pass_fail.py
# Lesson 5: Pass or fail based on a score

score = int(input("Enter your score (0-100): "))

# Check if the student passed
if score >= 60:
    print("Congratulations! You passed.")
    print("Your score:", score)
else:
    print("You did not pass this time.")
    print("Your score:", score)
    print("Keep practicing!")

# Multiple lines can be inside one if/else block.
# All lines with the same indentation belong to the same block.
