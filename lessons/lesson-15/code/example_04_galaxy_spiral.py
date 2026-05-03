# example_04_galaxy_spiral.py
# Lesson 15: Galaxy spiral — smooth curve using a small turn angle
# A small turn angle (like 30 degrees) creates a smooth, galaxy-like spiral.

import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("black")

colors = ["white", "yellow", "cyan", "lightblue"]
distance = 1

for i in range(200):
    turtle.pencolor(colors[i % len(colors)])
    turtle.forward(distance)
    turtle.right(30)          # small angle = smooth curve
    distance = distance + 0.5

turtle.update()
turtle.done()
