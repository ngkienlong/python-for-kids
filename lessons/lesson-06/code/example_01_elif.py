# example_01_elif.py
# Lesson 6: Introduction to elif
# elif = "else if" — check another condition when the previous one is False.

score = int(input("Enter your score (0-100): "))

# Python checks conditions from top to bottom.
# It stops at the FIRST True condition.
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    # This runs if NONE of the above conditions were True
    print("Grade: F")

# Only ONE branch runs, even if multiple conditions could be True.
# For score = 85: 85 >= 90 is False, 85 >= 80 is True → prints "B", stops.
