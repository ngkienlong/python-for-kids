"""
Lesson 16 - Example 04: Drawing a Smiley Face
A face = circle head + dot eyes + arc smile
"""
import turtle

turtle.speed(2)
turtle.title("Smiley Face")

# --- Draw the head (yellow circle) ---
turtle.penup()
turtle.goto(0, -60)         # goto() starts circle from bottom
turtle.pendown()

turtle.fillcolor("lightyellow")
turtle.pencolor("black")
turtle.pensize(2)
turtle.begin_fill()
turtle.circle(60)           # radius = 60
turtle.end_fill()

# --- Draw the left eye (black dot) ---
turtle.penup()
turtle.goto(-22, 20)
turtle.pendown()
turtle.dot(14, "black")     # dot(size, color)

# --- Draw the right eye (black dot) ---
turtle.penup()
turtle.goto(22, 20)
turtle.pendown()
turtle.dot(14, "black")

# --- Draw the smile (arc) ---
# setheading(-60) points the turtle down-right
# circle(25, 120) draws a 120-degree arc
turtle.penup()
turtle.goto(-22, -10)
turtle.pendown()
turtle.pensize(3)
turtle.setheading(-60)
turtle.circle(25, 120)      # arc: radius=25, extent=120 degrees

turtle.hideturtle()
turtle.done()
