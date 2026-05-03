# example_04_spiral.py
# Lesson 14: Drawing spirals by increasing the forward distance each step

import turtle

turtle.speed(0)   # instant drawing

# Square spiral: increase side length by 5 each step
print("Drawing square spiral...")
distance = 5
for i in range(40):
    turtle.forward(distance)
    turtle.right(90)
    distance = distance + 5

turtle.done()
