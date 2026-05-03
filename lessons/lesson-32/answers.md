# Lesson 32: Answers 🎨🔢

---

## 🟢 Easy

**E1.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

fib = [1, 1, 2, 3, 5, 8]
x = -200
for f in fib:
    size = f * 10
    move_to(x, 0)
    for i in range(4):
        t.forward(size)
        t.right(90)
    x += size + 10

turtle.done()
```

**E2.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(5)

# Right triangle with sides 3, 4, 5 (scaled by 30)
a, b, c = 90, 120, 150
t.goto(0, 0)
t.forward(a)
t.left(90)
t.forward(b)
t.goto(0, 0)

turtle.done()
```

**E3.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    y = 80 * math.sin(x * math.pi / 180)
    t.goto(x, y)

turtle.done()
```

**E4.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    y = 80 * math.cos(x * math.pi / 180)
    t.goto(x, y)

turtle.done()
```

**E5.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

first = True
for angle in range(361):
    rad = angle * math.pi / 180
    x = 100 * math.cos(rad)
    y = 100 * math.sin(rad)
    if first:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

turtle.done()
```

**E6.**
```python
import turtle
t = turtle.Turtle()
t.speed(0)

for i in range(100):
    t.forward(i * 2)
    t.right(91)

turtle.done()
```

**E7.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 5-pointed star
t.pencolor("red")
move_to(-100, 0)
for i in range(5):
    t.forward(100)
    t.right(144)

# 7-pointed star
t.pencolor("blue")
move_to(100, 0)
for i in range(7):
    t.forward(80)
    t.right(int(360 * 2 / 7))

turtle.done()
```

---

## 🟡 Medium

**M1.**
```python
import turtle
t = turtle.Turtle()
t.speed(8)

fib = [1, 1, 2, 3, 5, 8, 13, 21]
scale = 8

x, y = 0, 0
direction = 0   # 0=right, 1=up, 2=left, 3=down

for f in fib:
    size = f * scale
    t.penup()
    t.goto(x, y)
    t.setheading(direction * 90)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    # Move to next position
    if direction == 0:
        x += size
    elif direction == 1:
        y += size
    elif direction == 2:
        x -= size
    else:
        y -= size
    direction = (direction + 1) % 4

turtle.done()
```

**M2.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

# Sine wave (red)
t.pencolor("red")
t.penup()
t.goto(-300, 0)
t.pendown()
for x in range(-300, 301):
    y = 80 * math.sin(x * math.pi / 180)
    t.goto(x, y)

# Cosine wave (blue)
t.pencolor("blue")
t.penup()
t.goto(-300, 0)
t.pendown()
for x in range(-300, 301):
    y = 80 * math.cos(x * math.pi / 180)
    t.goto(x, y)

turtle.done()
```

**M3.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

first = True
for angle in range(361):
    theta = angle * math.pi / 180
    r = 150 * math.cos(3 * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if first:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

turtle.done()
```

**M4.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

first = True
for deg in range(361):
    t_rad = deg * math.pi / 180
    x = 200 * math.sin(3 * t_rad)
    y = 200 * math.sin(2 * t_rad)
    if first:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

turtle.done()
```

**M5.**
```python
import turtle
t = turtle.Turtle()
t.speed(0)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

for i in range(1, 8):
    for j in range(1, 8):
        if (i * j) % 2 == 0:
            move_to(i * 35 - 140, j * 35 - 140)
            for k in range(4):
                t.forward(15)
                t.right(90)

turtle.done()
```

**M6.**
```python
import turtle
t = turtle.Turtle()
t.speed(5)

def draw_square(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

# Level 0: base square
draw_square(-40, -100, 80)

# Level 1: two squares on top
draw_square(-40, -20, 56)
draw_square(16, -20, 56)

# Level 2: four squares
draw_square(-40, 36, 40)
draw_square(0, 36, 40)
draw_square(16, 36, 40)
draw_square(56, 36, 40)

turtle.done()
```

**M7.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(8)

fib = [1, 1, 2, 3, 5, 8, 13, 21]
scale = 8

x, y = 0, 0
direction = 0

for f in fib:
    size = f * scale
    # Draw the square
    t.penup()
    t.goto(x, y)
    t.setheading(direction * 90)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    # Draw quarter-circle arc inside the square
    t.pencolor("blue")
    t.penup()
    if direction == 0:
        t.goto(x, y)
    elif direction == 1:
        t.goto(x + size, y)
    elif direction == 2:
        t.goto(x + size, y + size)
    else:
        t.goto(x, y + size)
    t.setheading(direction * 90 + 90)
    t.pendown()
    t.circle(size, 90)
    t.pencolor("black")
    # Move to next position
    if direction == 0:
        x += size
    elif direction == 1:
        y += size
    elif direction == 2:
        x -= size
    else:
        y -= size
    direction = (direction + 1) % 4

turtle.done()
```

---

## 🔴 Hard

**H1.**
```python
import turtle
t = turtle.Turtle()
t.speed(8)

fib = [1, 1, 2, 3, 5, 8, 13, 21]
scale = 8

x, y = 0, 0
direction = 0   # 0=right, 1=up, 2=left, 3=down

for f in fib:
    size = f * scale
    t.penup()
    t.goto(x, y)
    t.setheading(direction * 90)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    if direction == 0:
        x += size
    elif direction == 1:
        y += size
    elif direction == 2:
        x -= size
    else:
        y -= size
    direction = (direction + 1) % 4

t.hideturtle()
turtle.done()
```
*Explanation: Place each Fibonacci square adjacent to the previous one, rotating 90° each time. The squares spiral outward.*

**H2.**
```python
import turtle
t = turtle.Turtle()
t.speed(8)

def draw_square(x, y, size, heading):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

def pythagorean_tree(x, y, size, heading, level):
    if level == 0:
        return
    # Draw the base square
    draw_square(x, y, size, heading)
    # Calculate top-left corner of the square
    import math
    rad = heading * math.pi / 180
    top_x = x + size * math.cos(rad + math.pi / 2) * (-1)
    top_y = y + size * math.sin(rad + math.pi / 2) * (-1)
    # Left branch (smaller square, rotated left)
    left_size = size * 0.7
    pythagorean_tree(top_x, top_y, left_size, heading - 45, level - 1)
    # Right branch
    right_size = size * 0.7
    pythagorean_tree(top_x + size * math.cos(rad), top_y + size * math.sin(rad),
                     right_size, heading + 45, level - 1)

pythagorean_tree(-40, -150, 80, 90, 3)
t.hideturtle()
turtle.done()
```
*Explanation: Recursively draw squares. Each square has two smaller squares on top, rotated ±45°. Stop at level 0.*

**H3.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

# Draw x-axis
t.pencolor("gray")
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)

# Draw sine wave
t.pencolor("blue")
t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    y = 100 * math.sin(x * math.pi / 180)
    t.goto(x, y)

t.hideturtle()
turtle.done()
```

**H4.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

first = True
for angle in range(361):
    theta = angle * math.pi / 180
    r = 150 * math.cos(3 * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if first:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

t.hideturtle()
turtle.done()
```

**H5.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

first = True
for deg in range(361):
    rad = deg * math.pi / 180
    x = 200 * math.sin(3 * rad)
    y = 200 * math.sin(2 * rad)
    if first:
        t.penup()
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

t.hideturtle()
turtle.done()
```
*Explanation: A Lissajous figure is drawn by using different frequencies for x and y. Here x uses frequency 3 and y uses frequency 2.*

**H6.**
```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Generate 5x5 spiral positions
def spiral_positions(n):
    """Generate positions for a spiral of n*n numbers."""
    positions = {}
    x, y = 0, 0
    dx, dy = 1, 0
    num = 1
    steps = 1
    while num <= n * n:
        for _ in range(2):
            for _ in range(steps):
                if num <= n * n:
                    positions[num] = (x * 40 - 80, y * 40 - 80)
                    num += 1
                x += dx
                y += dy
            dx, dy = -dy, dx
        steps += 1
    return positions

positions = spiral_positions(5)

for num, (x, y) in positions.items():
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(str(num), align="center", font=("Arial", 10, "normal"))
    if is_prime(num):
        t.goto(x, y - 5)
        t.dot(5, "red")

turtle.done()
```
*Explanation: Generate spiral positions for numbers 1-25, write each number, and mark primes with a red dot.*

**H7.**
```python
import turtle
import math
t = turtle.Turtle()
t.speed(0)

def fractal_tree(length, angle, level):
    """Draw a fractal tree branch."""
    if level == 0:
        return
    # Draw the trunk/branch
    t.forward(length)
    # Save position and heading
    pos = t.position()
    heading = t.heading()
    # Draw left branch
    t.left(angle)
    fractal_tree(length * 0.7, angle, level - 1)
    # Return to saved position
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()
    # Draw right branch
    t.right(angle)
    fractal_tree(length * 0.7, angle, level - 1)
    # Return to saved position
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

# Start at the bottom center
t.penup()
t.goto(0, -200)
t.setheading(90)   # point upward
t.pendown()

fractal_tree(80, 30, 4)

t.hideturtle()
turtle.done()
```
*Explanation: The fractal tree function draws a branch, then recursively draws two smaller branches at angles left and right. The base case (level=0) stops the recursion.*
