# Lesson 16: Answers 🎨

---

## 🟢 Easy

**E1.**
```python
import turtle
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.done()
```

**E2.**
```python
import turtle
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-50, 20)
turtle.pendown()
turtle.goto(50, 20)
turtle.goto(0, 80)
turtle.goto(-50, 20)
turtle.end_fill()
turtle.done()
```

**E3.**
```python
import turtle
turtle.penup()
turtle.goto(-10, -80)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()
turtle.done()
```

**E4.**
```python
import turtle
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()
```

**E5.**
```python
import turtle
turtle.penup()
turtle.goto(-20, 20)
turtle.pendown()
turtle.dot(12, "black")
turtle.penup()
turtle.goto(20, 20)
turtle.pendown()
turtle.dot(12, "black")
turtle.done()
```

**E6.**
```python
import turtle
turtle.pensize(4)
turtle.pencolor("green")
turtle.penup()
turtle.goto(-300, -100)
turtle.pendown()
turtle.goto(300, -100)
turtle.done()
```

**E7.**
```python
import turtle
turtle.bgcolor("lightblue")
turtle.pensize(4)
turtle.pencolor("green")
turtle.penup()
turtle.goto(-300, -100)
turtle.pendown()
turtle.goto(300, -100)
turtle.done()
```

---

## 🟡 Medium

**M1.**
```python
import turtle
# House body
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
# Roof
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-50, 20)
turtle.pendown()
turtle.goto(50, 20)
turtle.goto(0, 80)
turtle.goto(-50, 20)
turtle.end_fill()
turtle.done()
```

**M2.**
```python
import turtle
# Trunk
turtle.penup()
turtle.goto(-10, -80)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()
# Canopy
turtle.fillcolor("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-40, -40)
turtle.pendown()
turtle.goto(40, -40)
turtle.goto(0, 40)
turtle.goto(-40, -40)
turtle.end_fill()
turtle.done()
```

**M3.**
```python
import turtle
turtle.speed(0)
# Sun circle
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
# 8 rays
for i in range(8):
    turtle.penup()
    turtle.goto(150, 130)
    turtle.setheading(90 + i * 45)
    turtle.pendown()
    turtle.forward(50)
turtle.done()
```

**M4.**
```python
import turtle
# Head
turtle.penup()
turtle.goto(0, -60)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
# Left eye
turtle.penup()
turtle.goto(-20, 20)
turtle.pendown()
turtle.dot(12, "black")
# Right eye
turtle.penup()
turtle.goto(20, 20)
turtle.pendown()
turtle.dot(12, "black")
# Smile
turtle.penup()
turtle.goto(-20, -10)
turtle.pendown()
turtle.setheading(-60)
turtle.circle(25, 120)
turtle.done()
```

**M5.**
```python
import turtle
# House body
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
# Roof
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-50, 20)
turtle.pendown()
turtle.goto(50, 20)
turtle.goto(0, 80)
turtle.goto(-50, 20)
turtle.end_fill()
# Door
turtle.penup()
turtle.goto(-10, -80)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
turtle.end_fill()
turtle.done()
```

**M6.**
```python
import turtle
turtle.speed(0)
turtle.bgcolor("lightblue")
# Ground
turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(300, -200)
turtle.goto(300, -100)
turtle.goto(-300, -100)
turtle.goto(-300, -200)
turtle.end_fill()
# Sun
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()
```

**M7.**
```python
import turtle
turtle.speed(0)

def draw_tree(cx):
    # Trunk
    turtle.penup()
    turtle.goto(cx - 10, -80)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()
    # Canopy
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(cx - 40, -40)
    turtle.pendown()
    turtle.goto(cx + 40, -40)
    turtle.goto(cx, 40)
    turtle.goto(cx - 40, -40)
    turtle.end_fill()

draw_tree(50)
draw_tree(150)
turtle.done()
```

---

## 🔴 Hard

**H1. House with Door and Windows**

Draw each part separately using `goto()` to position them precisely.

```python
import turtle
turtle.speed(0)

# House body
turtle.penup()
turtle.goto(-60, -100)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(120)
    turtle.left(90)
turtle.end_fill()

# Roof
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-60, 20)
turtle.pendown()
turtle.goto(60, 20)
turtle.goto(0, 80)
turtle.goto(-60, 20)
turtle.end_fill()

# Door
turtle.penup()
turtle.goto(-12, -100)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()

# Left window
turtle.penup()
turtle.goto(-50, -30)
turtle.pendown()
turtle.fillcolor("lightblue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

# Right window
turtle.penup()
turtle.goto(25, -30)
turtle.pendown()
turtle.fillcolor("lightblue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

turtle.done()
```

**H2. Tree with Round Canopy**

Use `circle()` for the round canopy instead of a triangle.

```python
import turtle
turtle.speed(0)

# Trunk
turtle.penup()
turtle.goto(-10, -100)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

# Round canopy (circle centered at (0, 0))
turtle.penup()
turtle.goto(0, -45)   # goto bottom of circle (circle() starts drawing from bottom)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

turtle.done()
```

**H3. Sun with 12 Rays**

Use a loop with 30° spacing to draw 12 rays.

```python
import turtle
turtle.speed(0)

cx, cy = 150, 120
radius = 35
ray_length = 55

# Sun circle
turtle.penup()
turtle.goto(cx, cy - radius)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# 12 rays
for i in range(12):
    angle = 90 + i * 30
    # Start from edge of circle
    import math
    start_x = cx + radius * math.cos(math.radians(angle))
    start_y = cy + radius * math.sin(math.radians(angle))
    end_x = cx + (radius + ray_length) * math.cos(math.radians(angle))
    end_y = cy + (radius + ray_length) * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)

turtle.done()
```

**H4. Robot Face**

Draw each part of the robot face using rectangles and lines.

```python
import turtle
turtle.speed(0)

# Head (gray rectangle)
turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.fillcolor("gray")
turtle.begin_fill()
for i in range(2):
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# Left eye
turtle.penup()
turtle.goto(-45, 10)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

# Right eye
turtle.penup()
turtle.goto(20, 10)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

# Mouth (horizontal line)
turtle.penup()
turtle.goto(-25, -30)
turtle.pendown()
turtle.pensize(3)
turtle.goto(25, -30)

# Antenna (vertical line + circle)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.pensize(2)
turtle.goto(0, 90)
turtle.dot(10, "red")

turtle.done()
```

**H5. Simple Car**

Draw the car body, cabin, and two wheels.

```python
import turtle
turtle.speed(0)

# Car body (blue rectangle)
turtle.penup()
turtle.goto(-80, -60)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(2):
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()

# Cabin (dark gray rectangle on top)
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.fillcolor("darkgray")
turtle.begin_fill()
for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

# Left wheel
turtle.penup()
turtle.goto(-50, -85)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# Right wheel
turtle.penup()
turtle.goto(25, -85)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.done()
```

**H6. Night Scene**

Use a black background, yellow moon, and white dots for stars.

```python
import turtle
import random
turtle.speed(0)
turtle.bgcolor("black")

# Moon
turtle.penup()
turtle.goto(150, 85)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

# Stars (10 white dots at random positions)
star_positions = [
    (-200, 150), (-100, 180), (0, 160), (50, 130), (-150, 100),
    (200, 170), (-250, 50), (100, 50), (-50, 200), (220, 80)
]
for (sx, sy) in star_positions:
    turtle.penup()
    turtle.goto(sx, sy)
    turtle.pendown()
    turtle.dot(6, "white")

turtle.done()
```

**H7. Garden Scene**

Draw sky, ground, and three flowers with petals using a loop.

```python
import turtle
turtle.speed(0)
turtle.bgcolor("lightblue")

# Ground
turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(300, -200)
turtle.goto(300, -80)
turtle.goto(-300, -80)
turtle.goto(-300, -200)
turtle.end_fill()

petal_colors = ["red", "orange", "pink"]
flower_x = [-120, 0, 120]

for idx in range(3):
    fx = flower_x[idx]
    # Stem
    turtle.penup()
    turtle.goto(fx, -80)
    turtle.pendown()
    turtle.pencolor("darkgreen")
    turtle.pensize(3)
    turtle.goto(fx, 20)
    # 6 petals
    turtle.pensize(1)
    for p in range(6):
        turtle.penup()
        turtle.goto(fx, 20)
        turtle.setheading(p * 60)
        turtle.pendown()
        turtle.fillcolor(petal_colors[idx])
        turtle.begin_fill()
        turtle.circle(15, 360)
        turtle.end_fill()
        turtle.forward(20)
    # Center
    turtle.penup()
    turtle.goto(fx, 20)
    turtle.pendown()
    turtle.dot(18, "yellow")

turtle.done()
```
