# Lesson 17: Turtle Art Project 🖼️

> **Goal:** Combine ALL turtle skills into a creative drawing project. Plan your artwork, use variables for sizes, loops for repetition, and comments to explain your code.

---

## 1. Setting Up Your Canvas

Before drawing, set up the window with a title, size, and background color.

```python
import turtle

turtle.title("My Artwork")          # set the window title
turtle.setup(width=800, height=600) # set window size in pixels
turtle.bgcolor("white")             # set background color
turtle.speed(0)                     # fastest speed
```

`turtle.setup(800, 600)` makes an 800×600 pixel window.
`turtle.title("My Artwork")` shows text in the title bar.

---

## 2. Planning Your Drawing

Before writing code, sketch your drawing on paper:

1. What is the background color?
2. What elements will you draw? (shapes, patterns, characters)
3. Where will each element be positioned? (use coordinates)
4. What colors will you use?
5. Which parts repeat? (use loops)

**Example plan:**
```
Canvas: 800×600, background = "navy"
Elements:
  - 20 white stars scattered across the top half
  - A yellow moon at (200, 150)
  - A city skyline at the bottom (5 buildings)
```

---

## 3. Using Variables for Sizes

Store sizes and positions in variables so you can adjust them easily.

```python
import turtle

# --- Configuration variables ---
sky_color = "navy"
star_size = 6
moon_radius = 40
moon_x = 200
moon_y = 150

turtle.bgcolor(sky_color)

# Draw moon
turtle.penup()
turtle.goto(moon_x, moon_y - moon_radius)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(moon_radius)
turtle.end_fill()

turtle.done()
```

If you want a bigger moon, just change `moon_radius = 60`. No need to hunt through the code!

---

## 4. Grid Art with Nested Loops

Create a colorful grid using nested loops.

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
size = 40       # size of each square
cols = 8        # number of columns
rows = 6        # number of rows

for row in range(rows):
    for col in range(cols):
        x = -160 + col * size
        y = 120 - row * size
        color = colors[(row + col) % len(colors)]

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()

turtle.update()
turtle.done()
```

---

## 5. Simple Mandala

A mandala is made by rotating a shape many times around the center.

```python
import turtle

turtle.speed(0)
turtle.tracer(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
num_petals = 12
petal_size = 80

for i in range(num_petals):
    turtle.pencolor(colors[i % len(colors)])
    turtle.fillcolor(colors[i % len(colors)])
    turtle.begin_fill()
    # Draw one petal (a small circle)
    turtle.circle(petal_size / 2, 60)
    turtle.left(120)
    turtle.circle(petal_size / 2, 60)
    turtle.left(120)
    turtle.end_fill()
    turtle.right(360 / num_petals)  # rotate for next petal

turtle.update()
turtle.done()
```

---

## 6. Landscape

Draw mountains, sky, and a sun for a landscape scene.

```python
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor("skyblue")

# Ground
turtle.penup()
turtle.goto(-400, -150)
turtle.pendown()
turtle.fillcolor("darkgreen")
turtle.begin_fill()
turtle.goto(400, -150)
turtle.goto(400, -300)
turtle.goto(-400, -300)
turtle.goto(-400, -150)
turtle.end_fill()

# Mountain (triangle)
turtle.penup()
turtle.goto(-200, -150)
turtle.pendown()
turtle.fillcolor("gray")
turtle.begin_fill()
turtle.goto(0, 150)
turtle.goto(200, -150)
turtle.goto(-200, -150)
turtle.end_fill()

# Sun
turtle.penup()
turtle.goto(250, 80)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.update()
turtle.done()
```

---

## 7. Vocabulary

| English | Vietnamese | Meaning |
|---------|-----------|---------|
| project | dự án | A bigger task with a goal and plan |
| plan | kế hoạch | Decide what to do before starting |
| organize | tổ chức | Arrange code in a clear, logical order |
| variable | biến | A named box that stores a value |
| reuse | tái sử dụng | Use the same code or idea again |
| comment | ghi chú | A note in code that explains what it does |
| title | tiêu đề | The text shown in the window title bar |
| setup | thiết lập | Configure the window size and properties |
| canvas | khung vẽ | The drawing area (the turtle window) |
| artwork | tác phẩm | A finished creative drawing |

---

## 8. Summary

✅ `turtle.title("text")` sets the window title.
✅ `turtle.setup(width, height)` sets the window size.
✅ Use variables for sizes and positions — easy to adjust.
✅ Use nested loops for grids and repeated patterns.
✅ Use `turtle.tracer(0)` + `turtle.update()` for fast drawing.
✅ Plan your drawing before coding: sketch, list elements, note positions.
✅ Comment your code so others (and future you) can understand it.

---

## 9. Homework

### 🟢 Easy

---

**Exercise E1. Window Setup**

Write a program that sets up a turtle window with:
- Title: `"My Canvas"`
- Size: 600×400 pixels
- Background color: `"lightyellow"`

Then draw a filled blue circle (radius 40) in the center.

- **Input:** None.
- **Output:** A yellow canvas with a blue circle in the center.

---

**Exercise E2. Colorful Row of Squares**

Draw a row of 6 squares (side 50) side by side, starting at `(-150, -25)`. Use 6 different colors: red, orange, yellow, green, blue, purple.

- **Input:** None.
- **Output:** A row of 6 colorful squares.

---

**Exercise E3. Column of Circles**

Draw a column of 5 circles (radius 25) stacked vertically, centered at x=0. Use 5 different colors.

- **Input:** None.
- **Output:** A vertical column of 5 colored circles.

---

**Exercise E4. Checkerboard (4×4)**

Draw a 4×4 checkerboard using black and white squares (size 40). Use `(row + col) % 2` to alternate colors.

- **Input:** None.
- **Output:** A 4×4 checkerboard pattern.

---

**Exercise E5. Star Field**

Draw 15 white dots of size 6 at these positions on a dark blue background:
`(-200,150), (-100,180), (0,160), (100,140), (200,170), (-150,80), (-50,100), (50,90), (150,110), (250,80), (-220,30), (-80,50), (30,40), (130,20), (220,60)`.

- **Input:** None.
- **Output:** A dark blue sky with 15 white stars.

---

**Exercise E6. Rainbow Stripes**

Draw 7 horizontal stripes (each 400 wide, 40 tall) using rainbow colors: red, orange, yellow, green, blue, indigo, violet. Start from y=140 going down.

- **Input:** None.
- **Output:** A rainbow flag pattern.

---

**Exercise E7. Rotating Squares (6 squares)**

Draw 6 squares (side 80), each rotated 30° more than the previous. Use 6 different colors.

- **Input:** None.
- **Output:** 6 overlapping colored squares forming a star-like pattern.

---

### 🟡 Medium

---

**Exercise M1. Grid Art (4×4)**

Draw a 4×4 grid of squares (size 50). Color each square using `colors[(row + col) % 4]` where colors = `["red", "blue", "yellow", "green"]`.

- **Input:** None.
- **Output:** A 4×4 colorful grid.

---

**Exercise M2. Mandala (8 petals)**

Draw a mandala with 8 petals. Each petal is a small circle (radius 30). Rotate 45° between petals. Use 4 colors cycling.

- **Input:** None.
- **Output:** A mandala with 8 colored petals.

---

**Exercise M3. Mountain Landscape**

Draw a landscape with: sky blue background, a green ground rectangle, one gray mountain triangle, and a yellow sun circle.

- **Input:** None.
- **Output:** A mountain landscape scene.

---

**Exercise M4. Abstract Spiral Art**

Draw 36 squares (side 100), each rotated 10° more than the previous. Use 6 colors cycling. Use `tracer(0)`.

- **Input:** None.
- **Output:** An abstract pattern of overlapping colored squares.

---

**Exercise M5. City Skyline**

Draw a city skyline: dark blue background, 5 buildings of different heights (use a list of heights), all filled with gray. Add yellow dot windows on each building.

- **Input:** None.
- **Output:** A city skyline at night.

---

**Exercise M6. Flower Garden**

Draw 5 flowers in a row. Each flower has: a green stem line, a yellow center dot, and 6 colored petals (use a loop). Space them 80 pixels apart.

- **Input:** None.
- **Output:** A row of 5 flowers.

---

**Exercise M7. Concentric Circles**

Draw 8 concentric circles (circles with the same center) with radii 20, 40, 60, 80, 100, 120, 140, 160. Use 8 different colors. Center at `(0, 0)`.

- **Input:** None.
- **Output:** 8 concentric colored circles.

---

### 🔴 Hard

---

**Exercise H1. Clock Face**

*Draw a clock face.*

Draw a clock face that includes:
- A large white filled circle (radius 120) with a black border.
- 12 hour marks: short thick lines at every 30° around the edge.
- The numbers 12, 3, 6, 9 placed at the correct positions.
- A center dot.

- **Input:** None.
- **Output:** A clock face with 12 hour marks and 4 numbers.

---

**Exercise H2. Chessboard (8×8)**

*Draw a full chessboard.*

Draw an 8×8 chessboard where:
- Each square is 50×50 pixels.
- Squares alternate between black and white based on `(row + col) % 2`.
- The board is centered on screen.

- **Input:** None.
- **Output:** A full 8×8 chessboard with alternating black and white squares.

---

**Exercise H3. Bar Chart**

*Draw a bar chart.*

Draw a bar chart with 5 bars representing values `[80, 120, 60, 150, 100]`:
- Each bar is 40 pixels wide, spaced 20 pixels apart.
- Bar height = value (in pixels).
- Use 5 different colors for the bars.
- Draw a horizontal baseline.
- Label each bar with its value above it.

- **Input:** None.
- **Output:** A bar chart with 5 colored bars and value labels.

---

**Exercise H4. Spiral Galaxy**

*Draw a spiral galaxy.*

Draw a spiral galaxy with 150 dots:
- Each dot is placed at distance `i * 2` from center.
- Each dot is rotated by `137.5° × i` (golden angle).
- Dot size decreases from 8 to 2 as i increases.
- Use colors cycling through `["yellow", "white", "lightyellow"]`.

- **Input:** None.
- **Output:** A spiral galaxy pattern of colored dots.

---

**Exercise H5. City Skyline (5+ buildings)**

*Draw a detailed city skyline.*

Draw a city skyline with at least 5 buildings:
- Dark blue or black background.
- Buildings of different widths and heights, filled with dark gray.
- Yellow dot windows on each building (use nested loops).
- A moon or stars in the sky.

- **Input:** None.
- **Output:** A detailed night city skyline.

---

**Exercise H6. Butterfly**

*Draw a symmetric butterfly.*

Draw a butterfly with:
- Two left wings (filled with one color) and two right wings (filled with another color), symmetric about the vertical center axis.
- Each wing is an ellipse-like shape made with `circle()` arcs.
- A body (vertical oval or rectangle) in the center.
- Antennae (two lines with dots at the tips).

- **Input:** None.
- **Output:** A symmetric butterfly with colored wings.

---

**Exercise H7. Kaleidoscope Pattern**

*Draw a kaleidoscope.*

Draw a kaleidoscope pattern:
- Draw one colored triangle (filled).
- Rotate by 30° and draw another triangle in a different color.
- Repeat for a total of 12 triangles (full 360°).
- Use 6 colors cycling (each color used twice).
- Use `tracer(0)` for fast drawing.

- **Input:** None.
- **Output:** A kaleidoscope pattern of 12 overlapping colored triangles.
