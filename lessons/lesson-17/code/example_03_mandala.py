"""
Lesson 17 - Example 03: Simple Mandala
Draws a mandala by rotating colored shapes around the center
"""
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.title("Mandala")
turtle.bgcolor("black")

# --- Configuration ---
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
num_petals = 12             # number of petals
petal_radius = 50           # radius of each petal circle

# --- Draw the mandala ---
# Each petal is a circle; we rotate before drawing the next one
for i in range(num_petals):
    color = colors[i % len(colors)]

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    # Draw one petal (a full circle offset from center)
    turtle.circle(petal_radius)

    turtle.end_fill()

    # Rotate to position for the next petal
    turtle.right(360 / num_petals)

# --- Draw center dot ---
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(20, "white")

turtle.update()
turtle.hideturtle()
turtle.done()
