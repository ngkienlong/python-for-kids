# example_05_input_string.py
# Lesson 4: Working with string input
# Strings can be joined with + (concatenation) or printed with commas.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")

# Method 1: join with +
full_name = first_name + " " + last_name
print("Full name: " + full_name)

# Method 2: print with commas (adds spaces automatically)
print("Hello,", first_name, "from", city + "!")

# String length — how many characters?
print("Your first name has", len(first_name), "letters.")
