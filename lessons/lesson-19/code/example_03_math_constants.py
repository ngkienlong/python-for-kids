"""
Lesson 19 - Example 03: Math Constants
math.pi, math.e, and other constants
"""
import math

# Pi (π) — ratio of circumference to diameter
print("--- Pi ---")
print(f"math.pi = {math.pi}")
print(f"Rounded to 5 places: {round(math.pi, 5)}")

# Euler's number (e) — base of natural logarithm
print("\n--- Euler's Number (e) ---")
print(f"math.e = {math.e}")
print(f"Rounded to 5 places: {round(math.e, 5)}")

# Tau (τ = 2π)
print("\n--- Tau (2π) ---")
print(f"math.tau = {math.tau}")
print(f"math.tau == 2 * math.pi: {math.tau == 2 * math.pi}")

# Using pi for circle calculations
print("\n--- Circle Calculations ---")
radius = 7
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Radius: {radius}")
print(f"Area: {area:.4f}")
print(f"Circumference: {circumference:.4f}")

# Using e for exponential growth
print("\n--- Exponential Growth with e ---")
print(f"e^1 = {math.e ** 1:.4f}")
print(f"e^2 = {math.e ** 2:.4f}")
print(f"e^3 = {math.e ** 3:.4f}")
