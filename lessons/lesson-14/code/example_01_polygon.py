# example_01_polygon.py
# Lesson 14: Drawing regular polygons with loops
# Formula: exterior angle = 360 / number of sides

import turtle

turtle.speed(3)

# Draw a pentagon (5 sides)
print("Drawing pentagon...")
turtle.pencolor("blue")
for i in range(5):
    turtle.forward(80)
    turtle.right(360 / 5)   # 72 degrees

# Move to the right and draw a hexagon (6 sides)
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.pencolor("red")
for i in range(6):
    turtle.forward(80)
    turtle.right(360 / 6)   # 60 degrees

# Polygon table:
# Triangle: 3 sides, 120 degrees
# Square: 4 sides, 90 degrees
# Pentagon: 5 sides, 72 degrees
# Hexagon: 6 sides, 60 degrees
# Octagon: 8 sides, 45 degrees

turtle.done()
