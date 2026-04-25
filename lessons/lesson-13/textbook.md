# Lesson 13: Colors and Shapes 🎨

> **Goal:** Add colors and fills to turtle drawings using `pencolor()`, `fillcolor()`, `begin_fill()`, and `end_fill()`.

---

## 1. Adding Color to Your Turtle

You can change the color of the lines your turtle draws and the color it fills shapes with.

```python
import turtle

turtle.pencolor("red")      # line color = red
turtle.forward(100)

turtle.pencolor("blue")     # change line color to blue
turtle.forward(100)

turtle.done()
```

---

## 2. Color Names

Python turtle understands many color names:

| Color | Name |
|-------|------|
| 🔴 | `"red"` |
| 🔵 | `"blue"` |
| 🟢 | `"green"` |
| 🟡 | `"yellow"` |
| 🟠 | `"orange"` |
| 🟣 | `"purple"` |
| ⚫ | `"black"` |
| ⚪ | `"white"` |
| 🩷 | `"pink"` |
| 🩵 | `"cyan"` |

---

## 3. Filling Shapes

To fill a shape with color:
1. Set the fill color with `fillcolor()`.
2. Call `begin_fill()` before drawing.
3. Draw the shape.
4. Call `end_fill()` after drawing.

```python
import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()         # start filling
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()           # stop filling — fills the shape!

turtle.done()
```

---

## 4. `pencolor()` vs `fillcolor()`

| Command | What it changes |
|---------|----------------|
| `pencolor("red")` | The color of the lines drawn |
| `fillcolor("yellow")` | The color used to fill shapes |
| `turtle.color("red", "yellow")` | Set both at once: pen=red, fill=yellow |

---

## 5. Pen Size

`pensize(n)` sets the thickness of the line in pixels.

```python
import turtle

turtle.pensize(1)           # thin line
turtle.forward(100)

turtle.pensize(5)           # medium line
turtle.forward(100)

turtle.pensize(10)          # thick line
turtle.forward(100)

turtle.done()
```

---

## 6. Drawing a Circle

`turtle.circle(radius)` draws a circle with the given radius.

```python
import turtle

turtle.circle(50)           # draw a circle with radius 50

turtle.done()
```

You can also fill a circle:

```python
import turtle

turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.done()
```

---

## 7. Background Color

`turtle.bgcolor("color")` sets the background color of the window.

```python
import turtle

turtle.bgcolor("lightblue")
turtle.pencolor("white")
turtle.pensize(3)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| color | màu sắc | The visual appearance of a line or fill |
| fill | tô màu | Fill the inside of a shape with color |
| outline | đường viền | The border line of a shape |
| pencolor | màu bút | The color of the lines drawn |
| fillcolor | màu tô | The color used to fill a shape |
| pensize | độ dày bút | The thickness of the drawn line |
| radius | bán kính | The distance from the center to the edge of a circle |
| circle | hình tròn | A round shape |
| polygon | đa giác | A shape with straight sides |
| RGB | RGB | Red-Green-Blue color system |
| background | nền | The background color of the window |

---

## 9. Summary

✅ `pencolor("red")` sets the line color.
✅ `fillcolor("yellow")` sets the fill color.
✅ Use `begin_fill()` before and `end_fill()` after drawing to fill a shape.
✅ `pensize(n)` sets line thickness.
✅ `circle(radius)` draws a circle.
✅ `bgcolor("color")` sets the window background color.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Colored Lines**

Draw 4 lines, each a different color: red, blue, green, yellow. Each line is 100 pixels long, turning right 90° between lines.

- **Input:** None.
- **Output:** 4 colored lines forming a spiral-like shape.

---

**Exercise E2. Filled Square**

Draw a filled yellow square with a red border. Side length 100 pixels.

- **Input:** None.
- **Output:** A yellow square with a red outline.

---

**Exercise E3. Filled Circle**

Draw a filled blue circle with radius 60.

- **Input:** None.
- **Output:** A solid blue circle.

---

**Exercise E4. Thick Lines**

Draw a square with side 100 using a pensize of 5. Use any color you like.

- **Input:** None.
- **Output:** A square drawn with thick lines.

---

**Exercise E5. Colorful Triangle**

Draw a filled green triangle with a black border. Side length 100 pixels.

- **Input:** None.
- **Output:** A green filled triangle.

---

**Exercise E6. Background Color**

Set the background to dark blue. Draw a white square with side 100.

- **Input:** None.
- **Output:** A white square on a dark blue background.

---

**Exercise E7. Three Circles**

Draw 3 circles side by side (radius 40 each), colored red, green, and blue. Use `penup()` and `goto()` to position them.

- **Input:** None.
- **Output:** Three colored circles in a row.

---

### 🟡 Medium

---

**Exercise M1. Rainbow Lines**

Draw 7 lines, each a different rainbow color (red, orange, yellow, green, blue, indigo, violet). Each line is 100 pixels long, with a 10-pixel gap between them.

- **Input:** None.
- **Output:** 7 parallel colored lines.

---

**Exercise M2. Filled Rectangle**

Draw a filled orange rectangle (200 wide, 100 tall) with a purple border of pensize 3.

- **Input:** None.
- **Output:** An orange rectangle with a purple border.

---

**Exercise M3. Concentric Circles**

Draw 4 concentric circles (same center, different sizes) with radii 20, 40, 60, 80. Each a different color.

- **Input:** None.
- **Output:** 4 concentric circles in different colors.

---

**Exercise M4. Colorful Squares**

Draw 5 squares, each inside the previous one, each a different color. Sizes: 20, 40, 60, 80, 100.

- **Input:** None.
- **Output:** 5 nested squares in different colors.

---

**Exercise M5. Filled Pentagon**

Draw a filled purple pentagon with a black border. Side length 80 pixels.

- **Input:** None.
- **Output:** A purple filled pentagon.

---

**Exercise M6. Two Filled Shapes**

Draw a filled red circle (radius 50) on the left and a filled blue square (side 80) on the right.

- **Input:** None.
- **Output:** A red circle and a blue square side by side.

---

**Exercise M7. Color Wheel**

Draw 6 filled circles arranged in a ring (like a flower). Each circle has radius 30 and a different color. Use `goto()` to position each circle.

- **Input:** None.
- **Output:** 6 colored circles arranged in a ring.

---

### 🔴 Hard

---

**Exercise H1. Filled Red Circle**

Draw a filled red circle with radius 80, centered on screen.

- **Input:** None.
- **Output:** A solid red circle with radius 80.

---

**Exercise H2. Traffic Light**

Draw a traffic light: a black rectangle with 3 filled circles stacked vertically — red on top, yellow in the middle, green at the bottom.

- **Input:** None.
- **Output:** A traffic light with red, yellow, and green circles inside a black rectangle.

---

**Exercise H3. Filled House**

Draw a house with a blue filled square base (100×100) and a red filled triangle roof on top.

- **Input:** None.
- **Output:** A house with a blue body and red roof.

---

**Exercise H4. Rainbow Arcs**

Draw 7 arcs in rainbow colors (red, orange, yellow, green, blue, indigo, violet), each slightly larger than the previous, creating a rainbow effect.

- **Input:** None.
- **Output:** 7 colored arcs forming a rainbow shape.

---

**Exercise H5. Smiley Face**

Draw a smiley face: a large yellow filled circle, two small black filled circles for eyes, and a red arc for the smile.

- **Input:** None.
- **Output:** A smiley face with yellow face, black eyes, and red smile.

---

**Exercise H6. Flower**

Draw a flower with 6 filled circles arranged in a ring (petals), each with radius 40, in alternating colors. Add a small yellow circle in the center.

- **Input:** None.
- **Output:** A flower shape with 6 colored petals and a yellow center.

---

**Exercise H7. Vietnamese Flag**

Draw the Vietnamese flag: a red filled rectangle (200×130) with a yellow 5-pointed star outline in the center.

- **Input:** None.
- **Output:** A red rectangle with a yellow star outline in the center.
