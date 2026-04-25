# example_04_combine.py
# Lesson 7: Combining and, or, not in real programs

# Example 1: Login system
print("=== Login ===")
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome, admin!")
else:
    print("Wrong username or password.")

print()

# Example 2: Number in range
print("=== Range Check ===")
n = int(input("Enter a number (1-100): "))

if n >= 1 and n <= 100:
    print(n, "is in range.")
else:
    print(n, "is out of range.")

print()

# Example 3: Vowel check using or
print("=== Vowel Check ===")
letter = input("Enter a lowercase letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")
