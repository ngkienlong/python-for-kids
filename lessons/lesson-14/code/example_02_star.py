# example_02_star.py
# Lesson 14: Drawing a 5-pointed star
# A star uses 144 degrees (not 72) because it skips every other vertex.
# 5 x 144 = 720 = 2 x 360 (the turtle makes 2 full rotations)

import turtle

turtle.speed(3)

# Draw a simple 5-pointed star
turtle.pencolor("gold")
turtle.pensize(3)
for i in range(5):
    turtle.forward(100)
    turtle.right(144)

# Draw a filled red star
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.pencolor("darkred")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(80)
    turtle.right(144)
turtle.end_fill()

turtle.done()
