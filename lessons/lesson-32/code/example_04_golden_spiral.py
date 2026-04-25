# example_04_golden_spiral.py
# Lesson 32: Approximate the golden spiral using Fibonacci squares
# The golden spiral passes through the corners of Fibonacci squares

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Golden Spiral")

t = turtle.Turtle()
t.speed(8)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# Generate Fibonacci numbers
fib = []
a, b = 1, 1
for i in range(9):
    fib.append(a)
    a, b = b, a + b

scale = 8

# Draw Fibonacci squares in a spiral arrangement
# Direction: right, up, left, down, right, ...
x, y = 0, 0
direction = 0   # 0=right, 1=up, 2=left, 3=down

square_positions = []

for f in fib:
    size = f * scale
    # Draw the square
    t.pencolor("lightgray")
    move_to(x, y)
    t.setheading(direction * 90)
    for i in range(4):
        t.forward(size)
        t.right(90)
    square_positions.append((x, y, size, direction))
    # Move to next position
    if direction == 0:
        x += size
    elif direction == 1:
        y += size
    elif direction == 2:
        x -= size
    else:
        y -= size
    direction = (direction + 1) % 4

# Draw the spiral arcs (quarter circles inside each square)
t.pencolor("blue")
t.pensize(2)

for sx, sy, size, d in square_positions:
    # Find the arc center (corner of the square)
    if d == 0:
        arc_x, arc_y = sx, sy
        start_heading = 90
    elif d == 1:
        arc_x, arc_y = sx + size, sy
        start_heading = 180
    elif d == 2:
        arc_x, arc_y = sx + size, sy + size
        start_heading = 270
    else:
        arc_x, arc_y = sx, sy + size
        start_heading = 0

    move_to(arc_x, arc_y - size if d == 0 else arc_x)
    t.penup()
    t.goto(arc_x + size * math.cos((start_heading) * math.pi / 180),
           arc_y + size * math.sin((start_heading) * math.pi / 180))
    t.setheading(start_heading + 90)
    t.pendown()
    t.circle(size, 90)

t.hideturtle()
turtle.done()
