"""
Lesson 21 - Example 05: Divisibility Rules and Perfect Numbers
"""

# Divisibility rules using digit sums
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10     # add last digit
        n = n // 10         # remove last digit
    return total

print("--- Divisibility Rules ---")
test_numbers = [123, 450, 729, 1001, 315]
for n in test_numbers:
    ds = digit_sum(n)
    print(f"\nNumber: {n}  (digit sum = {ds})")
    print(f"  Div by 2:  {n % 2 == 0}  (last digit = {n % 10})")
    print(f"  Div by 3:  {n % 3 == 0}  (digit sum {ds} % 3 = {ds % 3})")
    print(f"  Div by 5:  {n % 5 == 0}  (last digit = {n % 10})")
    print(f"  Div by 9:  {n % 9 == 0}  (digit sum {ds} % 9 = {ds % 9})")
    print(f"  Div by 10: {n % 10 == 0} (last digit = {n % 10})")

# Perfect numbers
print("\n--- Perfect Numbers up to 1000 ---")
for n in range(1, 1001):
    proper_sum = sum(i for i in range(1, n) if n % i == 0)
    if proper_sum == n:
        divisors = [i for i in range(1, n) if n % i == 0]
        print(f"{n} is perfect: {' + '.join(str(d) for d in divisors)} = {proper_sum}")
