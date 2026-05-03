"""
Lesson 17 - Example 04: Landscape Scene
Draws mountains, sky, ground, and a sun
"""
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.title("Landscape")
turtle.setup(800, 600)

# --- Sky background ---
turtle.bgcolor("deepskyblue")

# --- Sun ---
sun_x = 250
sun_y = 150
sun_radius = 55

turtle.penup()
turtle.goto(sun_x, sun_y - sun_radius)
turtle.pendown()
turtle.fillcolor("gold")
turtle.pencolor("orange")
turtle.pensize(2)
turtle.begin_fill()
turtle.circle(sun_radius)
turtle.end_fill()

# --- Far mountain (lighter gray, drawn first so it appears behind) ---
turtle.penup()
turtle.goto(-300, -120)
turtle.pendown()
turtle.fillcolor("lightgray")
turtle.pencolor("lightgray")
turtle.begin_fill()
turtle.goto(0, 180)         # peak
turtle.goto(300, -120)
turtle.goto(-300, -120)
turtle.end_fill()

# --- Near mountain (darker gray) ---
turtle.penup()
turtle.goto(-350, -120)
turtle.pendown()
turtle.fillcolor("gray")
turtle.pencolor("gray")
turtle.begin_fill()
turtle.goto(-100, 100)      # peak
turtle.goto(150, -120)
turtle.goto(-350, -120)
turtle.end_fill()

# --- Ground ---
turtle.penup()
turtle.goto(-400, -300)
turtle.pendown()
turtle.fillcolor("darkgreen")
turtle.pencolor("darkgreen")
turtle.begin_fill()
turtle.goto(400, -300)
turtle.goto(400, -120)
turtle.goto(-400, -120)
turtle.goto(-400, -300)
turtle.end_fill()

# --- Snow on mountain peak ---
turtle.penup()
turtle.goto(-130, 60)
turtle.pendown()
turtle.fillcolor("white")
turtle.pencolor("white")
turtle.begin_fill()
turtle.goto(-100, 100)
turtle.goto(-70, 60)
turtle.goto(-130, 60)
turtle.end_fill()

turtle.update()
turtle.hideturtle()
turtle.done()
