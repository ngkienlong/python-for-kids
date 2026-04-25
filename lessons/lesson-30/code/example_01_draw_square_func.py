# example_01_draw_square_func.py
# Lesson 30: Draw squares using a function with a size parameter

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Draw Square Function")

t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_square(size):
    """Draw a square with the given side length."""
    for i in range(4):
        t.forward(size)
        t.right(90)

# Draw squares of different sizes at different positions
t.pencolor("blue")
move_to(-200, 0)
draw_square(50)

t.pencolor("red")
move_to(-80, 0)
draw_square(80)

t.pencolor("green")
move_to(60, 0)
draw_square(110)

t.pencolor("purple")
move_to(220, 0)
draw_square(60)

t.hideturtle()
turtle.done()
