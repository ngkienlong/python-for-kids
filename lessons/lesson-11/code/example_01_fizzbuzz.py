# example_01_fizzbuzz.py
# Lesson 11: FizzBuzz — the classic coding challenge
# Rules: Fizz for multiples of 3, Buzz for multiples of 5,
#        FizzBuzz for multiples of both, number otherwise.

print("--- FizzBuzz 1 to 20 ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:  # check BOTH first!
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Count how many Fizz, Buzz, FizzBuzz in 1 to 100
print("\n--- Counting in 1 to 100 ---")
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz_count = fizzbuzz_count + 1
    elif i % 3 == 0:
        fizz_count = fizz_count + 1
    elif i % 5 == 0:
        buzz_count = buzz_count + 1
print("Fizz:", fizz_count)
print("Buzz:", buzz_count)
print("FizzBuzz:", fizzbuzz_count)
