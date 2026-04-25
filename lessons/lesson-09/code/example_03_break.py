# example_03_break.py
# Lesson 9: Using break to exit a loop early

# Break when we find the number 5
print("--- Break when count reaches 5 ---")
count = 1
while count <= 10:
    if count == 5:
        print("Found 5! Breaking out of the loop.")
        break
    print(count)
    count = count + 1
print("After the loop, count =", count)

# Search for a value — stop when found
print("\n--- Search for first multiple of 7 greater than 20 ---")
n = 21
while True:             # "while True" runs forever until break
    if n % 7 == 0:
        print("Found it:", n)
        break
    n = n + 1

# Break in a guessing game
print("\n--- Simple guessing game (secret = 42) ---")
secret = 42
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! You got it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
