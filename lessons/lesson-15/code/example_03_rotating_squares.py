# example_03_rotating_squares.py
# Lesson 15: Rotating squares pattern
# Draw many squares, each rotated a little more than the previous.

import turtle

turtle.speed(0)
turtle.tracer(0)

# Draw 36 squares, each rotated 10 degrees more
# 36 x 10 = 360 degrees = full rotation
for i in range(36):
    turtle.pencolor("blue")
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)   # rotate 10 degrees before next square

turtle.update()
turtle.done()
