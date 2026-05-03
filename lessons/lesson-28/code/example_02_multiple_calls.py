# example_02_multiple_calls.py
# Lesson 28: Call a function multiple times
# This shows the power of functions — write once, use many times!

def print_separator():
    print("=" * 30)

def print_title():
    print("   MY PYTHON NOTEBOOK")

def print_date():
    print("   Date: 2025-01-01")

# Build a formatted page using functions
print_separator()
print_title()
print_separator()
print_date()
print_separator()

print()

# Another example: print a receipt
def print_receipt_line():
    print("-" * 20)

print_receipt_line()
print("Item 1: Apple    $1.00")
print("Item 2: Banana   $0.50")
print("Item 3: Milk     $2.00")
print_receipt_line()
print("Total:           $3.50")
print_receipt_line()

print()

# Count how many times we called print_separator
# (We called it 3 times above — imagine if we had to change it!)
# With a function, we only need to change ONE place.
