# example_05_guess_number.py
# Lesson 9: Guess the number game
# The computer picks 7. The user keeps guessing until correct.

secret_number = 7       # the computer's secret number
attempts = 0            # count how many guesses the user makes

print("I'm thinking of a number between 1 and 10.")
print("Can you guess it?")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! The number was", secret_number)
        print("You got it in", attempts, "guess(es)!")
        break           # exit the loop when the guess is correct
