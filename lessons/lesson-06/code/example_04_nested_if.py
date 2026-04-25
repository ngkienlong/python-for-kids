# example_04_nested_if.py
# Lesson 6: Nested if — an if statement inside another if statement

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

# Outer if: check age first
if age >= 18:
    # Inner if: only reached if age >= 18
    if has_ticket == "yes":
        print("Welcome! Enjoy the show.")
    else:
        print("Please buy a ticket first.")
else:
    # This runs if age < 18 — the inner if is never checked
    print("Sorry, this show is for adults only.")

# The inner if only runs when the outer if is True.
# This is called "nested if".
