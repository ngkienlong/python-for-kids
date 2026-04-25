# example_05_math_pattern.py
# Lesson 32: Draw a pattern based on the multiplication table
# For each (i, j), draw a shape if i*j meets a condition

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Multiplication Table Pattern")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw a dot at (x, y) with given color and size
def draw_dot(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.dot(size, color)

# Pattern 1: dot size based on i*j value
print("Drawing multiplication table pattern...")

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "white"]

for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        x = (i - 5) * 35
        y = (j - 5) * 35
        # Color based on product mod 9
        color_index = (product - 1) % 9
        # Size based on product
        size = 8 + (product % 5) * 3
        draw_dot(x, y, size, colors[color_index])

# Draw axes
t.pencolor("white")
t.pensize(1)
move_to(-160, 0)
t.goto(160, 0)
move_to(0, -160)
t.goto(0, 160)

turtle.done()
