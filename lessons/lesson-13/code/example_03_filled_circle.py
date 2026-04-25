# example_03_filled_circle.py
# Lesson 13: Drawing filled circles with turtle.circle()

import turtle

turtle.speed(3)

# Draw a filled orange circle
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(50)           # radius = 50 pixels
turtle.end_fill()

# Draw a filled blue circle
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.fillcolor("blue")
turtle.pencolor("blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Draw a small red circle on top
turtle.penup()
turtle.goto(50, 30)
turtle.pendown()
turtle.fillcolor("red")
turtle.pencolor("darkred")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.done()
