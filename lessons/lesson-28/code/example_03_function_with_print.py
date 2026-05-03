# example_03_function_with_print.py
# Lesson 28: Functions that print useful information

def print_times_table_2():
    """Print the 2x multiplication table."""
    print("=== 2x Table ===")
    for i in range(1, 11):
        print("2 x", i, "=", 2 * i)

def print_times_table_3():
    """Print the 3x multiplication table."""
    print("=== 3x Table ===")
    for i in range(1, 11):
        print("3 x", i, "=", 3 * i)

def print_fibonacci():
    """Print the first 8 Fibonacci numbers."""
    print("=== Fibonacci ===")
    a = 0
    b = 1
    for i in range(8):
        print(a)
        a, b = b, a + b

# Call each function
print_times_table_2()
print()
print_times_table_3()
print()
print_fibonacci()
