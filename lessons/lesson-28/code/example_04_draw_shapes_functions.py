# example_04_draw_shapes_functions.py
# Lesson 28: Draw shapes using turtle with functions
# Each shape is its own function — clean and reusable!

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Shapes with Functions")

t = turtle.Turtle()
t.speed(5)

# --- Define drawing functions ---

def draw_square():
    """Draw a square with side length 80."""
    for i in range(4):
        t.forward(80)
        t.right(90)

def draw_triangle():
    """Draw an equilateral triangle with side length 80."""
    for i in range(3):
        t.forward(80)
        t.right(120)

def move_to(x, y):
    """Move the turtle to position (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Draw shapes by calling functions ---

# Draw a square on the left
t.pencolor("blue")
move_to(-200, 0)
draw_square()

# Draw a triangle in the middle
t.pencolor("red")
move_to(0, 0)
draw_triangle()

# Draw another square on the right
t.pencolor("green")
move_to(150, 0)
draw_square()

# Draw a triangle at the top
t.pencolor("purple")
move_to(-50, 150)
draw_triangle()

t.hideturtle()
turtle.done()
