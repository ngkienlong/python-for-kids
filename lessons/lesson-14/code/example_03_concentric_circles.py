# example_03_concentric_circles.py
# Lesson 14: Drawing concentric circles (same center, different sizes)
# Move to (0, -r) before drawing each circle so they share the same center.

import turtle

turtle.speed(3)

# Draw 5 concentric circles
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    r = (i + 1) * 30       # radii: 30, 60, 90, 120, 150
    turtle.penup()
    turtle.goto(0, -r)     # position so circle is centered at origin
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.pensize(2)
    turtle.circle(r)

turtle.done()
