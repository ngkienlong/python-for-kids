# example_05_mini_project.py
# Lesson 34: Mini project — Grade Calculator with functions and lists
# This program reads student names and scores, then produces a full report.

# ============================================================
# FUNCTIONS
# ============================================================

def get_grade(score):
    """Return letter grade for a score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_status(score):
    """Return pass/fail status."""
    return "Pass" if score >= 60 else "Fail"

def print_separator():
    """Print a separator line."""
    print("=" * 40)

def print_header():
    """Print the report header."""
    print_separator()
    print("       STUDENT GRADE REPORT")
    print_separator()

def print_student_row(rank, name, score):
    """Print one student's row."""
    grade = get_grade(score)
    status = get_status(score)
    print(str(rank) + ". " + name.ljust(12) + str(score).rjust(4) + "  " + grade + "  " + status)

def print_summary(scores):
    """Print class summary statistics."""
    print_separator()
    print("CLASS SUMMARY")
    print_separator()
    n = len(scores)
    total = sum(scores)
    average = total / n
    print("Students:", n)
    print("Average:", round(average, 2))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))
    # Count grades
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        grade_counts[get_grade(score)] += 1
    print("Grade distribution:")
    for grade, count in grade_counts.items():
        print("  " + grade + ": " + str(count))
    print_separator()

# ============================================================
# MAIN PROGRAM
# ============================================================

print("=== Grade Calculator ===")
n = int(input("How many students? "))

names = []
scores = []

for i in range(n):
    name = input("Student " + str(i + 1) + " name: ")
    score = int(input("Score: "))
    names.append(name)
    scores.append(score)

# Sort by score (descending) — bubble sort on parallel lists
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[j] > scores[i]:
            scores[i], scores[j] = scores[j], scores[i]
            names[i], names[j] = names[j], names[i]

# Print the report
print()
print_header()
print("Rank  Name          Score  Grade  Status")
print("-" * 40)
for i in range(len(names)):
    print_student_row(i + 1, names[i], scores[i])

print_summary(scores)
