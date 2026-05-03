# example_03_type_conversion.py
# Lesson 4: Type conversion (casting)
# int(), float(), str() convert between types.

# String to integer
s = "42"
n = int(s)
print(n + 8)        # 50  (math works now!)

# String to float
s2 = "3.14"
f = float(s2)
print(f * 2)        # 6.28

# Integer to string
age = 10
message = "I am " + str(age) + " years old."
print(message)

# int() cuts off the decimal — it does NOT round!
print(int(3.9))     # 3  (not 4!)
print(int(7.1))     # 7

# float() adds a decimal point
print(float(5))     # 5.0
