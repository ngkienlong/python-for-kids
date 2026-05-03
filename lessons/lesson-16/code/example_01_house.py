"""
Lesson 16 - Example 01: Drawing a Simple House
A house = square body + triangle roof
"""
import turtle

turtle.speed(3)
turtle.title("Simple House")

# --- Draw the square body ---
turtle.penup()
turtle.goto(-50, -80)       # move to bottom-left corner of house
turtle.pendown()

turtle.fillcolor("lightyellow")
turtle.pencolor("black")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)     # each side is 100 pixels
    turtle.left(90)
turtle.end_fill()

# --- Draw the triangle roof ---
turtle.penup()
turtle.goto(-50, 20)        # bottom-left corner of roof
turtle.pendown()

turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(50, 20)         # bottom-right corner of roof
turtle.goto(0, 80)          # peak of the roof
turtle.goto(-50, 20)        # back to start
turtle.end_fill()

# --- Draw the door ---
turtle.penup()
turtle.goto(-12, -80)       # bottom-left of door
turtle.pendown()

turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(24)      # door width
    turtle.left(90)
    turtle.forward(35)      # door height
    turtle.left(90)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
