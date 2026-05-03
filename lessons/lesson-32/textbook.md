# Lesson 32: Turtle + Math Combo 🎨🔢

> **Goal:** Draw math-based art — Fibonacci spirals, Pythagorean shapes, sine waves, and geometric patterns.

---

## 1. Math Meets Art

When you combine math with turtle drawing, you get beautiful patterns! In this lesson, we use math formulas to control where and how the turtle draws.

---

## 2. Fibonacci Squares

The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...

Each number is the sum of the two before it. If you draw squares with these side lengths, they form a beautiful spiral!

```python
import turtle

t = turtle.Turtle()
t.speed(5)

# First 8 Fibonacci numbers
fib = [1, 1, 2, 3, 5, 8, 13, 21]

for size in fib:
    for i in range(4):
        t.forward(size * 10)   # scale up by 10
        t.right(90)
    t.right(90)   # rotate for next square

turtle.done()
```

---

## 3. Sine Wave with Turtle

We can approximate a sine wave by moving the turtle along the x-axis and using `math.sin()` for the y-position:

```python
import turtle
import math

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-300, 0)
t.pendown()

for x in range(-300, 301):
    y = 100 * math.sin(x * math.pi / 180)
    t.goto(x, y)

turtle.done()
```

---

## 4. Polar Rose

A polar rose uses the formula r = cos(k × θ). With k=3, you get a 3-petal rose:

```python
import turtle
import math

t = turtle.Turtle()
t.speed(0)

for angle in range(0, 360, 1):
    theta = angle * math.pi / 180
    r = 150 * math.cos(3 * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if angle == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

turtle.done()
```

---

## 5. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| Fibonacci spiral | xoắn ốc Fibonacci | A spiral based on Fibonacci numbers |
| golden ratio | tỉ lệ vàng | The ratio ≈ 1.618, related to Fibonacci |
| sine wave | sóng sin | A smooth wave shape from the sin() function |
| approximation | xấp xỉ | A close but not exact value |
| mathematical art | nghệ thuật toán học | Art created using math formulas |
| combine | kết hợp | Use two things together |
| visualize | trực quan hóa | Show something visually |
| pattern | hoa văn | A repeated design |

---

## 6. Summary

✅ Fibonacci numbers create beautiful spiral patterns.
✅ `math.sin()` and `math.cos()` create wave and circular patterns.
✅ Polar coordinates (r, θ) can draw roses and spirals.
✅ Combining math with turtle creates mathematical art.

---

## 7. Homework

### 🟢 Easy

---

**Exercise E1. Fibonacci Sizes**

Draw 6 squares with side lengths equal to the first 6 Fibonacci numbers × 10 (10, 10, 20, 30, 50, 80). Place them in a row.

- **Input:** None.
- **Output:** 6 squares of Fibonacci sizes in a row.

---

**Exercise E2. Pythagorean Triple**

Draw a right triangle with sides 3, 4, 5 (scaled by 30). Verify visually that it looks like a right angle.

- **Input:** None.
- **Output:** A right triangle with sides 90, 120, 150.

---

**Exercise E3. Sine Wave**

Draw a sine wave: for x from -300 to 300, y = 80 * sin(x * π / 180). Use `math.sin()`.

- **Input:** None.
- **Output:** A smooth sine wave on screen.

---

**Exercise E4. Cosine Wave**

Draw a cosine wave: for x from -300 to 300, y = 80 * cos(x * π / 180).

- **Input:** None.
- **Output:** A smooth cosine wave on screen.

---

**Exercise E5. Circle from Math**

Draw a circle using math: for angle 0 to 360, x = 100 * cos(angle), y = 100 * sin(angle). Move turtle to each point.

- **Input:** None.
- **Output:** A circle drawn using math formulas.

---

**Exercise E6. Spiral**

Draw a spiral: in each step, move forward by `i * 2` and turn right 91 degrees. Repeat 100 times.

- **Input:** None.
- **Output:** A square spiral.

---

**Exercise E7. Star Polygon**

Draw a star polygon: repeat 5 times (forward 150, right 144). Then repeat with 7 points (forward 150, right 360/7 * 2).

- **Input:** None.
- **Output:** Two star polygons.

---

### 🟡 Medium

---

**Exercise M1. Fibonacci Spiral**

Draw the first 8 Fibonacci squares arranged so they form a spiral pattern (each square rotated 90° from the previous).

- **Input:** None.
- **Output:** 8 Fibonacci squares forming a spiral.

---

**Exercise M2. Sine and Cosine Together**

Draw both a sine wave (red) and a cosine wave (blue) on the same screen.

- **Input:** None.
- **Output:** Two overlapping waves in different colors.

---

**Exercise M3. Polar Rose (3 petals)**

Draw a polar rose with k=3: r = 150 * cos(3θ) for θ from 0 to 360 degrees.

- **Input:** None.
- **Output:** A 3-petal rose.

---

**Exercise M4. Lissajous Figure**

Draw a Lissajous figure: x = 200 * sin(3t), y = 200 * sin(2t) for t from 0 to 2π (use 360 steps).

- **Input:** None.
- **Output:** A Lissajous figure.

---

**Exercise M5. Multiplication Table Pattern**

Draw a pattern based on the multiplication table: for each pair (i, j) where i*j is even, draw a small square at position (i*30, j*30).

- **Input:** None.
- **Output:** A grid pattern.

---

**Exercise M6. Pythagorean Tree (2 levels)**

Draw a Pythagorean tree: start with a square, then draw two smaller squares on the hypotenuse of a right triangle on top. 2 levels deep.

- **Input:** None.
- **Output:** A simple Pythagorean tree.

---

**Exercise M7. Golden Spiral Approximation**

Draw an approximation of the golden spiral using Fibonacci squares: draw a quarter-circle arc inside each Fibonacci square.

- **Input:** None.
- **Output:** A golden spiral approximation.

---

### 🔴 Hard

---

**Exercise H1. Fibonacci Squares Spiral**

Draw the first 8 Fibonacci squares arranged in a spiral (each square placed adjacent to the previous, rotating 90° each time).

- **Input:** None.
- **Output:** 8 Fibonacci squares forming a classic spiral arrangement.

---

**Exercise H2. Pythagorean Tree (3 levels)**

Draw a Pythagorean tree fractal 3 levels deep. Start with a square of size 80, then recursively draw two smaller squares on top.

- **Input:** None.
- **Output:** A Pythagorean tree 3 levels deep.

---

**Exercise H3. Sine Wave**

Draw a sine wave using turtle: x from -300 to 300, y = 100 * sin(x * π / 180). Draw the x-axis too.

- **Input:** None.
- **Output:** A sine wave with an x-axis.

---

**Exercise H4. Polar Rose**

Draw a polar rose with k=3: r = cos(3θ). Scale r by 150. Loop θ from 0 to 360 degrees in steps of 1.

- **Input:** None.
- **Output:** A 3-petal polar rose.

---

**Exercise H5. Lissajous Figure**

Draw a Lissajous figure: x = 200 * sin(3t * π/180), y = 200 * sin(2t * π/180) for t from 0 to 360.

- **Input:** None.
- **Output:** A Lissajous figure.

---

**Exercise H6. Number Spiral (Simplified)**

Draw numbers 1 to 25 arranged in a 5×5 spiral pattern. Mark prime numbers with a dot.

- **Input:** None.
- **Output:** A 5×5 number spiral with primes marked.

---

**Exercise H7. Fractal Tree (4 levels)**

Draw a fractal tree: start with a trunk, then split into two branches at an angle. Each branch splits again. 4 levels deep.

- **Input:** None.
- **Output:** A fractal tree 4 levels deep.
