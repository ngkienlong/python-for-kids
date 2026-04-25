# example_04_penup_pendown.py
# Lesson 12: Using penup() and pendown() to draw separate shapes
# penup() = lift the pen (move without drawing)
# pendown() = put the pen down (draw when moving)

import turtle

turtle.speed(3)

# Draw first line
turtle.forward(100)

# Lift pen and move to a new position
turtle.penup()
turtle.forward(50)      # move 50 pixels without drawing

# Put pen down and draw second line
turtle.pendown()
turtle.forward(100)

# Lift pen, move to a completely different spot
turtle.penup()
turtle.goto(-100, -80)  # jump to coordinates (-100, -80)

# Draw a square at the new position
turtle.pendown()
for i in range(4):
    turtle.forward(60)
    turtle.right(90)

turtle.done()
