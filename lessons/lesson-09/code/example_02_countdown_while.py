# example_02_countdown_while.py
# Lesson 9: Countdown using while loop

# Rocket countdown
print("--- Rocket countdown ---")
countdown = 10
while countdown > 0:
    print(countdown, "...")
    countdown = countdown - 1
print("LAUNCH! 🚀")

# Sum accumulator with while loop
print("\n--- Sum 1 to 10 using while ---")
total = 0
i = 1
while i <= 10:
    total = total + i
    i = i + 1
print("Sum =", total)

# Powers of 2 less than 1000
print("\n--- Powers of 2 less than 1000 ---")
power = 1
while power < 1000:
    print(power)
    power = power * 2
