# example_01_parameter.py
# Lesson 29: Functions with parameters
# A parameter is a variable that receives a value when the function is called

# Function with one parameter
def greet(name):
    print("Hello,", name + "!")
    print("Nice to meet you,", name)

# Call with different arguments
greet("Alice")
print()
greet("Bob")
print()
greet("An")

print()
print("---")

# Function with one number parameter
def print_square(n):
    print(n, "x", n, "=", n * n)

print_square(3)    # 3 x 3 = 9
print_square(5)    # 5 x 5 = 25
print_square(10)   # 10 x 10 = 100

print()

# Scratch connection:
# In Scratch: "My Block" with input [name]
# In Python:  def greet(name):
# The input in Scratch = the parameter in Python
