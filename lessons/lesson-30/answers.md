# Lesson 30: Answers 🐢

---

## 🟢 Easy

**E1.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-150, 0)
draw_square(50)
move_to(0, 0)
draw_square(80)
move_to(150, 0)
draw_square(110)

turtle.done()
```

**E2.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_colored_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-100, 0)
draw_colored_square(70, "red")
move_to(50, 0)
draw_colored_square(70, "blue")

turtle.done()
```

**E3.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_triangle(size):
    for i in range(3):
        t.forward(size)
        t.right(120)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-150, 0)
draw_triangle(60)
move_to(0, 0)
draw_triangle(90)
move_to(150, 0)
draw_triangle(120)

turtle.done()
```

**E4.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_polygon(sides, size):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-200, 0)
draw_polygon(3, 60)
move_to(-60, 0)
draw_polygon(4, 60)
move_to(80, 0)
draw_polygon(5, 60)
move_to(220, 0)
draw_polygon(6, 60)

turtle.done()
```

**E5.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

move_to(-150, 0)
draw_square(60)
move_to(0, 0)
draw_square(60)
move_to(150, 0)
draw_square(60)

turtle.done()
```

**E6.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_circle(radius, color):
    t.pencolor(color)
    t.circle(radius)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-150, 0)
draw_circle(40, "red")
move_to(0, 0)
draw_circle(60, "blue")
move_to(150, 0)
draw_circle(80, "green")

turtle.done()
```

**E7.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-80, 0)
draw_star(60)
move_to(80, 0)
draw_star(80)

turtle.done()
```

---

## 🟡 Medium

**M1.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

colors = ["red", "orange", "yellow", "green", "blue"]
x = -200
for color in colors:
    move_to(x, 0)
    draw_square(60, color)
    x += 90

turtle.done()
```

**M2.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

for i in range(5):
    size = 40 + i * 20
    move_to(-size // 2, -size // 2)
    draw_square(size)

turtle.done()
```

**M3.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_polygon(sides, size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-200, 0)
draw_polygon(3, 60, "red")
move_to(-60, 0)
draw_polygon(4, 60, "blue")
move_to(80, 0)
draw_polygon(5, 60, "green")
move_to(220, 0)
draw_polygon(6, 60, "yellow")

turtle.done()
```

**M4.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_house(x, y, size):
    # Draw the square body
    move_to(x, y)
    for i in range(4):
        t.forward(size)
        t.right(90)
    # Draw the triangle roof
    move_to(x, y)
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.setheading(0)

draw_house(-100, -50, 80)
draw_house(50, -50, 80)

turtle.done()
```

**M5.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_tree(x, y, height):
    # Draw triangle top (green)
    t.fillcolor("green")
    t.begin_fill()
    move_to(x, y)
    t.left(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.end_fill()
    t.setheading(0)
    # Draw trunk (brown)
    t.fillcolor("brown")
    t.begin_fill()
    trunk_w = height // 5
    move_to(x + height // 2 - trunk_w // 2, y)
    for i in range(4):
        if i % 2 == 0:
            t.forward(trunk_w)
        else:
            t.forward(height // 4)
        t.right(90)
    t.end_fill()

draw_tree(-150, -50, 60)
draw_tree(0, -50, 80)
draw_tree(150, -50, 100)

turtle.done()
```

**M6.**
```python
import turtle
t = turtle.Turtle()
t.speed(10)

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

for i in range(10):
    draw_square(100)
    t.right(36)

turtle.done()
```

**M7.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_face(x, y, size):
    # Face circle
    move_to(x, y - size)
    t.circle(size)
    # Left eye
    move_to(x - size // 3, y + size // 3)
    t.dot(size // 8)
    # Right eye
    move_to(x + size // 3, y + size // 3)
    t.dot(size // 8)
    # Smile
    move_to(x - size // 3, y - size // 5)
    t.setheading(-60)
    t.circle(size // 2, 120)
    t.setheading(0)

draw_face(-100, 0, 50)
draw_face(100, 0, 50)

turtle.done()
```

---

## 🔴 Hard

**H1.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

sizes = [40, 60, 80, 100, 120]
colors = ["red", "orange", "yellow", "green", "blue"]
x = -200

for i in range(5):
    move_to(x, 0)
    draw_square(sizes[i], colors[i])
    x += sizes[i] + 20

turtle.done()
```

**H2.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_regular_polygon(n, size):
    angle = 360 / n
    for i in range(n):
        t.forward(size)
        t.right(angle)

x = -200
for sides in [3, 4, 5, 6]:
    move_to(x, 0)
    draw_regular_polygon(sides, 60)
    x += 130

turtle.done()
```

**H3.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_star(size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

move_to(-150, 0)
draw_star(40, "red")
move_to(0, 0)
draw_star(70, "gold")
move_to(150, 0)
draw_star(100, "blue")

turtle.done()
```

**H4.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_house(x, y, size):
    # Square body
    move_to(x, y)
    for i in range(4):
        t.forward(size)
        t.right(90)
    # Triangle roof
    move_to(x, y)
    t.setheading(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.setheading(0)

draw_house(-200, -50, 80)
draw_house(-50, -50, 80)
draw_house(100, -50, 80)

turtle.done()
```

**H5.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_tree(x, y, height):
    # Green triangle top
    t.fillcolor("green")
    t.begin_fill()
    move_to(x, y)
    t.setheading(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.end_fill()
    t.setheading(0)
    # Brown trunk
    trunk_w = max(8, height // 6)
    trunk_h = height // 4
    t.fillcolor("brown")
    t.begin_fill()
    move_to(x + height // 2 - trunk_w // 2, y)
    t.forward(trunk_w)
    t.right(90)
    t.forward(trunk_h)
    t.right(90)
    t.forward(trunk_w)
    t.right(90)
    t.forward(trunk_h)
    t.end_fill()
    t.setheading(0)

heights = [60, 80, 100, 120]
x = -180
for h in heights:
    draw_tree(x, -80, h)
    x += 110

turtle.done()
```

**H6.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_face(x, y, size):
    # Face outline
    t.pencolor("black")
    move_to(x, y - size)
    t.circle(size)
    # Eyes
    move_to(x - size // 3, y + size // 3)
    t.dot(max(4, size // 8))
    move_to(x + size // 3, y + size // 3)
    t.dot(max(4, size // 8))
    # Smile
    move_to(x - size // 3, y - size // 5)
    t.setheading(-60)
    t.circle(size // 2, 120)
    t.setheading(0)

draw_face(-120, 0, 40)
draw_face(0, 0, 60)
draw_face(140, 0, 80)

turtle.done()
```

**H7.**
```python
import turtle
t = turtle.Turtle()
t.speed(10)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_flower(x, y, petals, color):
    """Draw a flower with the given number of petals."""
    t.fillcolor(color)
    move_to(x, y)
    petal_angle = 360 / petals
    for i in range(petals):
        t.begin_fill()
        t.circle(20, 60)
        t.left(120)
        t.circle(20, 60)
        t.left(120)
        t.end_fill()
        t.right(petal_angle)
    # Draw center
    move_to(x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

flowers = [
    (-200, 0, 5, "red"),
    (-100, 0, 6, "pink"),
    (0, 0, 8, "purple"),
    (100, 0, 4, "orange"),
    (200, 0, 7, "blue"),
]

for fx, fy, petals, color in flowers:
    draw_flower(fx, fy, petals, color)

t.hideturtle()
turtle.done()
```
