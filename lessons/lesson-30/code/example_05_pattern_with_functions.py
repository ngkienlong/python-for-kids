# example_05_pattern_with_functions.py
# Lesson 30: Draw a flower pattern using a draw_petal function

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flower Pattern")

t = turtle.Turtle()
t.speed(10)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_petal(size, color):
    """Draw one petal using two arcs."""
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.end_fill()

def draw_flower(x, y, petals, petal_size, color):
    """Draw a flower with the given number of petals."""
    move_to(x, y)
    angle = 360 / petals
    for i in range(petals):
        draw_petal(petal_size, color)
        t.right(angle)
    # Draw center
    move_to(x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(petal_size // 3)
    t.end_fill()

# Draw a single large flower in the center
draw_flower(0, 0, 8, 40, "pink")

# Draw smaller flowers around it
positions = [(-180, 80), (180, 80), (-180, -80), (180, -80), (0, 160)]
colors = ["red", "orange", "purple", "blue", "cyan"]

for i in range(5):
    x, y = positions[i]
    draw_flower(x, y, 6, 25, colors[i])

t.hideturtle()
turtle.done()
