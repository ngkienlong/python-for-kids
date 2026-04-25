"""
Lesson 17 - Example 01: Setting Up the Canvas
Shows how to use title(), setup(), and bgcolor()
"""
import turtle

# --- Window configuration ---
turtle.title("My Artwork")          # text shown in the title bar
turtle.setup(width=800, height=600) # window size: 800 wide, 600 tall
turtle.bgcolor("lightyellow")       # background color

# --- Configuration variables (easy to change) ---
circle_color = "steelblue"
circle_radius = 60
text_color = "darkblue"

# --- Draw a circle in the center ---
turtle.penup()
turtle.goto(0, -circle_radius)      # goto() starts circle from bottom
turtle.pendown()

turtle.fillcolor(circle_color)
turtle.pencolor("navy")
turtle.pensize(3)
turtle.begin_fill()
turtle.circle(circle_radius)
turtle.end_fill()

# --- Write a label ---
turtle.penup()
turtle.goto(0, -circle_radius - 30)
turtle.pendown()
turtle.pencolor(text_color)
turtle.write("Hello, Artist!", align="center", font=("Arial", 16, "bold"))

turtle.hideturtle()
turtle.done()
