# example_02_square.py
# Lesson 12: Draw a square using a for loop
# A square has 4 equal sides and 4 right angles (90 degrees).

import turtle

turtle.speed(3)

# Draw a square: forward 100, turn right 90, repeat 4 times
for i in range(4):
    turtle.forward(100)   # draw one side
    turtle.right(90)      # turn right 90 degrees

# The turtle ends up back where it started!
turtle.done()
