# example_01_pencolor.py
# Lesson 13: Using pencolor() to draw colored lines

import turtle

turtle.speed(3)

# Draw lines in different colors
turtle.pencolor("red")
turtle.forward(100)
turtle.right(90)

turtle.pencolor("blue")
turtle.forward(100)
turtle.right(90)

turtle.pencolor("green")
turtle.forward(100)
turtle.right(90)

turtle.pencolor("orange")
turtle.forward(100)
turtle.right(90)

# Draw a colorful star outline
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    turtle.pencolor(colors[i])
    turtle.forward(80)
    turtle.right(144)   # exterior angle of a 5-pointed star

turtle.done()
