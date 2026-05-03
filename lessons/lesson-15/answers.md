# Lesson 15: Answers — Spirals and Patterns

---

## 🟢 Easy

**E1. Square Spiral (10 steps)**
```python
import turtle
turtle.speed(0)
distance = 10
for i in range(10):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 10
turtle.done()
```

**E2. Triangle Spiral (10 steps)**
```python
import turtle
turtle.speed(0)
distance = 10
for i in range(10):
    turtle.forward(distance)
    turtle.right(120)
    distance = distance + 10
turtle.done()
```

**E3. Color Square Spiral**
```python
import turtle
turtle.speed(0)
colors = ["red", "blue", "green", "yellow"]
distance = 10
for i in range(20):
    turtle.pencolor(colors[i % 4])
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5
turtle.done()
```

**E4. Rotating Squares (4 squares)**
```python
import turtle
turtle.speed(3)
for i in range(4):
    for j in range(4):
        turtle.forward(80)
        turtle.right(90)
    turtle.right(45)
turtle.done()
```

**E5. Galaxy Spiral**
```python
import turtle
turtle.speed(0)
distance = 1
for i in range(100):
    turtle.forward(distance)
    turtle.right(30)
    distance = distance + 0.5
turtle.done()
```

**E6. Color Triangle Spiral**
```python
import turtle
turtle.speed(0)
colors = ["red", "green", "blue"]
distance = 5
for i in range(30):
    turtle.pencolor(colors[i % 3])
    turtle.forward(distance)
    turtle.right(120)
    distance = distance + 3
turtle.done()
```

**E7. Starburst Lines**
```python
import turtle
import math
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple",
          "pink", "cyan", "magenta", "brown", "gray", "black"]
for i in range(12):
    turtle.pencolor(colors[i])
    turtle.forward(120)
    turtle.backward(120)
    turtle.right(30)
turtle.done()
```

---

## 🟡 Medium

**M1. Double Spiral**
```python
import turtle
turtle.speed(0)
# Clockwise spiral
turtle.pencolor("blue")
distance = 5
for i in range(30):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 4
# Counter-clockwise spiral
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()
turtle.pencolor("red")
distance = 5
for i in range(30):
    turtle.forward(distance)
    turtle.left(90)
    distance = distance + 4
turtle.done()
```

**M2. Rotating Triangles**
```python
import turtle
turtle.speed(0)
for i in range(12):
    for j in range(3):
        turtle.forward(80)
        turtle.right(120)
    turtle.right(30)
turtle.done()
```

**M3. Rainbow Square Spiral**
```python
import turtle
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = 5
for i in range(42):
    turtle.pencolor(colors[i % 6])
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5
turtle.done()
```

**M4. Hexagon Spiral**
```python
import turtle
turtle.speed(0)
for i in range(20):
    side = 20 + i * 5
    turtle.right(i * 5)
    for j in range(6):
        turtle.forward(side)
        turtle.right(60)
turtle.done()
```

**M5. Web Pattern**
```python
import turtle
turtle.speed(0)
# Draw spokes
for i in range(36):
    turtle.forward(150)
    turtle.backward(150)
    turtle.right(10)
# Draw concentric circles
for r in [50, 100, 150]:
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)
turtle.done()
```

**M6. Fibonacci Squares**
```python
import turtle
turtle.speed(0)
fib = [1, 1, 2, 3, 5, 8, 13, 21]
scale = 10
x, y = 0, 0
directions = [0, 90, 180, 270]   # right, up, left, down
for idx in range(len(fib)):
    size = fib[idx] * scale
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    # Move to next position (simplified arrangement)
    if idx % 4 == 0:
        x = x + size
    elif idx % 4 == 1:
        y = y + size
    elif idx % 4 == 2:
        x = x - size
    else:
        y = y - size
turtle.done()
```

**M7. Color Polygon Spiral**
```python
import turtle
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(20):
    side = 20 + i * 8
    turtle.pencolor(colors[i % 5])
    turtle.right(i * 7)
    for j in range(5):
        turtle.forward(side)
        turtle.right(72)
turtle.done()
```

---

## 🔴 Hard

**H1. Square Spiral (30 iterations)**
```python
import turtle
turtle.tracer(0)
distance = 10
for i in range(30):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5
turtle.update()
turtle.done()
```
*`tracer(0)` skips animation. `update()` shows the final result. Side grows from 10 to 10+29×5=155.*

**H2. Triangle Spiral (20 iterations)**
```python
import turtle
turtle.tracer(0)
distance = 10
for i in range(20):
    turtle.forward(distance)
    turtle.right(120)
    distance = distance + 8
turtle.update()
turtle.done()
```
*Turn 120° each step (triangle exterior angle). Side grows from 10 to 10+19×8=162.*

**H3. Rotating Squares (20 squares)**
```python
import turtle
turtle.tracer(0)
for i in range(20):
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(18)   # 20 squares × 18° = 360° full rotation
turtle.update()
turtle.done()
```
*20 squares × 18° = 360°, so the pattern completes a full circle.*

**H4. Color Spiral (6 colors)**
```python
import turtle
turtle.tracer(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = 5
for i in range(60):
    turtle.pencolor(colors[i % 6])
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 4
turtle.update()
turtle.done()
```
*6 colors cycle every 6 steps. The spiral grows by 4 pixels per step.*

**H5. Sunflower Spiral**
```python
import turtle
import math
turtle.tracer(0)
turtle.penup()
golden_angle = 137.5   # the golden angle in degrees
colors = ["yellow", "gold", "orange"]
for i in range(100):
    angle = i * golden_angle
    distance = i * 4
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    turtle.goto(x, y)
    turtle.pencolor(colors[i % 3])
    turtle.dot(8)
turtle.update()
turtle.done()
```
*The golden angle (137.5°) creates the natural spiral pattern seen in sunflowers. Each dot is placed at distance i×4 from center, rotated by 137.5°×i.*

**H6. Web Pattern**
```python
import turtle
turtle.tracer(0)
turtle.pencolor("gray")
# Draw 18 spokes (every 20 degrees)
for i in range(18):
    turtle.forward(150)
    turtle.backward(150)
    turtle.right(20)
# Draw 4 concentric circles
for r in [40, 80, 120, 150]:
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)
turtle.update()
turtle.done()
```
*18 spokes × 20° = 360°. Concentric circles connect the spokes to form the web rings.*

**H7. Fibonacci Spiral**
```python
import turtle
turtle.tracer(0)
turtle.speed(0)
fib = [1, 1, 2, 3, 5, 8, 13, 21]
scale = 10
# Starting position and direction for each square
# Arrange squares in the classic Fibonacci tiling pattern
positions = [
    (0, 0, 0),       # size 1: start at (0,0), heading right
    (10, 0, 90),     # size 1: start at (10,0), heading up
    (0, 10, 180),    # size 2: start at (0,10+20=30)... simplified
]
# Draw squares and arcs
x, y = 0, 0
heading = 0
for idx in range(len(fib)):
    size = fib[idx] * scale
    # Draw square
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.pencolor("black")
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    # Draw quarter-circle arc inside the square
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading + 90)
    turtle.pendown()
    turtle.circle(size, 90)
    # Move to next square position
    if heading == 0:
        x = x + size
    elif heading == 90:
        y = y + size
    elif heading == 180:
        x = x - size
    else:
        y = y - size
    heading = (heading + 90) % 360
turtle.update()
turtle.done()
```
*Each Fibonacci square is placed adjacent to the previous one, rotating 90° each time. A quarter-circle arc inside each square approximates the Fibonacci spiral.*
