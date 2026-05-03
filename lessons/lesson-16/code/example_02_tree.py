"""
Lesson 16 - Example 02: Drawing a Tree
A tree = green triangle canopy + brown rectangle trunk
"""
import turtle

turtle.speed(3)
turtle.title("Tree")

# --- Draw the trunk (brown rectangle) ---
turtle.penup()
turtle.goto(-10, -80)       # bottom-left of trunk
turtle.pendown()

turtle.fillcolor("brown")
turtle.pencolor("black")
turtle.begin_fill()
# Draw rectangle: width=20, height=40
for i in range(2):
    turtle.forward(20)      # width
    turtle.left(90)
    turtle.forward(40)      # height
    turtle.left(90)
turtle.end_fill()

# --- Draw the canopy (green triangle) ---
turtle.fillcolor("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-40, -40)       # bottom-left of canopy
turtle.pendown()
turtle.goto(40, -40)        # bottom-right of canopy
turtle.goto(0, 40)          # top (peak)
turtle.goto(-40, -40)       # back to start
turtle.end_fill()

turtle.hideturtle()
turtle.done()
