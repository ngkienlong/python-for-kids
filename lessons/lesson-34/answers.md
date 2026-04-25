# Lesson 34: Answers 🏆

---

## 🟢 Easy

**E1.**
```python
name = input()
age = int(input())
height = float(input())
print(name + " is " + str(age) + " years old and " + str(height) + " cm tall.")
```

**E2.**
```python
temp = float(input())
if temp >= 35:
    print("Hot")
elif temp >= 20:
    print("Warm")
elif temp >= 10:
    print("Cool")
else:
    print("Cold")
```

**E3.**
```python
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

**E4.**
```python
n = int(input())
i = 2
while i <= n:
    print(i)
    i += 2
```

**E5.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
print(numbers)
print(len(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))
```

**E6.**
```python
import math

def circle_info(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    print("r =", r, "-> Area:", round(area, 2), "Circumference:", round(circumference, 2))

circle_info(3)
circle_info(5)
circle_info(7)
```

**E7.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
total = sum(numbers)
average = total / n
print(numbers)
print("Sum:", total)
print("Average:", round(average, 2))
print("Min:", min(numbers))
print("Max:", max(numbers))
if average > 50:
    print("Average is above 50")
else:
    print("Average is not above 50")
```

---

## 🟡 Medium

**M1.**
```python
def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

for i in range(1, 21):
    print(fizzbuzz(i))
```

**M2.**
```python
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
total = sum(numbers)
average = total / n
above = sum(1 for x in numbers if x > average)
print("Count:", n)
print("Sum:", total)
print("Average:", round(average, 2))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Range:", max(numbers) - min(numbers))
print("Above average:", above)
```

**M3.**
```python
def is_palindrome(s):
    return s == s[::-1]

n = int(input())
for i in range(n):
    word = input()
    print("yes" if is_palindrome(word) else "no")
```

**M4.**
```python
n = int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j) + " "
    print(row.strip())
```

**M5.**
```python
n = int(input())
students = []
for i in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    students.append((name, score))

students.sort(key=lambda x: x[1], reverse=True)

for i in range(len(students)):
    print(str(i + 1) + ". " + students[i][0] + ": " + str(students[i][1]))
```

**M6.**
```python
def shift_char(c, n):
    if c == " ":
        return " "
    return chr((ord(c) - ord('a') + n) % 26 + ord('a'))

message = input()
n = int(input())
result = ""
for c in message:
    result += shift_char(c, n)
print(result)
```

**M7.**
```python
questions = [
    ("What is 5 + 3?", "8"),
    ("What is the capital of France?", "paris"),
    ("What color is the sky?", "blue"),
]

score = 0
for question, answer in questions:
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer was:", answer)

print("Final score:", score, "/", len(questions))
```

---

## 🔴 Hard

**H1.**
```python
# Student grade book
n = int(input())
students = []
for i in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    students.append((name, score))

# Sort by score descending
students.sort(key=lambda x: x[1], reverse=True)

# Print ranked list
for i in range(len(students)):
    print(str(i + 1) + ". " + students[i][0] + ": " + str(students[i][1]))

# Print class average
total = sum(s[1] for s in students)
average = total / n
print("Class average:", round(average, 2))
```
*Explanation: Store each student as a (name, score) pair. Sort the list by score using `key=lambda x: x[1]`. Print with rank numbers. Calculate average from all scores.*

**H2.**
```python
# Number guessing game
secret = 42   # the computer's secret number
guesses = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Guess: "))
    guesses += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You got it in", guesses, "guesses.")
        break
```
*Explanation: Use a while True loop that only breaks when the guess is correct. Count each guess. Compare to the secret and give hints.*

**H3.**
```python
# Caesar cipher
def encode_message(message, shift):
    result = ""
    for c in message:
        if c == " ":
            result += " "
        elif c.isalpha():
            # Shift the letter, wrapping around with mod 26
            shifted = (ord(c.lower()) - ord('a') + shift) % 26
            result += chr(shifted + ord('a'))
        else:
            result += c
    return result

message = input()
shift = int(input())
print(encode_message(message, shift))
```
*Explanation: For each letter, find its 0-based position (ord(c) - ord('a')), add the shift, take mod 26 to wrap around, then convert back to a character.*

**H4.**
```python
# Prime factorization
n = int(input())
factors = []
divisor = 2
while n > 1:
    while n % divisor == 0:
        factors.append(divisor)
        n = n // divisor
    divisor += 1
print(" x ".join(str(f) for f in factors))
```
*Explanation: Start with divisor 2. While N is divisible by the current divisor, record it and divide N. When N is no longer divisible, try the next divisor. Continue until N becomes 1.*

**H5.**
```python
# Matrix sum
matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# Row sums
for i in range(3):
    row_sum = sum(matrix[i])
    print("Row " + str(i + 1) + ": " + str(row_sum))

# Column sums
for j in range(3):
    col_sum = 0
    for i in range(3):
        col_sum += matrix[i][j]
    print("Col " + str(j + 1) + ": " + str(col_sum))

# Main diagonal sum (top-left to bottom-right)
diag_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]
print("Diagonal:", diag_sum)
```
*Explanation: Store the matrix as a list of 3 lists. Sum each row directly. For columns, loop through rows and pick the j-th element. The diagonal is elements [0][0], [1][1], [2][2].*

**H6.**
```python
# Word frequency
n = int(input())
words = []
for i in range(n):
    words.append(input())

# Count each unique word
unique_words = []
counts = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
        counts.append(words.count(word))

# Sort by count descending (bubble sort on parallel lists)
for i in range(len(counts)):
    for j in range(i + 1, len(counts)):
        if counts[j] > counts[i]:
            counts[i], counts[j] = counts[j], counts[i]
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

for i in range(len(unique_words)):
    print(unique_words[i] + ": " + str(counts[i]))
```
*Explanation: Build a list of unique words and their counts. Sort both lists together by count (descending). Print each word with its count.*

**H7.**
```python
# Mini bank account
n = int(input())
balance = 0

for i in range(n):
    command = input().split()
    action = command[0]

    if action == "deposit":
        amount = int(command[1])
        balance += amount
        print("Balance:", balance)
    elif action == "withdraw":
        amount = int(command[1])
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print("Balance:", balance)
    elif action == "balance":
        print("Balance:", balance)
```
*Explanation: Parse each command by splitting the input. Use if/elif to handle deposit, withdraw, and balance. For withdraw, check if there are enough funds before subtracting.*
