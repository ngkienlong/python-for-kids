# Lesson 14: Loops + Turtle = Magic ✨

> **Goal:** Use loops to draw regular polygons, stars, concentric circles, and spirals.

---

## 1. Drawing Any Regular Polygon

A **regular polygon** has all sides equal and all angles equal. The key formula is:

> **Exterior angle = 360 ÷ number of sides**

```python
import turtle

# Draw a regular polygon with n sides
n = 6   # hexagon
for i in range(n):
    turtle.forward(100)
    turtle.right(360 / n)   # exterior angle

turtle.done()
```

| Polygon | Sides | Exterior Angle |
|---------|-------|---------------|
| Triangle | 3 | 120° |
| Square | 4 | 90° |
| Pentagon | 5 | 72° |
| Hexagon | 6 | 60° |
| Octagon | 8 | 45° |

---

## 2. Drawing a 5-Pointed Star

A star uses a different angle: **144°** (not 72°).

```python
import turtle

for i in range(5):
    turtle.forward(100)
    turtle.right(144)

turtle.done()
```

Why 144°? Because 5 × 144 = 720 = 2 × 360. The turtle makes 2 full rotations to draw a star.

---

## 3. Concentric Circles

**Concentric circles** share the same center but have different sizes.

```python
import turtle

for r in range(20, 101, 20):    # radii: 20, 40, 60, 80, 100
    turtle.penup()
    turtle.goto(0, -r)          # position so circle is centered
    turtle.pendown()
    turtle.circle(r)

turtle.done()
```

> 💡 `turtle.circle(r)` starts drawing from the turtle's current position. To center the circle at (0,0), move to (0, -r) first.

---

## 4. Drawing a Spiral

A **spiral** grows larger with each step. Increase the forward distance each iteration.

```python
import turtle

distance = 5
for i in range(30):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5     # grow by 5 each step

turtle.done()
```

---

## 5. Many Polygons in a Row

```python
import turtle

turtle.speed(0)

shapes = [3, 4, 5, 6]   # triangle, square, pentagon, hexagon
x_positions = [-200, -80, 40, 160]

for idx in range(4):
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

## 6. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| polygon | đa giác | A shape with straight sides |
| regular | đều | All sides and angles are equal |
| exterior angle | góc ngoài | The angle you turn at each vertex |
| star | ngôi sao | A star shape drawn by skipping vertices |
| concentric | đồng tâm | Circles sharing the same center |
| spiral | xoắn ốc | A shape that grows outward as it turns |
| vertex | đỉnh | A corner point of a polygon |
| side | cạnh | One straight edge of a polygon |

---

## 7. Summary

✅ Regular polygon: `for i in range(n): forward(100); right(360/n)`.
✅ 5-pointed star: `for i in range(5): forward(100); right(144)`.
✅ Concentric circles: loop through radii, move to (0, -r) before each circle.
✅ Spiral: increase the forward distance each step.
✅ `turtle.speed(0)` draws instantly — useful for complex drawings.

---

## 8. Homework

### 🟢 Easy

---

**Exercise E1. Draw a Pentagon**

Draw a regular pentagon with side length 100 pixels.

- **Input:** None.
- **Output:** A regular pentagon.

---

**Exercise E2. Draw a Hexagon**

Draw a regular hexagon with side length 80 pixels.

- **Input:** None.
- **Output:** A regular hexagon.

---

**Exercise E3. Draw a 5-Pointed Star**

Draw a 5-pointed star with side length 100 pixels.

- **Input:** None.
- **Output:** A 5-pointed star.

---

**Exercise E4. Draw 3 Concentric Circles**

Draw 3 concentric circles with radii 30, 60, and 90.

- **Input:** None.
- **Output:** Three concentric circles.

---

**Exercise E5. Draw a Simple Spiral**

Draw a square spiral with 10 iterations. Start with side length 10, increase by 10 each step.

- **Input:** None.
- **Output:** A square spiral with 10 steps.

---

**Exercise E6. Draw an Octagon**

Draw a regular octagon (8 sides) with side length 70 pixels.

- **Input:** None.
- **Output:** A regular octagon.

---

**Exercise E7. Draw a Triangle, Square, Pentagon in a Row**

Draw a triangle, square, and pentagon side by side. Each has side length 60 pixels.

- **Input:** None.
- **Output:** Three shapes in a row.

---

### 🟡 Medium

---

**Exercise M1. Colored Polygon**

Draw a filled regular hexagon with a yellow fill and blue border. Side length 80 pixels.

- **Input:** None.
- **Output:** A filled yellow hexagon with blue border.

---

**Exercise M2. Colored Star**

Draw a filled 5-pointed star with a red fill and black border. Side length 100 pixels.

- **Input:** None.
- **Output:** A filled red star.

---

**Exercise M3. Concentric Colored Circles**

Draw 5 concentric circles with radii 20, 40, 60, 80, 100. Each circle a different color.

- **Input:** None.
- **Output:** 5 concentric circles in different colors.

---

**Exercise M4. Polygon Spiral**

Draw 10 squares, each slightly larger (side grows by 10 from 10 to 100), all starting from the same point.

- **Input:** None.
- **Output:** 10 squares of increasing size, creating a spiral effect.

---

**Exercise M5. Star Burst**

Draw 8 lines from the center, each 100 pixels long, evenly spaced (45° apart). Use a loop.

- **Input:** None.
- **Output:** 8 lines radiating from the center like a starburst.

---

**Exercise M6. Nested Polygons**

Draw a triangle, square, pentagon, hexagon, and heptagon (7 sides), all centered at the origin. Each has side length 80 pixels.

- **Input:** None.
- **Output:** 5 nested polygons of increasing sides.

---

**Exercise M7. Colorful Star**

Draw a 5-pointed star where each of the 5 sides is a different color.

- **Input:** None.
- **Output:** A 5-pointed star with 5 different colored sides.

---

### 🔴 Hard

---

**Exercise H1. Regular Hexagon**

Draw a filled regular hexagon with side length 100 pixels. Fill color: gold. Border color: dark orange.

- **Input:** None.
- **Output:** A filled gold hexagon with dark orange border.

---

**Exercise H2. 6-Pointed Star**

Draw a 6-pointed Star of David by drawing two overlapping equilateral triangles (one pointing up, one pointing down). Side length 100 pixels.

- **Input:** None.
- **Output:** A 6-pointed star made of two overlapping triangles.

---

**Exercise H3. 5 Concentric Squares**

Draw 5 concentric squares centered at the origin. The smallest has side 20, each subsequent one is 20 pixels larger (20, 40, 60, 80, 100).

- **Input:** None.
- **Output:** 5 concentric squares.

---

**Exercise H4. Spiral Square**

Draw a square spiral with 20 iterations. Start with side length 10, increase by 5 each step. Turn right 90° each time.

- **Input:** None.
- **Output:** A square spiral with 20 steps, growing outward.

---

**Exercise H5. Flower from Circles**

Draw a flower using 12 circles arranged in a ring. Each circle has radius 40. Use a loop and `math.cos`/`math.sin` to position each circle.

- **Input:** None.
- **Output:** A flower shape made of 12 circles in a ring.

---

**Exercise H6. Snowflake**

Draw a snowflake with 6 arms from the center. Each arm is 100 pixels long with two small branches (40 pixels each) at 60° angles near the tip.

- **Input:** None.
- **Output:** A snowflake with 6 arms and branches.

---

**Exercise H7. Color-Changing Polygon Spiral**

Draw 10 polygons (hexagons), each slightly larger (side grows by 10 from 30 to 120) and rotated by 6° more than the previous. Each polygon a different color.

- **Input:** None.
- **Output:** A spiral of colored hexagons, each rotated slightly more than the last.
