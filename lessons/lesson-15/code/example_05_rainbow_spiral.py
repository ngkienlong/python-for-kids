# example_05_rainbow_spiral.py
# Lesson 15: Rainbow spiral combining color cycling, growth, and rotation
# This creates a beautiful rainbow pattern.

import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("black")

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
distance = 2

for i in range(100):
    turtle.pencolor(colors[i % len(colors)])
    turtle.pensize(2)
    turtle.forward(distance)
    turtle.right(59)          # 59 degrees creates an interesting spiral
    distance = distance + 1.5

turtle.update()
turtle.done()
