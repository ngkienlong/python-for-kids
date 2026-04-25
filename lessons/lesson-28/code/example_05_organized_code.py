# example_05_organized_code.py
# Lesson 28: Compare messy code vs organized code with functions

# ============================================================
# MESSY VERSION (without functions) — hard to read and change
# ============================================================

print("=== MESSY VERSION ===")
print()

# Student 1
print("--- Student 1 ---")
name1 = "Alice"
score1 = 85
print("Name:", name1)
print("Score:", score1)
if score1 >= 90:
    print("Grade: A")
elif score1 >= 80:
    print("Grade: B")
else:
    print("Grade: C")
print()

# Student 2 (same code repeated!)
print("--- Student 2 ---")
name2 = "Bob"
score2 = 92
print("Name:", name2)
print("Score:", score2)
if score2 >= 90:
    print("Grade: A")
elif score2 >= 80:
    print("Grade: B")
else:
    print("Grade: C")
print()

# ============================================================
# ORGANIZED VERSION (with functions) — clean and easy to change
# ============================================================

print("=== ORGANIZED VERSION ===")
print()

def print_student_report(name, score):
    """Print a student's name, score, and grade."""
    print("--- Student ---")
    print("Name:", name)
    print("Score:", score)
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    else:
        print("Grade: C")
    print()

# Now it's easy to add more students!
print_student_report("Alice", 85)
print_student_report("Bob", 92)
print_student_report("Charlie", 74)

# If we want to change the format, we only change the function ONCE.
