# example_04_recursive_factorial.py
# Lesson 31: Introduction to recursion with factorial
# Recursion = a function that calls itself

# --- Iterative version (using a loop) ---
def factorial_loop(n):
    """Calculate n! using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# --- Recursive version ---
def factorial_recursive(n):
    """Calculate n! using recursion.
    
    Base case: factorial(0) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    """
    if n == 0:          # BASE CASE: stop here!
        return 1
    return n * factorial_recursive(n - 1)   # RECURSIVE CALL

# Compare both versions
print("Comparing loop vs recursive:")
print("n  | loop | recursive")
print("-" * 25)
for n in range(8):
    loop_result = factorial_loop(n)
    rec_result = factorial_recursive(n)
    print(n, " |", loop_result, "|", rec_result)

print()

# Show how recursion works step by step
print("How factorial(4) works:")
print("factorial(4)")
print("= 4 * factorial(3)")
print("= 4 * 3 * factorial(2)")
print("= 4 * 3 * 2 * factorial(1)")
print("= 4 * 3 * 2 * 1 * factorial(0)")
print("= 4 * 3 * 2 * 1 * 1")
print("=", factorial_recursive(4))
