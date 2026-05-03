# example_03_draw_colored_shape.py
# Lesson 30: Draw filled shapes with color parameters

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Colored Shapes")

t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_filled_circle(x, y, radius, color):
    """Draw a filled circle at position (x, y) with given radius and color."""
    t.fillcolor(color)
    t.pencolor("black")
    move_to(x, y - radius)   # start at bottom of circle
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_filled_square(x, y, size, color):
    """Draw a filled square at position (x, y) with given size and color."""
    t.fillcolor(color)
    t.pencolor("black")
    move_to(x, y)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_filled_triangle(x, y, size, color):
    """Draw a filled equilateral triangle at position (x, y)."""
    t.fillcolor(color)
    t.pencolor("black")
    move_to(x, y)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

# Draw a row of circles
draw_filled_circle(-200, 50, 30, "red")
draw_filled_circle(-100, 50, 40, "orange")
draw_filled_circle(0, 50, 50, "yellow")
draw_filled_circle(100, 50, 40, "green")
draw_filled_circle(200, 50, 30, "blue")

# Draw a row of squares
draw_filled_square(-200, -50, 50, "purple")
draw_filled_square(-80, -50, 60, "pink")
draw_filled_square(60, -50, 50, "cyan")

# Draw triangles
draw_filled_triangle(-150, -150, 70, "brown")
draw_filled_triangle(50, -150, 70, "teal")

t.hideturtle()
turtle.done()
