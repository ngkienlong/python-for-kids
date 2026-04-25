# Lesson 34: Grand Review & Challenge 🏆

> **Goal:** Review all concepts learned in the course and solve mixed challenge problems that combine everything.

---

## 1. What You've Learned — The Big Picture

Congratulations! You've completed the Python for Kids course. Let's review everything:

| Module | Topics |
|--------|--------|
| 1. Hello Python! | `print()`, math, variables, `input()` |
| 2. Making Decisions | `if`, `elif`, `else`, logic (`and`, `or`, `not`) |
| 3. Loops | `for`, `while`, nested loops |
| 4. Turtle Graphics | Drawing shapes, colors, patterns, scenes |
| 5. Math Power! | Powers, square roots, Pythagorean theorem, sequences |
| 6. Lists | Create, access, modify, sort, filter lists |
| 7. Functions | `def`, parameters, `return`, recursion |
| 8. Putting It Together | Combine all skills, problem solving |

---

## 2. Quick Review: Variables and Input

```python
name = input("Your name: ")
age = int(input("Your age: "))
print("Hello,", name + "! You are", age, "years old.")
```

---

## 3. Quick Review: Conditions

```python
score = int(input("Score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## 4. Quick Review: Loops

```python
# For loop
for i in range(1, 6):
    print(i)

# While loop
n = 10
while n > 0:
    print(n)
    n -= 2
```

---

## 5. Quick Review: Lists

```python
scores = [85, 92, 78, 95, 88]
scores.append(91)
scores.sort()
print("Sorted:", scores)
print("Average:", sum(scores) / len(scores))
```

---

## 6. Quick Review: Functions

```python
def greet(name, age):
    return "Hello, " + name + "! You are " + str(age) + " years old."

message = greet("Alice", 10)
print(message)
```

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| review | ôn tập | Go over what you've learned |
| challenge | thử thách | A harder problem to test your skills |
| combine | kết hợp | Use multiple concepts together |
| apply | áp dụng | Use knowledge to solve a problem |
| master | thành thạo | Know something very well |
| achievement | thành tích | Something you accomplished |
| celebrate | kỷ niệm | Recognize your success |
| reflect | suy ngẫm | Think about what you've learned |

---

## 8. Summary

✅ You know variables, input/output, math, and strings.
✅ You can make decisions with if/elif/else.
✅ You can repeat actions with for and while loops.
✅ You can draw with turtle graphics.
✅ You can store data in lists and process them.
✅ You can write reusable functions with parameters and return values.
✅ You can solve real problems by combining all these skills!

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Review: Variables and Math**

Read a person's name, age, and height (in cm). Print a summary line.

- **Input:** Three lines: name, age (int), height (float).
- **Output:** One summary line.

**Example:**

| Input | Output |
|-------|--------|
| Alice | Alice is 10 years old and 145.5 cm tall. |
| 10 | |
| 145.5 | |

---

**Exercise E2. Review: Conditions**

Read a temperature in Celsius. Print "Hot" if ≥ 35, "Warm" if ≥ 20, "Cool" if ≥ 10, "Cold" otherwise.

- **Input:** One number.
- **Output:** One word.

**Example:**

| Input | Output |
|-------|--------|
| 38 | Hot |
| 22 | Warm |
| 5 | Cold |

---

**Exercise E3. Review: For Loop**

Print the multiplication table for a number N (N × 1 through N × 10).

- **Input:** One integer N.
- **Output:** 10 lines.

**Example:**

| Input | Output |
|-------|--------|
| 7 | 7 x 1 = 7 |
| | 7 x 2 = 14 |
| | ... |
| | 7 x 10 = 70 |

---

**Exercise E4. Review: While Loop**

Read a number N. Use a while loop to print all even numbers from 2 to N.

- **Input:** One integer N.
- **Output:** Even numbers from 2 to N.

**Example:**

| Input | Output |
|-------|--------|
| 10 | 2 |
| | 4 |
| | 6 |
| | 8 |
| | 10 |

---

**Exercise E5. Review: Lists**

Read N numbers into a list. Print the list, its length, sum, and average.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Four lines.

**Example:**

| Input | Output |
|-------|--------|
| 4 | [10, 20, 30, 40] |
| 10 | 4 |
| 20 | 100 |
| 30 | 25.0 |
| 40 | |

---

**Exercise E6. Review: Functions**

Write a function `circle_info(r)` that prints the area and circumference of a circle with radius r. Call it for r = 3, 5, 7.

- **Input:** None.
- **Output:** Area and circumference for each radius.

---

**Exercise E7. Review: All Together**

Read N numbers. Print: the list, sum, average, min, max, and whether the average is above 50.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Six lines.

---

### 🟡 Medium

---

**Exercise M1. FizzBuzz with Functions**

Write a function `fizzbuzz(n)` that returns "Fizz" if n is divisible by 3, "Buzz" if by 5, "FizzBuzz" if by both, else the number as a string. Print fizzbuzz(1) through fizzbuzz(20).

- **Input:** None.
- **Output:** 20 lines.

---

**Exercise M2. List Statistics**

Read N numbers. Print: count, sum, average, min, max, range, and how many are above average.

- **Input:** First line: N. Next N lines: numbers.
- **Output:** Seven lines.

---

**Exercise M3. Palindrome Checker**

Write a function `is_palindrome(s)`. Read N words and print "yes" or "no" for each.

- **Input:** First line: N. Next N lines: words.
- **Output:** "yes" or "no" for each word.

---

**Exercise M4. Number Pattern**

Print this pattern for N rows:
```
1
1 2
1 2 3
1 2 3 4
```

- **Input:** One integer N.
- **Output:** N rows of the pattern.

---

**Exercise M5. Sort and Rank**

Read N names and scores. Sort by score (descending) and print a ranked list.

- **Input:** First line: N. Next N lines: name and score.
- **Output:** Ranked list.

**Example:**

| Input | Output |
|-------|--------|
| 3 | 1. Bob: 95 |
| Alice 85 | 2. Alice: 85 |
| Bob 95 | 3. Charlie: 72 |
| Charlie 72 | |

---

**Exercise M6. Caesar Cipher (Simple)**

Write a function `shift_char(c, n)` that shifts a letter by n positions. Read a message and shift N. Print the encoded message.

- **Input:** First line: message (lowercase letters and spaces). Second line: shift N.
- **Output:** Encoded message.

**Example:**

| Input | Output |
|-------|--------|
| hello | khoor |
| 3 | |

---

**Exercise M7. Mini Quiz**

Write a quiz program with 3 questions. For each question, read the answer and check if it's correct. Print the final score.

- **Input:** 3 answers.
- **Output:** Correct/Wrong for each, then final score.

---

### 🔴 Hard

---

**Exercise H1. Student Grade Book**

Read N students, each with a name and score. Print them sorted by score (descending). Print the class average.

- **Input:** First line: N. Next N lines: name and score.
- **Output:** Sorted list with rank, then class average.

**Example:**

| Input | Output |
|-------|--------|
| 4 | 1. Bob: 95 |
| Alice 85 | 2. Alice: 85 |
| Bob 95 | 3. Diana: 78 |
| Charlie 72 | 4. Charlie: 72 |
| Diana 78 | Class average: 82.5 |

**Explanation:** Read names and scores into parallel lists (or a list of pairs). Sort by score descending. Print ranked. Calculate and print average.

---

**Exercise H2. Number Guessing Game**

The computer picks a secret number from 1 to 100 (use `secret = 42` for testing). The user guesses. Give "Too high" or "Too low" hints. Count guesses. Print "Correct! You got it in X guesses."

- **Input:** Repeated guesses until correct.
- **Output:** Hints and final message.

**Example:**
```
Guess: 50
Too high!
Guess: 25
Too low!
Guess: 42
Correct! You got it in 3 guesses.
```

**Explanation:** Use a while loop. Keep a guess counter. Compare each guess to the secret number.

---

**Exercise H3. Caesar Cipher**

Read a message and a shift N. Encode each letter by shifting N positions in the alphabet (wrap around: z + 1 = a). Keep spaces unchanged.

- **Input:** First line: message (lowercase letters and spaces). Second line: N.
- **Output:** Encoded message.

**Example:**

| Input | Output |
|-------|--------|
| hello world | khoor zruog |
| 3 | |

**Explanation:** For each letter, find its position (a=0, b=1, ...), add N, take mod 26, convert back to a letter.

---

**Exercise H4. Prime Factorization**

Read N. Print its prime factors. For example, 12 = 2 × 2 × 3.

- **Input:** One integer N (N ≥ 2).
- **Output:** Prime factors separated by " x ".

**Example:**

| Input | Output |
|-------|--------|
| 12 | 2 x 2 x 3 |
| 30 | 2 x 3 x 5 |
| 7 | 7 |

**Explanation:** Start with divisor 2. While N > 1: if N is divisible by divisor, record it and divide N. Otherwise, increment divisor.

---

**Exercise H5. Matrix Sum**

Read a 3×3 matrix of numbers (3 rows, 3 numbers per row). Print: each row sum, each column sum, and the main diagonal sum.

- **Input:** 3 lines, each with 3 numbers separated by spaces.
- **Output:** Row sums, column sums, diagonal sum.

**Example:**

| Input | Output |
|-------|--------|
| 1 2 3 | Row 1: 6 |
| 4 5 6 | Row 2: 15 |
| 7 8 9 | Row 3: 24 |
| | Col 1: 12 |
| | Col 2: 15 |
| | Col 3: 18 |
| | Diagonal: 15 |

**Explanation:** Store the matrix as a list of lists. Sum each row, each column, and the diagonal (elements at [0][0], [1][1], [2][2]).

---

**Exercise H6. Word Frequency**

Read N words. Print each unique word and how many times it appears, sorted by frequency (most frequent first).

- **Input:** First line: N. Next N lines: one word each.
- **Output:** Word and count, sorted by count descending.

**Example:**

| Input | Output |
|-------|--------|
| 7 | apple: 3 |
| apple | banana: 2 |
| banana | cherry: 1 |
| apple | mango: 1 |
| cherry | |
| banana | |
| apple | |
| mango | |

**Explanation:** Count occurrences of each word. Sort by count descending. Print each word and its count.

---

**Exercise H7. Mini Bank Account**

Simulate a bank account. Read commands: "deposit X", "withdraw X", or "balance". Maintain a running balance starting at 0. Print the balance after each command. If withdrawal exceeds balance, print "Insufficient funds".

- **Input:** First line: N (number of commands). Next N lines: commands.
- **Output:** Response to each command.

**Example:**

| Input | Output |
|-------|--------|
| 5 | Balance: 100 |
| deposit 100 | Balance: 150 |
| deposit 50 | Balance: 80 |
| withdraw 70 | Insufficient funds |
| withdraw 200 | Balance: 80 |
| balance | |

**Explanation:** Use a variable `balance = 0`. Parse each command. For deposit: add to balance. For withdraw: check if enough, then subtract. For balance: print current balance.
