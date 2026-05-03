# example_01_square_spiral.py
# Lesson 15: Drawing a square spiral
# Each side is longer than the previous — the spiral grows outward.

import turtle

turtle.speed(0)   # instant drawing

distance = 5      # starting side length
for i in range(50):
    turtle.forward(distance)
    turtle.right(90)          # turn 90 degrees (square corner)
    distance = distance + 3   # grow by 3 pixels each step

turtle.done()
