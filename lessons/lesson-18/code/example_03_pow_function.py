"""
Lesson 18 - Example 03: The pow() Function
pow(base, exponent) does the same as base ** exponent
"""

# pow() works just like **
print("--- pow() Function ---")
print(pow(2, 10))       # 1024
print(pow(3, 3))        # 27
print(pow(5, 0))        # 1
print(pow(10, 4))       # 10000

# Comparing ** and pow()
base = 7
exp = 3
result_operator = base ** exp
result_function = pow(base, exp)
print(f"\n{base} ** {exp} = {result_operator}")
print(f"pow({base}, {exp}) = {result_function}")
print(f"Same result? {result_operator == result_function}")

# pow() with negative exponent
print("\n--- pow() with negative exponent ---")
print(pow(2, -1))       # 0.5
print(pow(10, -2))      # 0.01

# Reading base and exponent from user
print("\n--- User Input ---")
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print(f"pow({b}, {e}) = {pow(b, e)}")
