# example_02_draw_polygon_func.py
# Lesson 30: Draw any regular polygon with a function
# A regular polygon has equal sides and equal angles

import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Regular Polygons")

t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_polygon(sides, size):
    """Draw a regular polygon with the given number of sides and size."""
    angle = 360 / sides   # exterior angle
    for i in range(sides):
        t.forward(size)
        t.right(angle)

# Draw different polygons in a row
colors = ["red", "blue", "green", "orange", "purple", "brown"]
polygon_names = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon"]

x = -250
for sides in range(3, 9):
    t.pencolor(colors[sides - 3])
    move_to(x, 0)
    draw_polygon(sides, 50)
    # Label the shape
    t.penup()
    t.goto(x, -80)
    t.write(polygon_names[sides - 3], align="left", font=("Arial", 8, "normal"))
    t.pendown()
    x += 100

t.hideturtle()
turtle.done()
