# example_01_fibonacci_squares.py
# Lesson 32: Draw squares with Fibonacci side lengths
# Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, ...

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fibonacci Squares")

t = turtle.Turtle()
t.speed(8)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_square(size, color):
    """Draw a square with given size and color."""
    t.pencolor(color)
    for i in range(4):
        t.forward(size)
        t.right(90)

# Generate first 8 Fibonacci numbers
fib = []
a, b = 1, 1
for i in range(8):
    fib.append(a)
    a, b = b, a + b

print("Fibonacci numbers:", fib)

# Draw squares in a row (scaled by 8)
scale = 8
colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "pink"]
x = -250

for i in range(len(fib)):
    size = fib[i] * scale
    move_to(x, -50)
    draw_square(size, colors[i])
    x += size + 5

t.hideturtle()
turtle.done()
