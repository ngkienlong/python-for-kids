# Lesson 28: Answers 🔧

---

## 🟢 Easy

**E1.**
```python
def say_hello():
    print("Hello, Python!")

say_hello()
```

**E2.**
```python
def print_name():
    print("An")

print_name()
print_name()
print_name()
```

**E3.**
```python
def print_stars():
    print("**********")

print_stars()
print_stars()
print_stars()
print_stars()
```

**E4.**
```python
def print_box():
    print("+--------+")
    print("|        |")
    print("+--------+")

print_box()
print_box()
```

**E5.**
```python
def print_banner():
    print("====================")
    print("   Welcome!")
    print("====================")

print_banner()
```

**E6.**
```python
def count_to_five():
    for i in range(1, 6):
        print(i)

count_to_five()
count_to_five()
```

**E7.**
```python
def print_stars():
    print("***")

def print_dashes():
    print("---")

def print_dots():
    print("...")

print_stars()
print_dashes()
print_dots()
print_stars()
```

---

## 🟡 Medium

**M1.**
```python
def print_header():
    print("=== REPORT ===")

def print_body():
    print("Name: An")
    print("Score: 95")

def print_footer():
    print("=== END ===")

print_header()
print_body()
print_footer()
```

**M2.**
```python
def print_times_table_3():
    for i in range(1, 11):
        print("3 x", i, "=", 3 * i)

print_times_table_3()
```

**M3.**
```python
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Blast off!")

countdown()
```

**M4.**
```python
def print_menu():
    print("=== MENU ===")
    print("1. Start game")
    print("2. View scores")
    print("3. Settings")
    print("4. Quit")

print_menu()
```

**M5.**
```python
def print_triangle():
    for i in range(1, 6):
        print("*" * i)

print_triangle()
print_triangle()
```

**M6.**
```python
def greet_user():
    print("Hello, User! Welcome back.")

greet_user()
greet_user()
greet_user()
```

**M7.**
```python
def print_checker_row():
    print("# # # # #")

def print_blank_row():
    print(". . . . .")

print_checker_row()
print_blank_row()
print_checker_row()
print_blank_row()
```

---

## 🔴 Hard

**H1.**
```python
def print_line():
    print("--------------------")

print_line()
print_line()
print_line()
```

**H2.**
```python
def print_welcome():
    print("**********************")
    print("*                    *")
    print("*   WELCOME TO       *")
    print("*   PYTHON CLASS!    *")
    print("*                    *")
    print("**********************")

print_welcome()
```

**H3.**
```python
def print_stars():
    print("********************")

def print_dashes():
    print("--------------------")

def print_dots():
    print("....................")

print_stars()
print_dashes()
print_dots()
print_dashes()
print_stars()
```

**H4.**
```python
def print_times_table_5():
    for i in range(1, 13):
        print("5 x", i, "=", 5 * i)

print_times_table_5()
```

**H5.**
```python
def print_separator():
    print("====================")

def print_menu():
    print("1. New game")
    print("2. Load game")
    print("3. High scores")
    print("4. Options")
    print("5. Exit")

print_separator()
print_menu()
print_separator()
```

**H6.**
```python
def print_fibonacci_10():
    a = 0
    b = 1
    for i in range(10):
        print(a)
        a, b = b, a + b

print_fibonacci_10()
```
*Explanation: Start with a=0, b=1. Each step: print a, then update a to b and b to a+b. This generates the Fibonacci sequence.*

**H7.**
```python
def print_title():
    print("=== STUDENT REPORT CARD ===")

def print_student_info():
    print("Name: An Nguyen")
    print("Class: 3A")
    print("---")

def print_scores():
    math = 95
    english = 88
    science = 92
    print("Math:", math)
    print("English:", english)
    print("Science:", science)
    print("---")

def print_summary():
    math = 95
    english = 88
    science = 92
    average = (math + english + science) / 3
    print("Average:", round(average, 2))
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    else:
        print("Grade: C")
    print("===========================")

print_title()
print_student_info()
print_scores()
print_summary()
```
*Explanation: Each function handles one section of the report. Calling them in order produces the complete report card.*
