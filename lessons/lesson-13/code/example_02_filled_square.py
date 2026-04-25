# example_02_filled_square.py
# Lesson 13: Drawing a filled square
# Use begin_fill() before drawing and end_fill() after.

import turtle

turtle.speed(3)

# Set colors
turtle.pencolor("black")      # outline color
turtle.fillcolor("yellow")    # fill color
turtle.pensize(3)             # thicker outline

# Start filling
turtle.begin_fill()

# Draw the square
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# Stop filling — the shape gets filled!
turtle.end_fill()

# Draw another filled square in a different position
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

turtle.pencolor("purple")
turtle.fillcolor("cyan")
turtle.begin_fill()
for i in range(4):
    turtle.forward(80)
    turtle.right(90)
turtle.end_fill()

turtle.done()
