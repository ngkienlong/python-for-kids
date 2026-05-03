# example_05_goto.py
# Lesson 12: Using goto(x, y) to draw a cross (+)
# goto() jumps the turtle to any coordinate on the screen.

import turtle

turtle.speed(3)

# Draw a cross (+) centered at the origin
# Horizontal bar: from (-100, 0) to (100, 0)
turtle.penup()
turtle.goto(-100, 0)    # move to left end of horizontal bar
turtle.pendown()
turtle.goto(100, 0)     # draw to right end

# Vertical bar: from (0, -100) to (0, 100)
turtle.penup()
turtle.goto(0, -100)    # move to bottom of vertical bar
turtle.pendown()
turtle.goto(0, 100)     # draw to top

# Draw a small square at each end of the cross
positions = [(-100, 0), (100, 0), (0, -100), (0, 100)]
for pos in positions:
    turtle.penup()
    turtle.goto(pos[0] - 10, pos[1] - 10)
    turtle.pendown()
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)

turtle.done()
