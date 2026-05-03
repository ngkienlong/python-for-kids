"""
Lesson 17 - Example 05: Abstract Art
Creates abstract art using rotating colored squares
"""
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.title("Abstract Art")
turtle.bgcolor("black")

# --- Configuration ---
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]
num_squares = 40            # total number of squares
side_length = 120           # side length of each square
rotation_step = 9           # degrees to rotate between squares

# --- Draw rotating colored squares ---
for i in range(num_squares):
    color = colors[i % len(colors)]

    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()

    # Draw one square
    for j in range(4):
        turtle.forward(side_length)
        turtle.left(90)

    turtle.end_fill()

    # Rotate for the next square
    turtle.right(rotation_step)

# --- Add a center decoration ---
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(20, "white")

turtle.update()
turtle.hideturtle()
turtle.done()
