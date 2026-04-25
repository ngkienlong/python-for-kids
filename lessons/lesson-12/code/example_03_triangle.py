# example_03_triangle.py
# Lesson 12: Draw an equilateral triangle
# An equilateral triangle has 3 equal sides.
# The exterior angle is 360 / 3 = 120 degrees.

import turtle

turtle.speed(3)

# Draw an equilateral triangle
for i in range(3):
    turtle.forward(100)   # draw one side
    turtle.right(120)     # turn 120 degrees (exterior angle)

turtle.done()
