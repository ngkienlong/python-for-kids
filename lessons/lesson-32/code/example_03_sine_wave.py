# example_03_sine_wave.py
# Lesson 32: Draw a sine wave using turtle and math.sin()
# sin() takes radians, so we convert degrees to radians: x * pi / 180

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Sine Wave")

t = turtle.Turtle()
t.speed(0)   # fastest speed

# Draw x-axis
t.pencolor("gray")
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)

# Draw y-axis
t.penup()
t.goto(0, -150)
t.pendown()
t.goto(0, 150)

# Draw sine wave (red)
t.pencolor("red")
t.pensize(2)
t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    # Convert x (degrees) to radians, then calculate y
    y = 100 * math.sin(x * math.pi / 180)
    t.goto(x, y)

# Draw cosine wave (blue) for comparison
t.pencolor("cyan")
t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    y = 100 * math.cos(x * math.pi / 180)
    t.goto(x, y)

# Labels
t.penup()
t.goto(-280, 110)
t.pencolor("red")
t.write("sin(x)", font=("Arial", 12, "normal"))
t.goto(-280, 90)
t.pencolor("cyan")
t.write("cos(x)", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()
