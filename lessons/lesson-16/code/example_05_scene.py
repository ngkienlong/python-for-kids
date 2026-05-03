"""
Lesson 16 - Example 05: Complete Scene
Combines house + tree + sun + sky + ground
"""
import turtle
import math

turtle.speed(0)
turtle.tracer(0)            # turn off animation for fast drawing
turtle.title("My Scene")

# --- Background ---
turtle.bgcolor("lightblue")

# --- Ground (green rectangle) ---
turtle.penup()
turtle.goto(-400, -200)
turtle.pendown()
turtle.fillcolor("limegreen")
turtle.pencolor("limegreen")
turtle.begin_fill()
turtle.goto(400, -200)
turtle.goto(400, -100)
turtle.goto(-400, -100)
turtle.goto(-400, -200)
turtle.end_fill()

# --- Sun (circle + 8 rays) ---
cx, cy, r = 180, 130, 35
turtle.penup()
turtle.goto(cx, cy - r)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.pencolor("orange")
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

for i in range(8):
    angle = 90 + i * 45
    sx = cx + r * math.cos(math.radians(angle))
    sy = cy + r * math.sin(math.radians(angle))
    ex = cx + (r + 40) * math.cos(math.radians(angle))
    ey = cy + (r + 40) * math.sin(math.radians(angle))
    turtle.penup()
    turtle.goto(sx, sy)
    turtle.pendown()
    turtle.pencolor("orange")
    turtle.goto(ex, ey)

# --- House body ---
turtle.penup()
turtle.goto(-160, -100)
turtle.pendown()
turtle.fillcolor("lightyellow")
turtle.pencolor("black")
turtle.begin_fill()
for i in range(4):
    turtle.forward(110)
    turtle.left(90)
turtle.end_fill()

# --- House roof ---
turtle.fillcolor("firebrick")
turtle.begin_fill()
turtle.penup()
turtle.goto(-160, 10)
turtle.pendown()
turtle.goto(-50, 10)
turtle.goto(-105, 75)
turtle.goto(-160, 10)
turtle.end_fill()

# --- House door ---
turtle.penup()
turtle.goto(-120, -100)
turtle.pendown()
turtle.fillcolor("saddlebrown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(22)
    turtle.left(90)
    turtle.forward(38)
    turtle.left(90)
turtle.end_fill()

# --- Tree trunk ---
turtle.penup()
turtle.goto(60, -100)
turtle.pendown()
turtle.fillcolor("saddlebrown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(90)
turtle.end_fill()

# --- Tree canopy (triangle) ---
turtle.fillcolor("forestgreen")
turtle.begin_fill()
turtle.penup()
turtle.goto(30, -55)
turtle.pendown()
turtle.goto(110, -55)
turtle.goto(70, 30)
turtle.goto(30, -55)
turtle.end_fill()

turtle.update()             # show the finished drawing
turtle.hideturtle()
turtle.done()
