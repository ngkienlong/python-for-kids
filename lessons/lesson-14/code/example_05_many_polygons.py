# example_05_many_polygons.py
# Lesson 14: Draw triangle, square, pentagon, hexagon in a row

import turtle

turtle.speed(0)

# List of shapes: (number of sides, x position)
shapes = [
    (3, -200),   # triangle at x=-200
    (4, -80),    # square at x=-80
    (5, 50),     # pentagon at x=50
    (6, 180),    # hexagon at x=180
]

colors = ["red", "blue", "green", "orange"]

for idx in range(len(shapes)):
    n, x = shapes[idx]
    turtle.penup()
    turtle.goto(x, 0)
    turtle.setheading(0)    # always face right before drawing
    turtle.pendown()
    turtle.pencolor(colors[idx])
    for i in range(n):
        turtle.forward(60)
        turtle.right(360 / n)

turtle.done()
