# example_02_return_value.py
# Lesson 29: Functions that return values
# return sends a value back to the caller

def square(n):
    return n * n   # send n*n back to whoever called this function

# Use the returned value
result = square(5)
print("5 squared =", result)   # 25

# Use directly in print
print("7 squared =", square(7))   # 49

# Use in a calculation
area = square(4)
print("Area of 4x4 square:", area)   # 16

print()

# Without return — the function gives None
def greet_no_return(name):
    print("Hello,", name)

x = greet_no_return("Alice")   # prints "Hello, Alice"
print("Return value:", x)       # None

print()

# With return — the function gives a value
def greet_with_return(name):
    return "Hello, " + name

message = greet_with_return("Bob")
print(message)   # Hello, Bob

print()

# Return True or False
def is_adult(age):
    return age >= 18

print("Age 20 is adult:", is_adult(20))   # True
print("Age 15 is adult:", is_adult(15))   # False
