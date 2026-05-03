"""
Lesson 18 - Example 04: Large Numbers
Python handles very large numbers exactly — no overflow!
"""

# Python can compute huge powers exactly
print("--- Large Powers ---")
print(f"2^10  = {2 ** 10}")
print(f"2^20  = {2 ** 20}")
print(f"2^30  = {2 ** 30}")
print(f"2^64  = {2 ** 64}")
print(f"2^100 = {2 ** 100}")

# Computer memory sizes (powers of 2)
print("\n--- Computer Memory Sizes ---")
print(f"1 KB = 2^10 = {2 ** 10} bytes")
print(f"1 MB = 2^20 = {2 ** 20} bytes")
print(f"1 GB = 2^30 = {2 ** 30} bytes")
print(f"1 TB = 2^40 = {2 ** 40} bytes")

# Scientific notation in Python
print("\n--- Scientific Notation ---")
a = 1e6         # 1 × 10^6
b = 2.5e3       # 2.5 × 10^3
c = 1e-4        # 1 × 10^-4
print(f"1e6   = {a}")
print(f"2.5e3 = {b}")
print(f"1e-4  = {c}")

# Powers of 2 table (0 to 10)
print("\n--- Powers of 2 Table ---")
for i in range(11):
    print(f"2^{i:2d} = {2 ** i}")
