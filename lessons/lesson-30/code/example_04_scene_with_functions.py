# example_04_scene_with_functions.py
# Lesson 30: Draw a complete scene using functions
# Functions: draw_house, draw_tree, draw_sun, draw_ground

import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Scene")

t = turtle.Turtle()
t.speed(8)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_ground():
    """Draw a green ground line."""
    t.pencolor("green")
    t.pensize(3)
    move_to(-300, -100)
    t.forward(600)
    t.pensize(1)

def draw_sun(x, y, radius):
    """Draw a yellow sun at (x, y)."""
    t.fillcolor("yellow")
    t.pencolor("orange")
    move_to(x, y - radius)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    # Draw rays
    t.pencolor("orange")
    for i in range(8):
        move_to(x, y)
        t.setheading(i * 45)
        t.forward(radius + 20)
    t.setheading(0)

def draw_house(x, y, size):
    """Draw a simple house at (x, y) with given size."""
    # Body (square)
    t.fillcolor("lightyellow")
    t.pencolor("brown")
    move_to(x, y)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    # Roof (triangle)
    t.fillcolor("red")
    move_to(x, y)
    t.begin_fill()
    t.setheading(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.end_fill()
    t.setheading(0)
    # Door
    t.fillcolor("brown")
    move_to(x + size // 3, y - size)
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.forward(size // 5)
        else:
            t.forward(size // 3)
        t.right(90)
    t.end_fill()

def draw_tree(x, y, height):
    """Draw a simple tree at (x, y) with given height."""
    # Green triangle top
    t.fillcolor("darkgreen")
    move_to(x, y)
    t.begin_fill()
    t.setheading(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.end_fill()
    t.setheading(0)
    # Brown trunk
    trunk_w = height // 5
    trunk_h = height // 3
    t.fillcolor("saddlebrown")
    move_to(x + height // 2 - trunk_w // 2, y)
    t.begin_fill()
    t.forward(trunk_w)
    t.right(90)
    t.forward(trunk_h)
    t.right(90)
    t.forward(trunk_w)
    t.right(90)
    t.forward(trunk_h)
    t.end_fill()
    t.setheading(0)

# --- Draw the scene ---
draw_ground()
draw_sun(200, 150, 40)
draw_house(-100, -100, 100)
draw_house(80, -100, 80)
draw_tree(-220, -100, 80)
draw_tree(220, -100, 70)
draw_tree(-30, -100, 60)

t.hideturtle()
turtle.done()
