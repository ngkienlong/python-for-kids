# Lesson 12: Answers — Meet the Turtle

---

## 🟢 Easy

**E1. Draw a Line**
```python
import turtle
turtle.forward(150)
turtle.done()
```

**E2. Draw a Square**
```python
import turtle
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**E3. Draw a Triangle**
```python
import turtle
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.done()
```

**E4. Two Separate Lines**
```python
import turtle
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.done()
```

**E5. Draw a Cross (+)**
```python
import turtle
# Horizontal arm
turtle.penup()
turtle.goto(-80, 0)
turtle.pendown()
turtle.goto(80, 0)
# Vertical arm
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)
turtle.done()
```

**E6. Draw a Rectangle**
```python
import turtle
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**E7. Draw the Letter L**
```python
import turtle
turtle.left(90)
turtle.forward(100)   # vertical stroke up
turtle.backward(100)  # back to bottom
turtle.right(90)
turtle.forward(60)    # horizontal stroke right
turtle.done()
```

---

## 🟡 Medium

**M1. Draw a Pentagon**
```python
import turtle
for i in range(5):
    turtle.forward(100)
    turtle.right(72)
turtle.done()
```

**M2. Draw a Hexagon**
```python
import turtle
for i in range(6):
    turtle.forward(80)
    turtle.right(60)
turtle.done()
```

**M3. Draw a Staircase**
```python
import turtle
for i in range(4):
    turtle.forward(40)   # horizontal step
    turtle.left(90)
    turtle.forward(40)   # vertical step
    turtle.right(90)
turtle.done()
```

**M4. Draw a Grid**
```python
import turtle
turtle.speed(0)
size = 60
for row in range(3):
    for col in range(3):
        turtle.penup()
        turtle.goto(col * size - 90, row * size - 90)
        turtle.pendown()
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)
turtle.done()
```

**M5. Draw a Zigzag**
```python
import turtle
turtle.left(45)
for i in range(5):
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
turtle.done()
```

**M6. Draw a Diamond**
```python
import turtle
turtle.left(45)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

**M7. Draw Initials (example: letter A)**
```python
import turtle
# Draw letter A
turtle.speed(3)
turtle.penup()
turtle.goto(-30, 0)
turtle.pendown()
turtle.goto(0, 80)    # left diagonal
turtle.goto(30, 0)    # right diagonal
turtle.penup()
turtle.goto(-15, 40)
turtle.pendown()
turtle.goto(15, 40)   # crossbar
turtle.done()
```

---

## 🔴 Hard

**H1. Draw a Rectangle (200×100)**
```python
import turtle
# Start at top-left corner so it's roughly centered
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```
*Start at (-100, 50) so the rectangle is centered at the origin.*

**H2. Draw a Right-Pointing Arrow**
```python
import turtle
turtle.speed(3)
# Arrow body (rectangle)
turtle.penup()
turtle.goto(-80, -20)
turtle.pendown()
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.backward(80)
turtle.right(90)
turtle.forward(40)
# Arrow head (triangle)
turtle.penup()
turtle.goto(0, -40)
turtle.pendown()
turtle.goto(60, 0)
turtle.goto(0, 40)
turtle.goto(0, 20)
turtle.done()
```
*The body is a rectangle on the left, the head is a triangle pointing right.*

**H3. Draw the Letter "L"**
```python
import turtle
turtle.speed(3)
turtle.penup()
turtle.goto(-20, 60)
turtle.pendown()
turtle.setheading(270)   # face downward
turtle.forward(120)      # vertical stroke
turtle.setheading(0)     # face right
turtle.forward(80)       # horizontal stroke
turtle.done()
```
*`setheading(270)` points the turtle straight down. `setheading(0)` points right.*

**H4. Draw a Plus Sign (+)**
```python
import turtle
turtle.speed(3)
# Horizontal bar
turtle.penup()
turtle.goto(-80, 0)
turtle.pendown()
turtle.goto(80, 0)
# Vertical bar
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)
turtle.done()
```
*Use goto() to draw each arm of the plus sign directly.*

**H5. Draw a Staircase (3 Steps)**
```python
import turtle
turtle.speed(3)
turtle.penup()
turtle.goto(-75, -75)
turtle.pendown()
for i in range(3):
    turtle.forward(50)   # horizontal step
    turtle.left(90)
    turtle.forward(50)   # vertical step
    turtle.right(90)
turtle.done()
```
*Each step goes right 50px then up 50px.*

**H6. Draw a House Outline**
```python
import turtle
turtle.speed(3)
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
# Square base
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
# Move to bottom-left of roof
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
# Triangle roof
turtle.goto(0, 100)    # peak
turtle.goto(50, 50)    # right corner
turtle.done()
```
*Draw the square base first, then add the triangular roof on top.*

**H7. Draw the Letter "T"**
```python
import turtle
turtle.speed(3)
# Horizontal bar (top of T)
turtle.penup()
turtle.goto(-60, 50)
turtle.pendown()
turtle.goto(60, 50)
# Vertical stroke (down from center)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(0, -50)
turtle.done()
```
*Draw the horizontal bar first, then the vertical stroke from the center downward.*
