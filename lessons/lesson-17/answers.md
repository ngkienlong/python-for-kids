# Lesson 17: Answers 🖼️

---

## 🟢 Easy

**E1.**
```python
import turtle
turtle.title("My Canvas")
turtle.setup(600, 400)
turtle.bgcolor("lightyellow")
turtle.penup()
turtle.goto(0, -40)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()
```

**E2.**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
for i in range(6):
    x = -150 + i * 50
    turtle.penup()
    turtle.goto(x, -25)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
turtle.done()
```

**E3.**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue"]
turtle.speed(0)
for i in range(5):
    y = 100 - i * 60
    turtle.penup()
    turtle.goto(0, y - 25)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
turtle.done()
```

**E4.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
size = 40
for row in range(4):
    for col in range(4):
        x = -80 + col * size
        y = 80 - row * size
        color = "black" if (row + col) % 2 == 0 else "white"
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
turtle.update()
turtle.done()
```

**E5.**
```python
import turtle
turtle.bgcolor("darkblue")
positions = [
    (-200,150), (-100,180), (0,160), (100,140), (200,170),
    (-150,80), (-50,100), (50,90), (150,110), (250,80),
    (-220,30), (-80,50), (30,40), (130,20), (220,60)
]
for (x, y) in positions:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(6, "white")
turtle.done()
```

**E6.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(7):
    y = 140 - i * 40
    turtle.penup()
    turtle.goto(-200, y)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    for j in range(2):
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()
turtle.update()
turtle.done()
```

**E7.**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
for i in range(6):
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(80)
        turtle.left(90)
    turtle.end_fill()
    turtle.right(30)
turtle.done()
```

---

## 🟡 Medium

**M1.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
colors = ["red", "blue", "yellow", "green"]
size = 50
for row in range(4):
    for col in range(4):
        x = -100 + col * size
        y = 100 - row * size
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(colors[(row + col) % 4])
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
turtle.update()
turtle.done()
```

**M2.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
colors = ["red", "orange", "yellow", "green"]
for i in range(8):
    turtle.fillcolor(colors[i % 4])
    turtle.begin_fill()
    turtle.circle(30, 360)
    turtle.end_fill()
    turtle.right(45)
turtle.update()
turtle.done()
```

**M3.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("skyblue")
# Ground
turtle.penup()
turtle.goto(-400, -300)
turtle.pendown()
turtle.fillcolor("darkgreen")
turtle.begin_fill()
turtle.goto(400, -300)
turtle.goto(400, -150)
turtle.goto(-400, -150)
turtle.goto(-400, -300)
turtle.end_fill()
# Mountain
turtle.penup()
turtle.goto(-200, -150)
turtle.pendown()
turtle.fillcolor("gray")
turtle.begin_fill()
turtle.goto(0, 150)
turtle.goto(200, -150)
turtle.goto(-200, -150)
turtle.end_fill()
# Sun
turtle.penup()
turtle.goto(250, 80)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.update()
turtle.done()
```

**M4.**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
turtle.tracer(0)
for i in range(36):
    turtle.fillcolor(colors[i % 6])
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    turtle.right(10)
turtle.update()
turtle.done()
```

**M5.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("darkblue")
buildings = [
    (-200, 60, 200), (-120, 80, 160), (-30, 50, 220),
    (50, 70, 180), (140, 90, 140)
]
for (x, w, h) in buildings:
    turtle.penup()
    turtle.goto(x, -200)
    turtle.pendown()
    turtle.fillcolor("dimgray")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()
    # Windows
    for wy in range(3):
        for wx in range(3):
            turtle.penup()
            turtle.goto(x + 10 + wx * 18, -180 + wy * 50)
            turtle.pendown()
            turtle.dot(6, "yellow")
turtle.update()
turtle.done()
```

**M6.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
petal_colors = ["red", "orange", "pink", "purple", "blue"]
for idx in range(5):
    fx = -160 + idx * 80
    # Stem
    turtle.penup()
    turtle.goto(fx, -100)
    turtle.pendown()
    turtle.pencolor("darkgreen")
    turtle.pensize(2)
    turtle.goto(fx, 0)
    # Petals
    turtle.pensize(1)
    for p in range(6):
        turtle.penup()
        turtle.goto(fx, 0)
        turtle.setheading(p * 60)
        turtle.forward(20)
        turtle.pendown()
        turtle.fillcolor(petal_colors[idx])
        turtle.begin_fill()
        turtle.circle(12, 360)
        turtle.end_fill()
    # Center
    turtle.penup()
    turtle.goto(fx, 0)
    turtle.pendown()
    turtle.dot(14, "yellow")
turtle.update()
turtle.done()
```

**M7.**
```python
import turtle
turtle.speed(0)
turtle.tracer(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
for i in range(8):
    r = (i + 1) * 20
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.circle(r)
turtle.update()
turtle.done()
```

---

## 🔴 Hard

**H1. Clock Face**

Use `math` to calculate positions of hour marks and numbers.

```python
import turtle
import math

turtle.speed(0)
turtle.tracer(0)

# Clock face
turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
turtle.fillcolor("white")
turtle.pencolor("black")
turtle.pensize(3)
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

# 12 hour marks
for i in range(12):
    angle = math.radians(90 - i * 30)
    x1 = 100 * math.cos(angle)
    y1 = 100 * math.sin(angle)
    x2 = 115 * math.cos(angle)
    y2 = 115 * math.sin(angle)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pensize(3)
    turtle.goto(x2, y2)

# Numbers 12, 3, 6, 9
numbers = {12: (0, 125), 3: (125, 0), 6: (0, -140), 9: (-140, 0)}
turtle.pencolor("black")
for num, (nx, ny) in numbers.items():
    turtle.penup()
    turtle.goto(nx, ny)
    turtle.pendown()
    turtle.write(str(num), align="center", font=("Arial", 14, "bold"))

# Center dot
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(10, "black")

turtle.update()
turtle.done()
```

**H2. Chessboard (8×8)**

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

size = 50
start_x = -200
start_y = 200

for row in range(8):
    for col in range(8):
        x = start_x + col * size
        y = start_y - row * size
        color = "black" if (row + col) % 2 == 0 else "white"
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.pencolor("black")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()

turtle.update()
turtle.done()
```

**H3. Bar Chart**

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

values = [80, 120, 60, 150, 100]
colors = ["red", "blue", "green", "orange", "purple"]
bar_width = 40
gap = 20
start_x = -150
baseline_y = -150

# Baseline
turtle.penup()
turtle.goto(start_x - 10, baseline_y)
turtle.pendown()
turtle.pencolor("black")
turtle.pensize(2)
turtle.goto(start_x + len(values) * (bar_width + gap), baseline_y)

# Bars
for i, val in enumerate(values):
    x = start_x + i * (bar_width + gap)
    turtle.penup()
    turtle.goto(x, baseline_y)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    for j in range(2):
        turtle.forward(bar_width)
        turtle.left(90)
        turtle.forward(val)
        turtle.left(90)
    turtle.end_fill()
    # Label
    turtle.penup()
    turtle.goto(x + bar_width / 2, baseline_y + val + 5)
    turtle.pendown()
    turtle.write(str(val), align="center", font=("Arial", 10, "normal"))

turtle.update()
turtle.done()
```

**H4. Spiral Galaxy**

```python
import turtle
import math

turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("black")

colors = ["yellow", "white", "lightyellow"]

for i in range(150):
    angle = math.radians(137.5 * i)
    dist = i * 2
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    dot_size = max(2, 8 - i // 20)
    color = colors[i % len(colors)]
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(dot_size, color)

turtle.update()
turtle.done()
```

**H5. City Skyline**

```python
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("midnightblue")

# Buildings: (x, width, height)
buildings = [
    (-280, 80, 180), (-180, 60, 240), (-100, 90, 160),
    (10, 70, 280), (100, 80, 200), (200, 60, 150), (280, 70, 220)
]

for (bx, bw, bh) in buildings:
    turtle.penup()
    turtle.goto(bx, -250)
    turtle.pendown()
    turtle.fillcolor("dimgray")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(bw)
        turtle.left(90)
        turtle.forward(bh)
        turtle.left(90)
    turtle.end_fill()
    # Windows
    for wy in range(4):
        for wx in range(3):
            wx_pos = bx + 10 + wx * (bw // 3 - 2)
            wy_pos = -230 + wy * 55
            if wy_pos < -250 + bh - 10:
                turtle.penup()
                turtle.goto(wx_pos, wy_pos)
                turtle.pendown()
                turtle.dot(5, "yellow")

# Moon
turtle.penup()
turtle.goto(200, 150)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

turtle.update()
turtle.done()
```

**H6. Butterfly**

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

# Left upper wing
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.setheading(135)
turtle.circle(80, 270)
turtle.end_fill()

# Right upper wing
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.setheading(45)
turtle.circle(-80, 270)
turtle.end_fill()

# Left lower wing
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.setheading(225)
turtle.circle(-60, 240)
turtle.end_fill()

# Right lower wing
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.setheading(315)
turtle.circle(60, 240)
turtle.end_fill()

# Body
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(8, 360)
turtle.end_fill()

# Antennae
turtle.penup()
turtle.goto(0, 10)
turtle.pendown()
turtle.pencolor("black")
turtle.pensize(2)
turtle.setheading(135)
turtle.forward(50)
turtle.dot(6, "black")
turtle.penup()
turtle.goto(0, 10)
turtle.pendown()
turtle.setheading(45)
turtle.forward(50)
turtle.dot(6, "black")

turtle.update()
turtle.done()
```

**H7. Kaleidoscope Pattern**

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
size = 100

for i in range(12):
    turtle.fillcolor(colors[i % 6])
    turtle.begin_fill()
    # Draw one equilateral triangle
    for j in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.right(30)    # rotate 30 degrees for next triangle

turtle.update()
turtle.done()
```
