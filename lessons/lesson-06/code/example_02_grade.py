# example_02_grade.py
# Lesson 6: Grade calculator with remarks
# Each branch can have multiple lines of code.

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
    remark = "Outstanding!"
elif score >= 80:
    grade = "B"
    remark = "Well done!"
elif score >= 70:
    grade = "C"
    remark = "Good effort."
elif score >= 60:
    grade = "D"
    remark = "Keep trying."
else:
    grade = "F"
    remark = "Please study more."

# Print the result after the if/elif/else block
print("Grade:", grade)
print(remark)
