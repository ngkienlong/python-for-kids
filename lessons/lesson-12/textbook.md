# Lesson 12: Meet the Turtle 🐢

> **Goal:** Use Python's `turtle` module to draw lines and shapes by moving a virtual turtle on screen.

---

This lesson uses Python's `turtle` module, which requires a graphical window. Please open **Thonny** to run the examples. If you haven't installed Thonny yet, install it before continuing.

## 1. What is the Turtle?

The **turtle** is a small arrow on the screen that you can control with code. When you move the turtle, it draws a line behind it — just like dragging a pen across paper.

> 💡 **Scratch connection:** The turtle module is like the **Pen extension** in Scratch! `pendown()` = "Pen Down", `forward()` = "move N steps", `right()` = "turn right N degrees".

| Scratch | Python Turtle |
|---------|--------------|
| Pen Down | `turtle.pendown()` |
| Pen Up | `turtle.penup()` |
| Move 100 steps | `turtle.forward(100)` |
| Turn right 90 degrees | `turtle.right(90)` |
| Go to x, y | `turtle.goto(x, y)` |

---

## 2. Setting Up Turtle

Every turtle program starts with `import turtle` and ends with `turtle.done()`.

```python
import turtle

# Your drawing code goes here

turtle.done()   # keeps the window open until you close it
```

---

## 3. The Turtle's Starting Position

When you start, the turtle is at the **center** of the screen at coordinates **(0, 0)**, facing **right**.

```
         y
         |
         |
---------+--------- x
         |
         |
       (0,0) = center
```

- Moving **forward** goes in the direction the turtle is facing.
- `right(90)` turns **clockwise** by 90 degrees.
- `left(90)` turns **counter-clockwise** by 90 degrees.

---

## 4. Basic Commands

| Command | What it does |
|---------|-------------|
| `turtle.forward(100)` | Move forward 100 pixels |
| `turtle.backward(50)` | Move backward 50 pixels |
| `turtle.right(90)` | Turn right (clockwise) 90 degrees |
| `turtle.left(45)` | Turn left (counter-clockwise) 45 degrees |
| `turtle.penup()` | Lift the pen — move without drawing |
| `turtle.pendown()` | Put the pen down — draw when moving |
| `turtle.goto(x, y)` | Jump to coordinates (x, y) |
| `turtle.speed(5)` | Set speed (1=slow, 10=fast, 0=instant) |
| `turtle.done()` | Keep window open |

---

## 5. Drawing a Square

A square has 4 equal sides and 4 right angles (90°).

```python
import turtle

turtle.speed(3)

# Draw a square: forward 100, turn right 90, repeat 4 times
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.done()
```

Or using a loop (much cleaner!):

```python
import turtle

turtle.speed(3)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()
```

---

## 6. `penup()` and `pendown()`

Use `penup()` to move without drawing, then `pendown()` to start drawing again.

```python
import turtle

turtle.forward(100)     # draw a line
turtle.penup()          # lift the pen
turtle.forward(50)      # move without drawing
turtle.pendown()        # put pen down
turtle.forward(100)     # draw another line

turtle.done()
```

---

## 7. `goto(x, y)` — Jump to a Position

```python
import turtle

turtle.penup()
turtle.goto(100, 0)     # jump to (100, 0)
turtle.pendown()
turtle.goto(100, 100)   # draw a line to (100, 100)

turtle.done()
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| turtle | con rùa | The drawing cursor in the turtle module |
| module | mô-đun | A collection of Python tools you can import |
| import | nhập | Load a module so you can use its tools |
| forward | tiến | Move the turtle forward |
| backward | lùi | Move the turtle backward |
| turn | quay | Change the direction the turtle faces |
| angle | góc | The amount of rotation in degrees |
| degree | độ | Unit of angle measurement |
| pen | bút | The drawing tool the turtle carries |
| coordinate | tọa độ | A position described by x and y values |
| x-axis | trục x | The horizontal axis |
| y-axis | trục y | The vertical axis |
| origin | gốc tọa độ | The center point (0, 0) |
| pixel | điểm ảnh | One dot on the screen |
| clockwise | theo chiều kim đồng hồ | Turning in the direction clock hands move |
| counterclockwise | ngược chiều kim đồng hồ | Turning opposite to clock hands |

---

## 9. Summary

✅ `import turtle` loads the turtle module.
✅ The turtle starts at (0, 0) facing right.
✅ `forward(n)` moves n pixels forward; `right(d)` turns d degrees clockwise.
✅ `penup()` lifts the pen (no drawing); `pendown()` puts it back.
✅ `goto(x, y)` jumps to any position.
✅ Always end with `turtle.done()` to keep the window open.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Draw a Line**

Draw a horizontal line 150 pixels long.

- **Input:** None.
- **Output:** A horizontal line 150 pixels long drawn on screen.

---

**Exercise E2. Draw a Square**

Draw a square with side length 100 pixels.

- **Input:** None.
- **Output:** A square with side 100 pixels.

---

**Exercise E3. Draw a Triangle**

Draw an equilateral triangle with side length 100 pixels. (Hint: turn 120 degrees each time.)

- **Input:** None.
- **Output:** An equilateral triangle with side 100 pixels.

---

**Exercise E4. Two Separate Lines**

Draw a line, lift the pen, move forward, then draw another line. The two lines should not be connected.

- **Input:** None.
- **Output:** Two separate horizontal lines with a gap between them.

---

**Exercise E5. Draw a Cross (+)**

Use `goto()` to draw a plus sign (+) centered at the origin. Each arm is 80 pixels long.

- **Input:** None.
- **Output:** A plus sign (+) with arms of 80 pixels.

---

**Exercise E6. Draw a Rectangle**

Draw a rectangle that is 200 pixels wide and 100 pixels tall.

- **Input:** None.
- **Output:** A rectangle 200×100 pixels.

---

**Exercise E7. Draw the Letter L**

Draw the letter "L" using turtle. The vertical part is 100 pixels tall, the horizontal part is 60 pixels wide.

- **Input:** None.
- **Output:** The letter "L" drawn with turtle lines.

---

### 🟡 Medium

---

**Exercise M1. Draw a Pentagon**

Draw a regular pentagon (5 sides, each 100 pixels). The exterior angle of a pentagon is 72°.

- **Input:** None.
- **Output:** A regular pentagon.

---

**Exercise M2. Draw a Hexagon**

Draw a regular hexagon (6 sides, each 80 pixels). The exterior angle is 60°.

- **Input:** None.
- **Output:** A regular hexagon.

---

**Exercise M3. Draw a Staircase**

Draw a staircase going up-right with 4 steps. Each step is 40 pixels wide and 40 pixels tall.

- **Input:** None.
- **Output:** A staircase with 4 steps.

---

**Exercise M4. Draw a Grid**

Draw a 3×3 grid of squares, each 60 pixels. Use `penup()` and `goto()` to position each square.

- **Input:** None.
- **Output:** A 3×3 grid of squares.

---

**Exercise M5. Draw a Zigzag**

Draw a zigzag line with 5 peaks. Each segment is 60 pixels long, alternating up-right and down-right.

- **Input:** None.
- **Output:** A zigzag line with 5 peaks.

---

**Exercise M6. Draw a Diamond**

Draw a diamond shape (rotated square) with diagonal length 100 pixels. Start facing up-right (45°).

- **Input:** None.
- **Output:** A diamond (rotated square) shape.

---

**Exercise M7. Draw Your Initials**

Draw the first letter of your name using turtle lines. Use `penup()` and `pendown()` to lift the pen when needed.

- **Input:** None.
- **Output:** Your initial letter drawn with turtle.

---

### 🔴 Hard

---

**Exercise H1. Draw a Rectangle (200×100)**

Draw a rectangle with width 200 pixels and height 100 pixels, centered at the origin.

- **Input:** None.
- **Output:** A rectangle 200 pixels wide and 100 pixels tall, centered at the origin.

---

**Exercise H2. Draw a Right-Pointing Arrow**

Draw an arrow shape pointing to the right. The arrow has a rectangular body and a triangular head.

- **Input:** None.
- **Output:** An arrow shape pointing right, made of turtle lines.

---

**Exercise H3. Draw the Letter "L"**

Draw the letter "L" using turtle. The vertical stroke is 120 pixels tall, the horizontal stroke is 80 pixels wide.

- **Input:** None.
- **Output:** The letter "L" drawn with turtle lines.

---

**Exercise H4. Draw a Plus Sign (+)**

Draw a plus sign (+) centered at the origin. Each arm extends 80 pixels from the center.

- **Input:** None.
- **Output:** A plus sign with arms of 80 pixels, centered at (0, 0).

---

**Exercise H5. Draw a Staircase (3 Steps)**

Draw a staircase going up and to the right with 3 steps. Each step is 50 pixels wide and 50 pixels tall.

- **Input:** None.
- **Output:** A staircase with 3 steps going up-right.

---

**Exercise H6. Draw a House Outline**

Draw a house outline: a square base (100×100) with a triangular roof on top.

- **Input:** None.
- **Output:** A house shape with a square base and triangular roof.

---

**Exercise H7. Draw the Letter "T"**

Draw the letter "T" using turtle. The horizontal bar is 120 pixels wide, the vertical stroke is 100 pixels tall.

- **Input:** None.
- **Output:** The letter "T" drawn with turtle lines.
