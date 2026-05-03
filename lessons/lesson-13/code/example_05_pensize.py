# example_05_pensize.py
# Lesson 13: Using pensize() to draw lines of different thickness

import turtle

turtle.speed(3)

# Draw lines with increasing thickness
y_start = 100
for size in range(1, 8):
    turtle.penup()
    turtle.goto(-150, y_start - size * 25)
    turtle.pendown()
    turtle.pensize(size)
    turtle.pencolor("blue")
    turtle.forward(300)

# Draw a thick outlined square
turtle.penup()
turtle.goto(-60, -60)
turtle.pendown()
turtle.pensize(8)
turtle.pencolor("red")
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(120)
    turtle.right(90)
turtle.end_fill()

turtle.done()
