# example_04_colorful_shapes.py
# Lesson 13: Drawing multiple colorful shapes

import turtle

turtle.speed(0)   # instant drawing

# Set background color
turtle.bgcolor("lightyellow")

# Draw a filled red triangle
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.pencolor("darkred")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.end_fill()

# Draw a filled green pentagon
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.pencolor("darkgreen")
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(5):
    turtle.forward(80)
    turtle.right(72)
turtle.end_fill()

# Draw a filled blue circle
turtle.penup()
turtle.goto(120, -50)
turtle.pendown()
turtle.pencolor("darkblue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()
