"""
Lesson 17 - Example 02: Colorful Grid Art
Uses nested loops to draw a grid of colored squares
"""
import turtle

turtle.speed(0)
turtle.tracer(0)            # turn off animation for fast drawing
turtle.title("Grid Art")

# --- Configuration ---
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
size = 40                   # size of each square
cols = 8                    # number of columns
rows = 6                    # number of rows

# Calculate starting position to center the grid
start_x = -(cols * size) // 2
start_y = (rows * size) // 2

# --- Draw the grid ---
for row in range(rows):
    for col in range(cols):
        # Calculate position of this square
        x = start_x + col * size
        y = start_y - row * size

        # Pick color based on position (creates a diagonal pattern)
        color = colors[(row + col) % len(colors)]

        # Move to position and draw filled square
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.fillcolor(color)
        turtle.pencolor("white")    # white border between squares
        turtle.pensize(1)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()

turtle.update()             # show the finished drawing
turtle.hideturtle()
turtle.done()
