# example_01_if_else.py
# Lesson 5: Basic if/else
# In Scratch: the "if/else" block. In Python: if condition: ... else: ...

age = int(input("Enter your age: "))

# The condition is checked: is age >= 18?
if age >= 18:
    # This block runs ONLY if the condition is True
    print("You are an adult.")
else:
    # This block runs ONLY if the condition is False
    print("You are a child.")

# Only ONE branch runs — never both!
print("Program finished.")
