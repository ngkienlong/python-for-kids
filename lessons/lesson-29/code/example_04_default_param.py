# example_04_default_param.py
# Lesson 29: Default parameter values
# If no argument is given, the default value is used

def greet(name="friend"):
    print("Hello,", name + "!")

# Call with an argument
greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!

# Call without an argument — uses default "friend"
greet()           # Hello, friend!

print()

# Default value for a number
def power(base, exp=2):
    result = 1
    for i in range(exp):
        result *= base
    return result

print("3^2 =", power(3))      # uses default exp=2 → 9
print("3^3 =", power(3, 3))   # exp=3 → 27
print("5^2 =", power(5))      # uses default exp=2 → 25
print("2^8 =", power(2, 8))   # exp=8 → 256

print()

# Multiple defaults
def make_greeting(name="friend", language="English"):
    if language == "English":
        return "Hello, " + name + "!"
    elif language == "Vietnamese":
        return "Xin chào, " + name + "!"
    else:
        return "Hi, " + name + "!"

print(make_greeting())                          # Hello, friend!
print(make_greeting("An"))                      # Hello, An!
print(make_greeting("An", "Vietnamese"))        # Xin chào, An!
print(make_greeting("Bob", "Spanish"))          # Hi, Bob!
