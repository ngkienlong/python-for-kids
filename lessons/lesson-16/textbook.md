# Lesson 16: Creative Drawing 🎨

> **Goal:** Combine all turtle skills to draw complete scenes — houses, trees, suns, and faces — by breaking drawings into logical parts.

---

## 1. Breaking a Drawing into Parts

Complex drawings are easier when you split them into small pieces.

A **house** = square body + triangle roof + rectangle door + square windows.
A **tree** = triangle canopy + rectangle trunk.
A **scene** = sky + ground + house + tree + sun.

Plan your drawing before you code!

```
Scene layout:
┌─────────────────────────────┐
│  ☀  (sun, top right)        │
│                             │
│  🏠  (house, center-left)   │
│  🌲  (tree, center-right)   │
│─────────────────────────────│  ← ground line
```

---

## 2. Using `penup()` and `goto()` to Position

Use `penup()` + `goto(x, y)` + `pendown()` to move to a new position without drawing a line.

```python
import turtle

turtle.penup()
turtle.goto(-100, 0)   # move to position (-100, 0)
turtle.pendown()
turtle.forward(80)     # draw from that position

turtle.done()
```

The turtle screen center is `(0, 0)`. Left is negative x, right is positive x, up is positive y, down is negative y.

---

## 3. Drawing a House

A house = square body + triangle roof.

```python
import turtle

# --- Draw the square body ---
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()

turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# --- Draw the triangle roof ---
turtle.penup()
turtle.goto(-50, 20)   # bottom-left corner of roof
turtle.pendown()

turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(50, 20)    # bottom-right
turtle.goto(0, 80)     # top (peak)
turtle.goto(-50, 20)   # back to start
turtle.end_fill()

turtle.done()
```

---

## 4. Drawing a Tree

A tree = green triangle canopy + brown rectangle trunk.

```python
import turtle

# --- Draw the trunk ---
turtle.penup()
turtle.goto(-10, -80)
turtle.pendown()

turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()

# --- Draw the canopy (triangle) ---
turtle.penup()
turtle.goto(-40, -40)
turtle.pendown()

turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(40, -40)
turtle.goto(0, 40)
turtle.goto(-40, -40)
turtle.end_fill()

turtle.done()
```

---

## 5. Drawing a Sun

A sun = yellow circle + rays drawn with a loop.

```python
import turtle

turtle.speed(0)

# --- Draw the circle ---
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# --- Draw 8 rays ---
for i in range(8):
    turtle.penup()
    turtle.goto(100, 130)   # start from center-top of sun
    turtle.pendown()
    turtle.setheading(90 + i * 45)   # point in 8 directions
    turtle.forward(50)

turtle.done()
```

---

## 6. Drawing a Face

A face = circle head + dot eyes + arc smile.

```python
import turtle

turtle.speed(1)

# --- Head ---
turtle.penup()
turtle.goto(0, -60)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

# --- Left eye ---
turtle.penup()
turtle.goto(-20, 20)
turtle.pendown()
turtle.dot(12, "black")

# --- Right eye ---
turtle.penup()
turtle.goto(20, 20)
turtle.pendown()
turtle.dot(12, "black")

# --- Smile (arc) ---
turtle.penup()
turtle.goto(-20, -10)
turtle.pendown()
turtle.setheading(-60)
turtle.circle(25, 120)   # draw 120-degree arc

turtle.done()
```

`turtle.circle(radius, extent)` draws an arc of `extent` degrees.

---

## 7. Combining into a Scene

Put all parts together with `goto()` to position each element.

```python
import turtle

turtle.speed(0)
turtle.bgcolor("lightblue")

# --- Ground ---
turtle.penup()
turtle.goto(-300, -100)
turtle.pendown()
turtle.pencolor("green")
turtle.pensize(3)
turtle.forward(600)

# --- Sun ---
turtle.penup()
turtle.goto(180, 80)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# --- House body ---
turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# --- House roof ---
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(50, 0)
turtle.goto(-50, 60)
turtle.goto(-150, 0)
turtle.end_fill()

turtle.done()
```

---

## 8. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| scene | cảnh | A complete picture with multiple elements |
| composition | bố cục | How elements are arranged in a picture |
| layer | lớp | One level of a drawing (background, foreground) |
| foreground | tiền cảnh | The front part of a scene |
| background | hậu cảnh | The back part of a scene |
| element | phần tử | One piece of a drawing (house, tree, sun) |
| position | vị trí | Where something is placed |
| coordinate | tọa độ | A pair (x, y) that describes a position |
| reuse | tái sử dụng | Use the same drawing steps again |
| decompose | phân tách | Break a complex thing into smaller parts |
| goto | đi đến | Move the turtle to a specific coordinate |
| setheading | đặt hướng | Point the turtle in a specific direction |

---

## 9. Summary

✅ Break complex drawings into parts: body, roof, trunk, canopy, rays.
✅ Use `penup()` + `goto(x, y)` + `pendown()` to position between parts.
✅ Use `goto(x, y)` to draw straight lines to specific points.
✅ Use `setheading(angle)` to point the turtle in any direction.
✅ Use `circle(r, extent)` to draw full circles or arcs.
✅ Combine all parts with a clear layout plan.

---

## 10. Homework

### 🟢 Easy

---

**Exercise E1. Square House Body**

Draw a filled square (side 100) with `fillcolor("lightyellow")` starting at position `(-50, -80)`.

- **Input:** None.
- **Output:** A filled yellow square on screen.

---

**Exercise E2. Triangle Roof**

Draw a filled red triangle as a roof. The three corners are at `(-50, 20)`, `(50, 20)`, and `(0, 80)`.

- **Input:** None.
- **Output:** A filled red triangle on screen.

---

**Exercise E3. Tree Trunk**

Draw a filled brown rectangle (width 20, height 40) starting at `(-10, -80)`.

- **Input:** None.
- **Output:** A filled brown rectangle on screen.

---

**Exercise E4. Yellow Sun Circle**

Draw a filled yellow circle with radius 40 at position `(150, 100)`.

- **Input:** None.
- **Output:** A filled yellow circle on screen.

---

**Exercise E5. Dot Eyes**

Draw two black dots: one at `(-20, 20)` and one at `(20, 20)`. Use `turtle.dot(12, "black")`.

- **Input:** None.
- **Output:** Two black dots on screen.

---

**Exercise E6. Green Ground Line**

Draw a green horizontal line from `(-300, -100)` to `(300, -100)` with `pensize(4)`.

- **Input:** None.
- **Output:** A thick green horizontal line on screen.

---

**Exercise E7. Blue Sky Background**

Set the background color to `"lightblue"` using `turtle.bgcolor("lightblue")`. Then draw a green ground line from `(-300, -100)` to `(300, -100)`.

- **Input:** None.
- **Output:** A light blue background with a green ground line.

---

### 🟡 Medium

---

**Exercise M1. House (Body + Roof)**

Draw a complete house: a filled yellow square body (side 100) at `(-50, -80)` and a filled red triangle roof with peak at `(0, 80)`.

- **Input:** None.
- **Output:** A house shape with yellow body and red roof.

---

**Exercise M2. Tree (Canopy + Trunk)**

Draw a complete tree: a filled brown rectangle trunk (20×40) at `(-10, -80)` and a filled green triangle canopy with corners at `(-40, -40)`, `(40, -40)`, `(0, 40)`.

- **Input:** None.
- **Output:** A tree with green canopy and brown trunk.

---

**Exercise M3. Sun with 8 Rays**

Draw a filled yellow circle (radius 30) at `(150, 100)`. Then draw 8 rays of length 50 pointing in 8 directions (every 45°).

- **Input:** None.
- **Output:** A sun with 8 rays.

---

**Exercise M4. Smiley Face**

Draw a smiley face: filled yellow circle (radius 60), two black dot eyes, and a smile arc.

- **Input:** None.
- **Output:** A smiley face on screen.

---

**Exercise M5. House with Door**

Draw a house (body + roof) and add a filled brown rectangle as a door (width 20, height 35) centered at the bottom of the house.

- **Input:** None.
- **Output:** A house with a door.

---

**Exercise M6. Sky and Ground**

Draw a scene with: light blue background, a green filled rectangle as ground (from y=-200 to y=-100, full width), and a yellow sun circle at `(150, 100)`.

- **Input:** None.
- **Output:** A sky-and-ground scene with a sun.

---

**Exercise M7. Two Trees**

Draw two trees side by side. First tree centered at x=50, second tree centered at x=150. Both have green canopy and brown trunk.

- **Input:** None.
- **Output:** Two trees on screen.

---

### 🔴 Hard

---

**Exercise H1. House with Door and Windows**

*Draw a complete house with details.*

Draw a house that includes:
- Filled yellow square body (side 120) starting at `(-60, -100)`.
- Filled red triangle roof with peak at `(0, 80)`.
- Filled brown rectangle door (width 25, height 40) centered at the bottom of the house.
- Two filled light-blue squares as windows (size 25×25), one on each side of the door.

- **Input:** None.
- **Output:** A house with a red roof, yellow walls, a brown door, and two blue windows.

---

**Exercise H2. Tree with Round Canopy**

*Draw a realistic-looking tree.*

Draw a tree that includes:
- Filled brown rectangle trunk (width 20, height 50) centered at `(0, -100)`.
- Filled green circle (radius 45) as the round canopy, centered above the trunk at `(0, 0)`.

- **Input:** None.
- **Output:** A tree with a round green canopy and a brown trunk.

---

**Exercise H3. Sun with 12 Rays**

*Draw a detailed sun.*

Draw a sun that includes:
- Filled yellow circle (radius 35) centered at `(150, 120)`.
- 12 rays of length 55, evenly spaced (every 30°), drawn from the edge of the circle outward.

- **Input:** None.
- **Output:** A bright sun with 12 rays pointing in all directions.

---

**Exercise H4. Robot Face**

*Draw a robot face.*

Draw a robot face that includes:
- Filled gray rectangle as the head (width 120, height 100) centered at `(0, 0)`.
- Two filled white squares as eyes (size 25×25), one on each side.
- A horizontal black line as the mouth.
- A vertical line as the antenna on top of the head, with a small circle at the top.

- **Input:** None.
- **Output:** A robot face with rectangular head, square eyes, line mouth, and antenna.

---

**Exercise H5. Simple Car**

*Draw a simple car.*

Draw a car that includes:
- Filled blue rectangle as the car body (width 160, height 60) starting at `(-80, -60)`.
- Filled dark-gray rectangle as the car cabin (width 100, height 50) centered on top of the body.
- Two filled black circles (radius 25) as wheels, positioned below the body.

- **Input:** None.
- **Output:** A simple car with a blue body, dark cabin, and two black wheels.

---

**Exercise H6. Night Scene**

*Draw a night scene.*

Draw a night scene that includes:
- Black background (`turtle.bgcolor("black")`).
- A filled yellow circle (radius 35) as the moon at `(150, 120)`.
- At least 10 white dots of varying sizes scattered across the sky as stars (use `turtle.dot()`).

- **Input:** None.
- **Output:** A night scene with a black sky, yellow moon, and white stars.

---

**Exercise H7. Garden Scene**

*Draw a complete garden scene.*

Draw a garden scene that includes:
- Light blue background.
- A filled green rectangle as the ground (full width, from y=-200 to y=-80).
- Three flowers, each made of: a green vertical line (stem), a yellow circle (center), and 6 colored petals (use a loop to draw petals around the center).
- Space the three flowers evenly across the scene.

- **Input:** None.
- **Output:** A garden with blue sky, green ground, and three colorful flowers.
