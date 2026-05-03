# Lesson 15: Spirals and Patterns 🌀

> **Goal:** Create beautiful spiral patterns by combining growing distances, rotating angles, and color cycling.

---

## 1. The Square Spiral

A square spiral grows by increasing the forward distance each step.

```python
import turtle

turtle.speed(0)

distance = 5
for i in range(50):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 3

turtle.done()
```

Each side is 3 pixels longer than the previous. The result is a growing square spiral.

---

## 2. Color Cycling

Use a list of colors and cycle through them with `i % len(colors)`.

```python
import turtle

turtle.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = 5

for i in range(60):
    turtle.pencolor(colors[i % len(colors)])   # cycle through colors
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 3

turtle.done()
```

`i % 6` gives: 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, ... — it cycles!

---

## 3. Rotating Squares

Draw many squares, each rotated a little more than the previous.

```python
import turtle

turtle.speed(0)

for i in range(36):
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)    # rotate 10 degrees before next square

turtle.done()
```

36 squares × 10° = 360° — a full rotation!

---

## 4. Galaxy Spiral

A galaxy spiral uses a small turn angle (not 90°) to create a smooth curve.

```python
import turtle

turtle.speed(0)

distance = 1
for i in range(200):
    turtle.forward(distance)
    turtle.right(30)        # small angle = smooth curve
    distance = distance + 0.5

turtle.done()
```

---

## 5. Fast Drawing with `tracer()`

For complex drawings, use `turtle.tracer(0)` to skip animation and `turtle.update()` to show the final result instantly.

```python
import turtle

turtle.tracer(0)    # turn off animation

# ... all your drawing code here ...

turtle.update()     # show the final drawing
turtle.done()
```

---

## 6. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| spiral | xoắn ốc | A shape that grows outward as it turns |
| rotate | xoay | Turn by an angle |
| cycle | chu kỳ | Repeat a sequence over and over |
| pattern | mẫu hình | A repeated visual design |
| increment | tăng dần | Increase by a fixed amount each step |
| tracer | bộ theo dõi | Controls animation speed in turtle |
| update | cập nhật | Refresh the screen to show new drawing |
| aesthetic | thẩm mỹ | Visually pleasing |

---

## 7. Summary

✅ Spiral: increase `distance` each iteration.
✅ Color cycling: `colors[i % len(colors)]` cycles through a list.
✅ Rotating shapes: draw a shape, then `right(small_angle)` before the next.
✅ `turtle.tracer(0)` + `turtle.update()` for instant drawing.
✅ Combine growing + rotating + color cycling for beautiful art.

---

## 8. Homework

### 🟢 Easy

---

**Exercise E1. Square Spiral (10 steps)**

Draw a square spiral with 10 iterations. Start with side 10, increase by 10 each step.

- **Input:** None.
- **Output:** A square spiral with 10 steps.

---

**Exercise E2. Triangle Spiral (10 steps)**

Draw a triangle spiral with 10 iterations. Start with side 10, increase by 10 each step. Turn 120° each time.

- **Input:** None.
- **Output:** A triangle spiral with 10 steps.

---

**Exercise E3. Color Square Spiral**

Draw a square spiral with 20 iterations using 4 colors cycling (red, blue, green, yellow). Side starts at 10, grows by 5.

- **Input:** None.
- **Output:** A colorful square spiral.

---

**Exercise E4. Rotating Squares (4 squares)**

Draw 4 squares (side 80), each rotated 45° more than the previous.

- **Input:** None.
- **Output:** 4 overlapping squares, each rotated 45°.

---

**Exercise E5. Galaxy Spiral**

Draw a galaxy spiral: 100 iterations, start with distance 1, increase by 0.5 each step, turn 30° each step.

- **Input:** None.
- **Output:** A smooth galaxy-like spiral.

---

**Exercise E6. Color Triangle Spiral**

Draw a triangle spiral with 30 iterations using 3 colors cycling (red, green, blue). Side starts at 5, grows by 3.

- **Input:** None.
- **Output:** A colorful triangle spiral.

---

**Exercise E7. Starburst Lines**

Draw 12 lines from the center, each 120 pixels long, evenly spaced (30° apart). Each line a different color.

- **Input:** None.
- **Output:** A starburst with 12 colored lines.

---

### 🟡 Medium

---

**Exercise M1. Double Spiral**

Draw two square spirals: one turning right (clockwise) and one turning left (counter-clockwise), both starting from the center.

- **Input:** None.
- **Output:** Two spirals going in opposite directions.

---

**Exercise M2. Rotating Triangles**

Draw 12 equilateral triangles (side 80), each rotated 30° more than the previous.

- **Input:** None.
- **Output:** 12 overlapping triangles forming a star-like pattern.

---

**Exercise M3. Rainbow Square Spiral**

Draw a square spiral with 42 iterations using 6 rainbow colors cycling. Side starts at 5, grows by 5.

- **Input:** None.
- **Output:** A rainbow-colored square spiral.

---

**Exercise M4. Hexagon Spiral**

Draw a hexagon spiral: 20 iterations, each hexagon slightly larger (side grows by 5 from 20), each rotated 5° more.

- **Input:** None.
- **Output:** A spiral of hexagons.

---

**Exercise M5. Web Pattern**

Draw a web pattern: lines from the center at every 10°, each 150 pixels long. Then draw concentric circles at radii 50, 100, 150.

- **Input:** None.
- **Output:** A spider web pattern.

---

**Exercise M6. Fibonacci Squares**

Draw squares of sizes 1, 1, 2, 3, 5, 8, 13, 21 (Fibonacci numbers × 10 pixels). Arrange them in an L-shape pattern.

- **Input:** None.
- **Output:** Fibonacci squares arranged in a pattern.

---

**Exercise M7. Color Polygon Spiral**

Draw 20 pentagons, each rotated 7° more and 8 pixels larger than the previous. Cycle through 5 colors.

- **Input:** None.
- **Output:** A spiral of colored pentagons.

---

### 🔴 Hard

---

**Exercise H1. Square Spiral (30 iterations)**

Draw a square spiral with 30 iterations. Side starts at 10, grows by 5 each step. Use `tracer(0)` for fast drawing.

- **Input:** None.
- **Output:** A square spiral with 30 steps, side growing from 10 to 155.

---

**Exercise H2. Triangle Spiral (20 iterations)**

Draw a triangle spiral with 20 iterations. Side starts at 10, grows by 8 each step. Turn 120° each time.

- **Input:** None.
- **Output:** A triangle spiral with 20 steps.

---

**Exercise H3. Rotating Squares (20 squares)**

Draw 20 squares (side 100), each rotated 18° more than the previous. Use `tracer(0)`.

- **Input:** None.
- **Output:** 20 overlapping squares, each rotated 18°, forming a circular pattern.

---

**Exercise H4. Color Spiral (6 colors)**

Draw a square spiral with 60 iterations using 6 colors cycling (red, orange, yellow, green, blue, purple). Side starts at 5, grows by 4. Use `tracer(0)`.

- **Input:** None.
- **Output:** A colorful square spiral with 6 cycling colors.

---

**Exercise H5. Sunflower Spiral**

Draw a sunflower spiral using the golden angle (≈ 137.5°). Place 100 dots, each at distance `i * 4` from center, rotated by 137.5° × i. Use `turtle.dot(8)` to draw each dot.

- **Input:** None.
- **Output:** A sunflower-like spiral of 100 dots.

---

**Exercise H6. Web Pattern**

Draw a spider web: 18 lines from the center at every 20°, each 150 pixels long. Then draw 4 concentric circles (radii 40, 80, 120, 150) connecting the lines.

- **Input:** None.
- **Output:** A spider web with 18 spokes and 4 rings.

---

**Exercise H7. Fibonacci Spiral**

Draw a Fibonacci spiral approximation using squares of sizes 1, 1, 2, 3, 5, 8, 13, 21 (multiplied by 10 pixels). Draw each square and a quarter-circle arc inside it to approximate the spiral.

- **Input:** None.
- **Output:** A Fibonacci spiral made of squares with quarter-circle arcs.
