# example_01_first_turtle.py
# Lesson 12: Your first turtle program — draw a line
# The turtle starts at (0,0) facing right.

import turtle

turtle.speed(3)         # drawing speed: 1=slow, 10=fast, 0=instant

# Draw a horizontal line 200 pixels long
turtle.forward(200)

# The turtle is now at (200, 0)
print("Done drawing!")

turtle.done()           # keep the window open
