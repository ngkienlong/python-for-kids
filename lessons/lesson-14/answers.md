# Lesson 14: Answers — Loops + Turtle = Magic

---

## 🟢 Easy

**E1. Draw a Pentagon**
```python
import turtle
for i in range(5):
    turtle.forward(100)
    turtle.right(72)
turtle.done()
```

**E2. Draw a Hexagon**
```python
import turtle
for i in range(6):
    turtle.forward(80)
    turtle.right(60)
turtle.done()
```

**E3. Draw a 5-Pointed Star**
```python
import turtle
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.done()
```

**E4. Draw 3 Concentric Circles**
```python
import turtle
for r in [30, 60, 90]:
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)
turtle.done()
```

**E5. Draw a Simple Spiral**
```python
import turtle
distance = 10
for i in range(10):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 10
turtle.done()
```

**E6. Draw an Octagon**
```python
import turtle
for i in range(8):
    turtle.forward(70)
    turtle.right(45)
turtle.done()
```

**E7. Triangle, Square, Pentagon in a Row**
```python
import turtle
turtle.speed(0)
shapes = [3, 4, 5]
x_positions = [-150, -30, 90]
for idx in range(3):
    turtle.penup()
    turtle.goto(x_positions[idx], 0)
    turtle.pendown()
    n = shapes[idx]
    for i in range(n):
        turtle.forward(60)
        turtle.right(360 / n)
turtle.done()
```

---

## 🟡 Medium

**M1. Colored Polygon**
```python
import turtle
turtle.pencolor("blue")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(6):
    turtle.forward(80)
    turtle.right(60)
turtle.end_fill()
turtle.done()
```

**M2. Colored Star**
```python
import turtle
turtle.pencolor("black")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
turtle.done()
```

**M3. Concentric Colored Circles**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    r = (i + 1) * 20
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.circle(r)
turtle.done()
```

**M4. Polygon Spiral**
```python
import turtle
turtle.speed(0)
for size in range(10, 101, 10):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
turtle.done()
```

**M5. Star Burst**
```python
import turtle
turtle.speed(3)
for i in range(8):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)
turtle.done()
```

**M6. Nested Polygons**
```python
import turtle
turtle.speed(0)
for n in range(3, 8):
    for i in range(n):
        turtle.forward(80)
        turtle.right(360 / n)
turtle.done()
```

**M7. Colorful Star**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    turtle.pencolor(colors[i])
    turtle.forward(100)
    turtle.right(144)
turtle.done()
```

---

## 🔴 Hard

**H1. Regular Hexagon**
```python
import turtle
turtle.pencolor("darkorange")
turtle.fillcolor("gold")
turtle.pensize(2)
turtle.begin_fill()
for i in range(6):
    turtle.forward(100)
    turtle.right(60)
turtle.end_fill()
turtle.done()
```
*Exterior angle of hexagon = 360/6 = 60°.*

**H2. 6-Pointed Star**
```python
import turtle
turtle.speed(3)
# First triangle (pointing up)
turtle.pencolor("blue")
turtle.penup()
turtle.goto(0, -60)
turtle.pendown()
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
# Second triangle (pointing down — rotate 180 degrees)
turtle.pencolor("red")
turtle.penup()
turtle.goto(-50, 27)
turtle.pendown()
turtle.setheading(0)
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.done()
```
*Draw one triangle pointing up, then another pointing down, overlapping to form a Star of David.*

**H3. 5 Concentric Squares**
```python
import turtle
turtle.speed(0)
for size in range(20, 101, 20):
    turtle.penup()
    turtle.goto(-size // 2, -size // 2)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
turtle.done()
```
*Center each square by starting at (-size/2, -size/2).*

**H4. Spiral Square**
```python
import turtle
turtle.speed(0)
distance = 10
for i in range(20):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5
turtle.done()
```
*Each side is 5 pixels longer than the previous. After 4 sides, the spiral has grown outward.*

**H5. Flower from Circles**
```python
import turtle
import math
turtle.speed(0)
ring_radius = 80
petal_radius = 40
for i in range(12):
    angle = i * 30
    x = ring_radius * math.cos(math.radians(angle))
    y = ring_radius * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(x, y - petal_radius)
    turtle.pendown()
    turtle.circle(petal_radius)
turtle.done()
```
*Place 12 circles evenly around a ring (every 30°) using cos/sin for positioning.*

**H6. Snowflake**
```python
import turtle
turtle.speed(0)
turtle.pencolor("blue")
for arm in range(6):
    # Draw main arm
    turtle.forward(100)
    # Draw right branch
    turtle.right(60)
    turtle.forward(40)
    turtle.backward(40)
    # Draw left branch
    turtle.left(120)
    turtle.forward(40)
    turtle.backward(40)
    turtle.right(60)
    # Return to center
    turtle.backward(100)
    # Rotate for next arm
    turtle.right(60)
turtle.done()
```
*For each arm: go forward, draw two branches, come back, rotate 60° for the next arm.*

**H7. Color-Changing Polygon Spiral**
```python
import turtle
import math
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue",
          "indigo", "violet", "pink", "cyan", "magenta"]
for idx in range(10):
    side = 30 + idx * 10
    turtle.pencolor(colors[idx])
    turtle.right(idx * 6)   # rotate a little more each time
    for i in range(6):
        turtle.forward(side)
        turtle.right(60)
turtle.done()
```
*Each hexagon is larger and rotated 6° more than the previous, creating a spiral effect.*
