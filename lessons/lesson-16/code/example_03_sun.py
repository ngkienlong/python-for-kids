"""
Lesson 16 - Example 03: Drawing a Sun
A sun = yellow filled circle + rays drawn with a loop
"""
import turtle
import math

turtle.speed(0)
turtle.title("Sun with Rays")

# Sun center position
cx = 150
cy = 120
radius = 35
ray_length = 55

# --- Draw the sun circle ---
turtle.penup()
turtle.goto(cx, cy - radius)    # goto() starts circle from bottom
turtle.pendown()

turtle.fillcolor("yellow")
turtle.pencolor("orange")
turtle.pensize(2)
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# --- Draw 8 rays using a loop ---
turtle.pencolor("orange")
turtle.pensize(2)

for i in range(8):
    angle = 90 + i * 45         # 8 rays, 45 degrees apart

    # Calculate start point (on the edge of the circle)
    start_x = cx + radius * math.cos(math.radians(angle))
    start_y = cy + radius * math.sin(math.radians(angle))

    # Calculate end point (beyond the circle)
    end_x = cx + (radius + ray_length) * math.cos(math.radians(angle))
    end_y = cy + (radius + ray_length) * math.sin(math.radians(angle))

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)

turtle.hideturtle()
turtle.done()
