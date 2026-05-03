"""
Lesson 23 - Example 04: Sequence Analysis
Detect whether a sequence is arithmetic, geometric, or neither.
Then extend it by 3 more terms.
"""

def detect_sequence(nums):
    """Return 'arithmetic', 'geometric', or 'neither'."""
    n = len(nums)
    if n < 2:
        return "too short"

    # Check arithmetic: all differences equal
    diffs = [nums[i+1] - nums[i] for i in range(n - 1)]
    if all(abs(d - diffs[0]) < 0.0001 for d in diffs):
        return "arithmetic"

    # Check geometric: all ratios equal (no zeros)
    if all(nums[i] != 0 for i in range(n - 1)):
        ratios = [nums[i+1] / nums[i] for i in range(n - 1)]
        if all(abs(r - ratios[0]) < 0.0001 for r in ratios):
            return "geometric"

    return "neither"

def extend_sequence(nums, seq_type, extra=3):
    """Extend the sequence by 'extra' more terms."""
    extended = list(nums)
    if seq_type == "arithmetic":
        d = nums[1] - nums[0]
        for i in range(extra):
            extended.append(extended[-1] + d)
    elif seq_type == "geometric":
        r = nums[1] / nums[0]
        for i in range(extra):
            extended.append(extended[-1] * r)
    return extended

# Test sequences
test_sequences = [
    [2, 5, 8, 11, 14],
    [3, 6, 12, 24, 48],
    [1, 2, 4, 7, 11],
    [100, 50, 25, 12.5, 6.25],
]

print("--- Sequence Analysis ---")
for seq in test_sequences:
    seq_type = detect_sequence(seq)
    extended = extend_sequence(seq, seq_type)
    print(f"Sequence: {seq}")
    print(f"Type: {seq_type}")
    if seq_type != "neither":
        print(f"Extended: {extended}")
    print()

# User input
print("--- Analyze Your Sequence ---")
parts = input("Enter 5 numbers: ").split()
nums = [float(x) for x in parts]
seq_type = detect_sequence(nums)
print(f"Type: {seq_type}")
if seq_type != "neither":
    extended = extend_sequence(nums, seq_type)
    print(f"Next 3 terms: {extended[5:]}")
