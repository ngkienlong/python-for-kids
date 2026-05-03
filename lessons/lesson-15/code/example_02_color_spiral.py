# example_02_color_spiral.py
# Lesson 15: Color-cycling spiral
# Use i % len(colors) to cycle through a list of colors.

import turtle

turtle.speed(0)
turtle.tracer(0)   # skip animation for speed

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = 5

for i in range(60):
    turtle.pencolor(colors[i % len(colors)])   # cycle: 0,1,2,3,4,5,0,1,2,...
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 4

turtle.update()   # show the final drawing
turtle.done()
