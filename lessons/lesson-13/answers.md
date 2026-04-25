# Lesson 13: Answers — Colors and Shapes

---

## 🟢 Easy

**E1. Colored Lines**
```python
import turtle
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    turtle.pencolor(color)
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**E2. Filled Square**
```python
import turtle
turtle.pencolor("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done()
```

**E3. Filled Circle**
```python
import turtle
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.done()
```

**E4. Thick Lines**
```python
import turtle
turtle.pensize(5)
turtle.pencolor("purple")
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**E5. Colorful Triangle**
```python
import turtle
turtle.pencolor("black")
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.end_fill()
turtle.done()
```

**E6. Background Color**
```python
import turtle
turtle.bgcolor("darkblue")
turtle.pencolor("white")
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**E7. Three Circles**
```python
import turtle
colors = ["red", "green", "blue"]
x_positions = [-120, 0, 120]
for i in range(3):
    turtle.penup()
    turtle.goto(x_positions[i], -40)
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
turtle.done()
```

---

## 🟡 Medium

**M1. Rainbow Lines**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle.pensize(3)
for i in range(7):
    turtle.penup()
    turtle.goto(-150, 80 - i * 25)
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.forward(300)
turtle.done()
```

**M2. Filled Rectangle**
```python
import turtle
turtle.pencolor("purple")
turtle.fillcolor("orange")
turtle.pensize(3)
turtle.begin_fill()
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done()
```

**M3. Concentric Circles**
```python
import turtle
colors = ["red", "orange", "yellow", "green"]
radii = [20, 40, 60, 80]
for i in range(4):
    turtle.penup()
    turtle.goto(0, -radii[i])
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.circle(radii[i])
turtle.done()
```

**M4. Colorful Squares**
```python
import turtle
colors = ["red", "orange", "yellow", "green", "blue"]
sizes = [20, 40, 60, 80, 100]
for i in range(5):
    turtle.penup()
    turtle.goto(-sizes[i] // 2, -sizes[i] // 2)
    turtle.pendown()
    turtle.pencolor(colors[i])
    for j in range(4):
        turtle.forward(sizes[i])
        turtle.right(90)
turtle.done()
```

**M5. Filled Pentagon**
```python
import turtle
turtle.pencolor("black")
turtle.fillcolor("purple")
turtle.begin_fill()
for i in range(5):
    turtle.forward(80)
    turtle.right(72)
turtle.end_fill()
turtle.done()
```

**M6. Two Filled Shapes**
```python
import turtle
# Red circle on the left
turtle.penup()
turtle.goto(-120, -50)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
# Blue square on the right
turtle.penup()
turtle.goto(40, -40)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(80)
    turtle.right(90)
turtle.end_fill()
turtle.done()
```

**M7. Color Wheel**
```python
import turtle
import math
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
radius = 80   # distance from center to each circle
for i in range(6):
    angle = i * 60
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(x, y - 30)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
turtle.done()
```

---

## 🔴 Hard

**H1. Filled Red Circle**
```python
import turtle
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.fillcolor("red")
turtle.pencolor("red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.done()
```
*Move to (0, -80) first so the circle is centered at the origin.*

**H2. Traffic Light**
```python
import turtle
turtle.speed(0)
# Draw black rectangle (traffic light body)
turtle.penup()
turtle.goto(-35, -120)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
for i in range(2):
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
turtle.end_fill()
# Draw the three lights
light_colors = ["red", "yellow", "green"]
y_positions = [60, 0, -60]
for i in range(3):
    turtle.penup()
    turtle.goto(0, y_positions[i] - 25)
    turtle.pendown()
    turtle.fillcolor(light_colors[i])
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
turtle.done()
```
*Draw the black rectangle body first, then place three colored circles inside it.*

**H3. Filled House**
```python
import turtle
turtle.speed(3)
# Blue square base
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
# Red triangle roof
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(0, 110)
turtle.goto(50, 50)
turtle.goto(-50, 50)
turtle.end_fill()
turtle.done()
```
*Draw the square base, then use goto() to draw the triangular roof.*

**H4. Rainbow Arcs**
```python
import turtle
turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.pensize(4)
for i in range(7):
    turtle.pencolor(colors[6 - i])
    turtle.penup()
    turtle.goto(0, -20 - i * 12)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(80 + i * 12, 180)   # draw a semicircle
turtle.done()
```
*Draw semicircles of increasing radius, each in a rainbow color.*

**H5. Smiley Face**
```python
import turtle
turtle.speed(3)
# Yellow face
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
# Left eye
turtle.penup()
turtle.goto(-30, 20)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
# Right eye
turtle.penup()
turtle.goto(20, 20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
# Red smile (arc)
turtle.penup()
turtle.goto(-30, -20)
turtle.pendown()
turtle.pencolor("red")
turtle.pensize(3)
turtle.circle(30, 180)   # draw a 180-degree arc for the smile
turtle.done()
```
*Draw the face, then position the eyes and smile using goto().*

**H6. Flower**
```python
import turtle
import math
turtle.speed(0)
colors = ["red", "orange", "yellow", "pink", "purple", "cyan"]
petal_radius = 40
ring_radius = 60
# Draw 6 petals
for i in range(6):
    angle = i * 60
    x = ring_radius * math.cos(math.radians(angle))
    y = ring_radius * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(x, y - petal_radius)
    turtle.pendown()
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.circle(petal_radius)
    turtle.end_fill()
# Yellow center
turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.done()
```
*Place 6 circles evenly around a ring using trigonometry, then add a center circle.*

**H7. Vietnamese Flag**
```python
import turtle
turtle.speed(0)
# Red rectangle background
turtle.penup()
turtle.goto(-100, -65)
turtle.pendown()
turtle.fillcolor("red")
turtle.pencolor("red")
turtle.begin_fill()
for i in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
turtle.end_fill()
# Yellow 5-pointed star outline in center
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.pencolor("yellow")
turtle.pensize(2)
turtle.setheading(90)
for i in range(5):
    turtle.forward(40)
    turtle.right(144)
turtle.done()
```
*Draw the red rectangle first, then draw the 5-pointed star outline in yellow at the center.*
