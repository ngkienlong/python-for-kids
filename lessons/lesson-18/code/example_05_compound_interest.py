"""
Lesson 18 - Example 05: Compound Interest
Formula: A = P * (1 + r/100) ** n
"""

# Compound interest formula
# A = final amount
# P = principal (starting amount)
# r = annual interest rate (%)
# n = number of years

print("--- Compound Interest Calculator ---")
P = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
n = int(input("Enter number of years: "))

# Calculate final amount
A = P * (1 + r / 100) ** n

print(f"\nStarting amount: ${P:.2f}")
print(f"Interest rate:   {r}% per year")
print(f"Years:           {n}")
print(f"Final amount:    ${A:.2f}")
print(f"Interest earned: ${A - P:.2f}")

# Show year-by-year growth
print("\n--- Year by Year ---")
balance = P
for year in range(1, n + 1):
    balance = balance * (1 + r / 100)
    print(f"Year {year:2d}: ${balance:.2f}")
