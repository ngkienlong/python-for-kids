# example_02_pythagorean_art.py
# Lesson 32: Draw right triangles from Pythagorean triples
# Pythagorean triple: a² + b² = c²
# Famous triples: (3,4,5), (5,12,13), (8,15,17)

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pythagorean Art")

t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    """Move turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_right_triangle(x, y, a, b, color):
    """Draw a right triangle with legs a and b at position (x, y)."""
    c = math.sqrt(a * a + b * b)
    t.pencolor(color)
    move_to(x, y)
    t.setheading(0)
    t.forward(a)          # draw leg a (horizontal)
    t.left(90)
    t.forward(b)          # draw leg b (vertical)
    t.goto(x, y)          # draw hypotenuse back to start
    t.setheading(0)

# Pythagorean triples (scaled by 10)
triples = [
    (3, 4, 5),    # classic 3-4-5
    (5, 12, 13),  # 5-12-13
    (8, 15, 17),  # 8-15-17
]

colors = ["red", "blue", "green"]
scale = 10

x = -250
for i, (a, b, c) in enumerate(triples):
    # Verify it's a Pythagorean triple
    hyp = math.sqrt(a*a + b*b)
    print(f"Triple ({a},{b},{c}): hypotenuse = {hyp:.1f} ✓" if abs(hyp - c) < 0.001 else "Not a triple!")
    draw_right_triangle(x, -50, a * scale, b * scale, colors[i])
    x += a * scale + 30

t.hideturtle()
turtle.done()
