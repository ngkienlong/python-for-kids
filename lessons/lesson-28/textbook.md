# Lesson 28: What is a Function? 🔧

> **Goal:** Define functions with `def`, call them, and understand why functions make code better.

---

## 1. What is a Function?

A **function** is a named block of code that you can run whenever you want.

> 💡 **Scratch connection:** In Scratch, you create "My Blocks" to make reusable code. In Python, you use `def` to define a function!

| Scratch | Python |
|---------|--------|
| Create "My Block" called greet | `def greet():` |
| Use the block | `greet()` |
| Code inside the block | Indented code inside `def` |

---

## 2. Defining a Function

Use `def` to define a function:

```python
def greet():
    print("Hello!")
    print("Welcome to Python!")
```

- `def` = "define" (create a function)
- `greet` = the name of the function
- `():` = parentheses and colon (required)
- The indented lines = the **body** of the function

> ⚠️ Defining a function does NOT run it. You must **call** it!

---

## 3. Calling a Function

To run a function, write its name followed by `()`:

```python
def greet():
    print("Hello!")
    print("Welcome to Python!")

# Call the function
greet()
```

**Output:**
```
Hello!
Welcome to Python!
```

---

## 4. Call a Function Many Times

One of the best things about functions: call them as many times as you want!

```python
def print_line():
    print("--------------------")

print_line()
print("My Report")
print_line()
print("Score: 95")
print_line()
```

**Output:**
```
--------------------
My Report
--------------------
Score: 95
--------------------
```

---

## 5. Why Use Functions? — DRY Principle

**DRY = Don't Repeat Yourself.**

Without functions (bad):
```python
print("--------------------")
print("Hello!")
print("--------------------")
print("--------------------")
print("Goodbye!")
print("--------------------")
```

With functions (good):
```python
def print_line():
    print("--------------------")

print_line()
print("Hello!")
print_line()
print_line()
print("Goodbye!")
print_line()
```

Functions make code:
- **Shorter** — write once, use many times
- **Readable** — the function name explains what it does
- **Easier to fix** — change the function once, it's fixed everywhere

---

## 6. Functions Must Be Defined BEFORE They Are Called

```python
# WRONG — calling before defining
greet()          # ❌ Error! Python doesn't know greet yet

def greet():
    print("Hello!")
```

```python
# CORRECT — define first, then call
def greet():     # ✅ Define first
    print("Hello!")

greet()          # ✅ Then call
```

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| function | hàm | A named block of reusable code |
| define | định nghĩa | Create a function with `def` |
| call | gọi | Run a function by writing its name with `()` |
| body | thân hàm | The indented code inside a function |
| DRY | Đừng lặp lại | Don't Repeat Yourself — write code once |
| reuse | tái sử dụng | Use the same code in multiple places |
| organize | tổ chức | Arrange code into logical sections |
| invoke | gọi thực thi | Same as "call" |
| execute | thực thi | Run the code |
| definition | định nghĩa | The `def` block that creates a function |
| declaration | khai báo | Same as definition |
| modular | mô-đun hóa | Organized into separate, reusable pieces |

---

## 8. Summary

✅ `def name():` defines a function.
✅ The indented code inside is the function body.
✅ `name()` calls (runs) the function.
✅ You can call a function many times.
✅ Functions must be defined BEFORE they are called.
✅ Functions follow the DRY principle: Don't Repeat Yourself.

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Hello Function**

Write a function called `say_hello()` that prints "Hello, Python!". Call it once.

- **Input:** None.
- **Output:**
```
Hello, Python!
```

---

**Exercise E2. Print Name**

Write a function called `print_name()` that prints your name. Call it 3 times.

- **Input:** None.
- **Output:** (example)
```
An
An
An
```

---

**Exercise E3. Print Stars**

Write a function called `print_stars()` that prints a line of 10 stars. Call it 4 times.

- **Input:** None.
- **Output:**
```
**********
**********
**********
**********
```

---

**Exercise E4. Print Box**

Write a function called `print_box()` that prints:
```
+--------+
|        |
+--------+
```
Call it twice.

- **Input:** None.
- **Output:** The box printed twice.

---

**Exercise E5. Greeting Banner**

Write a function called `print_banner()` that prints:
```
====================
   Welcome!
====================
```
Call it once.

- **Input:** None.
- **Output:** The banner.

---

**Exercise E6. Count to 5**

Write a function called `count_to_five()` that prints the numbers 1 through 5. Call it twice.

- **Input:** None.
- **Output:**
```
1
2
3
4
5
1
2
3
4
5
```

---

**Exercise E7. Print Separator**

Write three functions: `print_stars()` (prints `***`), `print_dashes()` (prints `---`), `print_dots()` (prints `...`). Call them in order: stars, dashes, dots, stars.

- **Input:** None.
- **Output:**
```
***
---
...
***
```

---

### 🟡 Medium

---

**Exercise M1. Organized Report**

Write functions `print_header()`, `print_body()`, and `print_footer()`. Use them to print a formatted report.

- **Input:** None.
- **Output:** (example)
```
=== REPORT ===
Name: An
Score: 95
=== END ===
```

---

**Exercise M2. Times Table 3**

Write a function called `print_times_table_3()` that prints the 3× multiplication table (3×1 through 3×10). Call it.

- **Input:** None.
- **Output:**
```
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
```

---

**Exercise M3. Countdown**

Write a function called `countdown()` that counts down from 10 to 1, then prints "Blast off!". Call it.

- **Input:** None.
- **Output:**
```
10
9
...
1
Blast off!
```

---

**Exercise M4. Print Menu**

Write a function called `print_menu()` that prints a numbered menu with 4 options. Call it.

- **Input:** None.
- **Output:** (example)
```
=== MENU ===
1. Start game
2. View scores
3. Settings
4. Quit
```

---

**Exercise M5. Print Pattern**

Write a function called `print_triangle()` that prints a triangle of stars (5 rows). Call it twice.

- **Input:** None.
- **Output:**
```
*
**
***
****
*****
*
**
***
****
*****
```

---

**Exercise M6. Greet Three Times**

Write a function called `greet_user()` that prints "Hello, User! Welcome back." Call it 3 times.

- **Input:** None.
- **Output:**
```
Hello, User! Welcome back.
Hello, User! Welcome back.
Hello, User! Welcome back.
```

---

**Exercise M7. Print Checkerboard Row**

Write a function called `print_checker_row()` that prints `# # # # #`. Write another called `print_blank_row()` that prints `. . . . .`. Alternate them 4 times.

- **Input:** None.
- **Output:**
```
# # # # #
. . . . .
# # # # #
. . . . .
```

---

### 🔴 Hard

---

**Exercise H1. Print Line 3 Times**

Write a function `print_line()` that prints exactly 20 dashes. Call it 3 times.

- **Input:** None.
- **Output:**
```
--------------------
--------------------
--------------------
```

**Explanation:** Define the function once, call it 3 times. The function body has one `print()` statement.

---

**Exercise H2. Welcome Banner**

Write a function `print_welcome()` that prints a decorative welcome banner (at least 5 lines). Call it.

- **Input:** None.
- **Output:** (example)
```
**********************
*                    *
*   WELCOME TO       *
*   PYTHON CLASS!    *
*                    *
**********************
```

**Explanation:** The function prints each line of the banner. Call it once to display it.

---

**Exercise H3. Decorative Border**

Write three functions: `print_stars()` (prints 20 stars), `print_dashes()` (prints 20 dashes), `print_dots()` (prints 20 dots). Use them to print a decorative border pattern: stars, dashes, dots, dashes, stars.

- **Input:** None.
- **Output:**
```
********************
--------------------
....................
--------------------
********************
```

**Explanation:** Call the functions in order to build the pattern.

---

**Exercise H4. Times Table 5**

Write a function `print_times_table_5()` that prints the complete 5× multiplication table (5×1 through 5×12). Call it.

- **Input:** None.
- **Output:**
```
5 x 1 = 5
5 x 2 = 10
...
5 x 12 = 60
```

**Explanation:** Use a `for` loop inside the function.

---

**Exercise H5. Print Menu and Separator**

Write a function `print_menu()` that prints a numbered menu with 5 options. Write a function `print_separator()` that prints a line of `=` signs. Print: separator, menu, separator.

- **Input:** None.
- **Output:** (example)
```
====================
1. New game
2. Load game
3. High scores
4. Options
5. Exit
====================
```

**Explanation:** Call `print_separator()`, then `print_menu()`, then `print_separator()` again.

---

**Exercise H6. Print Fibonacci 10**

Write a function `print_fibonacci_10()` that prints the first 10 Fibonacci numbers (starting from 0). Call it.

- **Input:** None.
- **Output:**
```
0
1
1
2
3
5
8
13
21
34
```

**Explanation:** Use variables `a = 0` and `b = 1` inside the function. In each step, print `a`, then update: `a, b = b, a + b`.

---

**Exercise H7. Full Report**

Write functions: `print_title()`, `print_student_info()`, `print_scores()`, `print_summary()`. Use them to print a complete student report card.

- **Input:** None (hardcode the data).
- **Output:** (example)
```
=== STUDENT REPORT CARD ===
Name: An Nguyen
Class: 3A
---
Math: 95
English: 88
Science: 92
---
Average: 91.67
Grade: A
===========================
```

**Explanation:** Each function prints one section of the report. Call them in order.
