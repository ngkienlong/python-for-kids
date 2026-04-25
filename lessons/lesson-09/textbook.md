# Lesson 9: While Loop — Repeat Until 🔄

> **Goal:** Use `while` loops to repeat code while a condition is true, and know when to use `while` vs `for`.

---

## 1. What is a While Loop?

A `while` loop keeps running **as long as a condition is True**. It's perfect when you don't know in advance how many times to repeat.

> 💡 **Scratch connection:** The `while` loop is like the **"repeat until"** block in Scratch — but reversed! "repeat until X" means "keep going until X is true". `while condition` means "keep going while condition is true".

| Scratch | Python |
|---------|--------|
| `repeat until (score = 10)` | `while score != 10:` |
| `repeat until (answer = "yes")` | `while answer != "yes":` |
| Code inside the repeat-until block | Indented code inside `while` |

---

## 2. Basic `while` Loop

```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
```

**Output:**
```
1
2
3
4
5
```

How it works:
1. Check: is `count <= 5`? Yes (count = 1) → run the body.
2. Print 1, then `count` becomes 2.
3. Check again: is `count <= 5`? Yes (count = 2) → run the body.
4. ... keep going ...
5. Check: is `count <= 5`? No (count = 6) → **stop**.

> ⚠️ **Important:** You must update the variable inside the loop (`count = count + 1`). If you forget, the loop runs forever!

---

## 3. Infinite Loop Warning

```python
# DANGER: This loop runs forever!
count = 1
while count <= 5:
    print(count)
    # Forgot to update count!
```

If your program seems stuck, press **Ctrl + C** to stop it.

---

## 4. `break` — Exit the Loop Early

`break` immediately stops the loop, even if the condition is still True.

```python
count = 1
while count <= 10:
    if count == 5:
        break           # stop when count reaches 5
    print(count)
    count = count + 1
print("Loop ended at count =", count)
```

**Output:**
```
1
2
3
4
Loop ended at count = 5
```

---

## 5. Input Validation Loop

A very useful pattern: keep asking the user for input until they give a valid answer.

```python
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Invalid age! Try again.")
    age = int(input("Enter your age: "))
print("Your age is:", age)
```

This keeps asking until the user enters a number between 0 and 120.

---

## 6. `for` vs `while` — When to Use Which?

| Situation | Use |
|-----------|-----|
| You know exactly how many times to repeat | `for` |
| You repeat until a condition changes | `while` |
| Looping through a range of numbers | `for` |
| Waiting for valid user input | `while` |
| Counting up/down a fixed amount | `for` |
| Unknown number of repetitions | `while` |

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| while | trong khi | Keep looping while condition is True |
| condition | điều kiện | A True/False expression that controls the loop |
| infinite loop | vòng lặp vô hạn | A loop that never stops (a bug!) |
| break | thoát vòng lặp | Exit the loop immediately |
| terminate | kết thúc | Stop the loop |
| update | cập nhật | Change the loop variable so the loop can end |
| iteration | lần lặp | One pass through the loop body |
| sentinel | giá trị dừng | A special value that signals the loop to stop |
| validate | kiểm tra hợp lệ | Check that input meets requirements |
| input validation | kiểm tra đầu vào | Looping until the user gives valid input |

---

## 8. Summary

✅ `while condition:` runs as long as condition is True.
✅ Always update something inside the loop to avoid infinite loops.
✅ `break` exits the loop immediately.
✅ Use `while` when you don't know how many repetitions are needed.
✅ Use `for` when you know the exact count.
✅ Input validation: keep asking until the user gives a valid answer.

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Count to 10**

Use a `while` loop to print numbers 1 through 10.

- **Input:** None.
- **Output:**
```
1
2
3
4
5
6
7
8
9
10
```

---

**Exercise E2. Count Down**

Use a `while` loop to count down from 5 to 1, then print "Done!".

- **Input:** None.
- **Output:**
```
5
4
3
2
1
Done!
```

---

**Exercise E3. Sum to 100**

Use a `while` loop to find the sum 1 + 2 + 3 + ... until the sum first reaches or exceeds 100. Print the final sum.

- **Input:** None.
- **Output:**
```
105
```

*(Hint: 1+2+...+13 = 91, 1+2+...+14 = 105.)*

---

**Exercise E4. Powers of 2**

Use a `while` loop to print powers of 2 that are less than 1000: 1, 2, 4, 8, 16, ...

- **Input:** None.
- **Output:**
```
1
2
4
8
16
32
64
128
256
512
```

---

**Exercise E5. Break at 7**

Use a `while` loop that counts from 1 upward. Use `break` to stop when the counter reaches 7. Print each number before breaking.

- **Input:** None.
- **Output:**
```
1
2
3
4
5
6
```

---

**Exercise E6. Repeat Until Positive**

Keep asking the user to enter a positive number. If they enter 0 or negative, ask again. When they enter a positive number, print it.

- **Input:** One or more integers (the last one is positive).
- **Output:** Print the valid positive number.

**Example:**

| Input | Output |
|-------|--------|
| -3 then 0 then 5 | 5 |

---

**Exercise E7. Multiply Up**

Start with `n = 1`. Keep multiplying by 2 until n is greater than 100. Print the final value of n.

- **Input:** None.
- **Output:**
```
128
```

---

### 🟡 Medium

---

**Exercise M1. Guess the Number**

The secret number is 7. Ask the user to guess. Keep asking until they guess correctly. Print "Correct!" when they get it.

- **Input:** One or more integers (guesses).
- **Output:** Print "Too low!", "Too high!", or "Correct!" for each guess.

**Example:**

| Input | Output |
|-------|--------|
| 3 | Too low! |
| 10 | Too high! |
| 7 | Correct! |

---

**Exercise M2. Sum of Positives**

Keep reading integers from the user. Stop when the user enters 0. Print the sum of all positive numbers entered.

- **Input:** Several integers ending with 0.
- **Output:** One integer — the sum of positive numbers.

**Example:**

| Input | Output |
|-------|--------|
| 3 5 -2 8 0 | 16 |

---

**Exercise M3. Count Digits**

Read a positive integer N. Count how many digits it has using a `while` loop and `//`.

- **Input:** One integer N (1 ≤ N ≤ 1000000).
- **Output:** One integer — the number of digits.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1 |
| 42 | 2 |
| 1000 | 4 |

---

**Exercise M4. Fibonacci Sequence**

Print the Fibonacci sequence (each number is the sum of the two before it) while the values are less than 100. Start with 1, 1.

- **Input:** None.
- **Output:**
```
1
1
2
3
5
8
13
21
34
55
89
```

---

**Exercise M5. Divisor Check**

Read a positive integer N. Use a `while` loop to find and print all divisors of N (numbers that divide N evenly).

- **Input:** One integer N (1 ≤ N ≤ 100).
- **Output:** All divisors of N, one per line.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 1 |
| | 2 |
| | 3 |
| | 4 |
| | 6 |
| | 12 |

---

**Exercise M6. Reverse Digits**

Read a positive integer N. Use a `while` loop to reverse its digits and print the result.

- **Input:** One integer N (1 ≤ N ≤ 99999).
- **Output:** One integer — N with its digits reversed.

**Example:**

| Input | Output |
|-------|--------|
| 1234 | 4321 |
| 100 | 1 |
| 7 | 7 |

---

**Exercise M7. Collatz Steps**

The Collatz sequence: if N is even, divide by 2; if N is odd, multiply by 3 and add 1. Count how many steps it takes to reach 1.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** One integer — the number of steps to reach 1.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 8 |
| 1 | 0 |
| 27 | 111 |

---

### 🔴 Hard

---

**Exercise H1. Sum Until Zero**

Minh is collecting donations. People give him money one by one. He stops collecting when someone gives 0. Write a program that reads donations and prints the total.

- **Input:** Several integers, ending with 0. Each integer is ≥ 0.
- **Output:** One integer — the total sum (not counting the 0).

**Example:**

| Input | Output |
|-------|--------|
| 100 200 50 0 | 350 |
| 0 | 0 |

**Explanation:** Keep reading numbers and adding them. Stop when you read 0.

---

**Exercise H2. Count Digits**

A post office needs to know how many digits are in a package tracking number N. Write a program that counts the digits using a `while` loop.

- **Input:** One integer N (1 ≤ N ≤ 1000000000).
- **Output:** One integer — the number of digits in N.

**Example:**

| Input | Output |
|-------|--------|
| 5 | 1 |
| 123 | 3 |
| 1000000 | 7 |

**Explanation:** Repeatedly divide by 10 and count until N becomes 0.

---

**Exercise H3. Collatz Sequence**

A mathematician discovered a famous sequence: start with any number N. If N is even, divide by 2. If N is odd, multiply by 3 and add 1. Repeat until you reach 1. Print the whole sequence.

- **Input:** One integer N (1 ≤ N ≤ 1000).
- **Output:** Print each number in the sequence, one per line, including N and ending with 1.

**Example:**

| Input | Output |
|-------|--------|
| 6 | 6 |
| | 3 |
| | 10 |
| | 5 |
| | 16 |
| | 8 |
| | 4 |
| | 2 |
| | 1 |

---

**Exercise H4. Reverse a Number**

A spy needs to reverse a secret code number. Write a program that reverses the digits of N using a `while` loop and `%`.

- **Input:** One integer N (1 ≤ N ≤ 1000000).
- **Output:** One integer — N with its digits reversed (leading zeros are dropped).

**Example:**

| Input | Output |
|-------|--------|
| 1234 | 4321 |
| 1200 | 21 |
| 7 | 7 |

**Explanation:** Use `% 10` to get the last digit, build the reversed number by multiplying by 10 and adding.

---

**Exercise H5. Find First Multiple**

A teacher asks: "What is the smallest multiple of K that is greater than N?" Write a program to find it.

- **Input:** Two integers N and K (1 ≤ N ≤ 10000, 1 ≤ K ≤ 100).
- **Output:** One integer — the smallest multiple of K that is greater than N.

**Example:**

| Input | Output |
|-------|--------|
| 10 3 | 12 |
| 20 7 | 21 |
| 15 5 | 20 |

**Explanation:** For N=10, K=3: multiples of 3 are 3, 6, 9, 12, ... The first one greater than 10 is 12.

---

**Exercise H6. Power Without `**`**

A student wants to calculate base^exp without using the `**` operator. Write a program using a `while` loop to multiply base by itself exp times.

- **Input:** Two integers base and exp (1 ≤ base ≤ 10, 0 ≤ exp ≤ 10).
- **Output:** One integer — base raised to the power exp.

**Example:**

| Input | Output |
|-------|--------|
| 2 8 | 256 |
| 3 4 | 81 |
| 5 0 | 1 |

**Explanation:** 2^8 = 2×2×2×2×2×2×2×2 = 256. Multiply in a loop exp times.

---

**Exercise H7. Number of Divisors**

A number is called "highly composite" if it has many divisors. Write a program that counts how many numbers from 1 to N divide N evenly.

- **Input:** One integer N (1 ≤ N ≤ 10000).
- **Output:** One integer — the number of divisors of N.

**Example:**

| Input | Output |
|-------|--------|
| 12 | 6 |
| 7 | 2 |
| 1 | 1 |

**Explanation:** Divisors of 12 are: 1, 2, 3, 4, 6, 12 → 6 divisors. A prime number always has exactly 2 divisors.
