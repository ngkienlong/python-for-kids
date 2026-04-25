# example_05_countdown.py
# Lesson 8: Countdown and real-world loop examples

# Rocket countdown
print("--- Rocket countdown ---")
for i in range(10, 0, -1):
    print(i, "...")
print("LAUNCH! 🚀")

# Print a ruler from 0 to 20 (step 5)
print("\n--- Ruler (0 to 20, step 5) ---")
for i in range(0, 21, 5):
    print(i)

# Sum of squares: 1^2 + 2^2 + ... + 5^2
print("\n--- Sum of squares 1 to 5 ---")
total = 0
for i in range(1, 6):
    square = i * i
    total = total + square
    print(i, "squared =", square, "| running total =", total)
print("Sum of squares:", total)
