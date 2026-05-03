# Lesson 30: Functions + Turtle 🐢

> **Goal:** Draw shapes with functions, make reusable drawing blocks, and use parameters for size and color.

---

## 1. Why Use Functions with Turtle?

Without functions, drawing the same shape multiple times means repeating the same code. With functions, you write the drawing code once and call it with different sizes and colors!

```python
# Without functions — messy!
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)

# With functions — clean!
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

draw_square(80)
```

---

## 2. Draw a Square with a Size Parameter

```python
import turtle

t = turtle.Turtle()

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

# Draw squares of different sizes
draw_square(50)
draw_square(100)
draw_square(150)

turtle.done()
```

---

## 3. Move Without Drawing

```python
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
```

---

## 4. Draw with Color Parameters

```python
def draw_filled_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

draw_filled_square(60, "red")
draw_filled_square(80, "blue")
```

---

## 5. Draw a Regular Polygon

```python
def draw_polygon(sides, size):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)

draw_polygon(3, 80)   # triangle
draw_polygon(5, 60)   # pentagon
draw_polygon(6, 50)   # hexagon
```

---

## 6. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| reusable | có thể tái sử dụng | Can be used many times |
| parameter | tham số | A variable that receives a value |
| argument | đối số | The value passed to a function |
| modular | mô-đun hóa | Organized into separate functions |
| drawing | vẽ | Creating shapes with turtle |
| function | hàm | A named block of reusable code |
| call | gọi | Run a function |
| scene | cảnh | A complete picture made of multiple shapes |

---

## 7. Summary

✅ Functions make turtle code clean and reusable.
✅ `def draw_square(size):` draws a square of any size.
✅ `def draw_polygon(sides, size):` draws any regular polygon.
✅ Use `t.penup()` / `t.pendown()` to move without drawing.
✅ Pass color as a parameter for flexible drawing.

---

## 8. Homework

### 🟢 Easy

---

**Exercise E1. Draw Three Squares**

Write a function `draw_square(size)`. Draw 3 squares of sizes 50, 80, and 110 at different positions.

- **Input:** None.
- **Output:** Three squares of different sizes on screen.

---

**Exercise E2. Draw Colored Square**

Write a function `draw_colored_square(size, color)`. Draw a filled square of size 70 in red, then one in blue.

- **Input:** None.
- **Output:** Two filled squares of different colors.

---

**Exercise E3. Draw Triangle**

Write a function `draw_triangle(size)`. Draw 3 triangles of sizes 60, 90, and 120.

- **Input:** None.
- **Output:** Three triangles of different sizes.

---

**Exercise E4. Draw Polygon**

Write a function `draw_polygon(sides, size)`. Draw a triangle (3 sides), square (4), pentagon (5), and hexagon (6), each with size 60.

- **Input:** None.
- **Output:** Four different polygons.

---

**Exercise E5. Move and Draw**

Write a function `move_to(x, y)` and a function `draw_square(size)`. Draw squares at positions (-150, 0), (0, 0), and (150, 0).

- **Input:** None.
- **Output:** Three squares in a row.

---

**Exercise E6. Draw Circle**

Write a function `draw_circle(radius, color)`. Draw 3 circles of different radii and colors.

- **Input:** None.
- **Output:** Three circles of different sizes and colors.

---

**Exercise E7. Draw Star**

Write a function `draw_star(size)`. A 5-pointed star: repeat 5 times (forward size, right 144). Draw 2 stars.

- **Input:** None.
- **Output:** Two stars.

---

### 🟡 Medium

---

**Exercise M1. Row of Squares**

Write `draw_square(size, color)`. Draw 5 squares in a row, each a different color.

- **Input:** None.
- **Output:** 5 colored squares in a horizontal row.

---

**Exercise M2. Nested Squares**

Write `draw_square(size)`. Draw 5 squares centered at the same point, each 20 pixels larger than the previous.

- **Input:** None.
- **Output:** 5 concentric squares.

---

**Exercise M3. Colorful Polygons**

Write `draw_polygon(sides, size, color)`. Draw a triangle (red), square (blue), pentagon (green), hexagon (yellow).

- **Input:** None.
- **Output:** 4 colored polygons.

---

**Exercise M4. Simple House**

Write `draw_house(x, y, size)` that draws a house (a square body + a triangle roof). Draw 2 houses.

- **Input:** None.
- **Output:** 2 houses side by side.

---

**Exercise M5. Simple Tree**

Write `draw_tree(x, y, height)` that draws a tree (a triangle top + a rectangle trunk). Draw 3 trees.

- **Input:** None.
- **Output:** 3 trees of different heights.

---

**Exercise M6. Spiral Squares**

Write `draw_square(size)`. Draw 10 squares, each rotated 36 degrees from the previous, creating a spiral effect.

- **Input:** None.
- **Output:** A spiral of squares.

---

**Exercise M7. Smiley Face**

Write `draw_face(x, y, size)` that draws a circle face with two dot eyes and a smile arc. Draw 2 faces.

- **Input:** None.
- **Output:** 2 smiley faces.

---

### 🔴 Hard

---

**Exercise H1. Five Squares**

Write `draw_square(size, color)`. Draw 5 squares of sizes 40, 60, 80, 100, 120 in colors red, orange, yellow, green, blue.

- **Input:** None.
- **Output:** 5 squares of different sizes and colors arranged on screen.

---

**Exercise H2. Polygon Row**

Write `draw_regular_polygon(n, size)`. Draw a triangle, square, pentagon, and hexagon in a row (each separated by 120 pixels).

- **Input:** None.
- **Output:** 4 polygons in a horizontal row.

---

**Exercise H3. Three Stars**

Write `draw_star(size, color)`. Draw 3 stars of sizes 40, 70, 100 in different colors.

- **Input:** None.
- **Output:** 3 stars of different sizes and colors.

---

**Exercise H4. Three Houses**

Write `draw_house(x, y, size)`. Draw 3 houses side by side at x = -150, 0, 150.

- **Input:** None.
- **Output:** 3 houses in a row.

---

**Exercise H5. Row of Trees**

Write `draw_tree(x, y, height)`. Draw 4 trees of heights 60, 80, 100, 120 in a row.

- **Input:** None.
- **Output:** 4 trees of different heights in a row.

---

**Exercise H6. Three Faces**

Write `draw_face(x, y, size)`. Draw 3 faces of sizes 40, 60, 80 at different positions.

- **Input:** None.
- **Output:** 3 smiley faces of different sizes.

---

**Exercise H7. Flower Garden**

Write `draw_flower(x, y, petals, color)` that draws a flower with the given number of petals and color. Draw 5 flowers with different petal counts and colors.

- **Input:** None.
- **Output:** A garden with 5 flowers.
