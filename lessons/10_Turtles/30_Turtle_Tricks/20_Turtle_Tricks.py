"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

tina.pencolor("red")                    # Change the pen color to red
tina.forward(100)                       # Move tina forward by 100
tina.left(72)                           # Turn tina left by 72 degrees
tina.pencolor("blue")                   # Change the pen color to blue
tina.forward(100)                       # Move tina forward by 100
tina.left(72)                           # Turn tina left by 72 degrees
tina.pencolor("green")                  # Change the pen color to green
tina.forward(100)                       # Move tina forward by 100
tina.left(72)                           # Turn tina left by 72 degrees
tina.pencolor("orange")                 # Change the pen color to orange
tina.forward(100)                       # Move tina forward by 100
tina.left(72)                           # Turn tina left by 72 degrees
tina.pencolor("purple")                 # Change the pen color to purple
tina.forward(100)                       # Move tina forward by 100
tina.left(72)                           # Turn tina left by 72 degrees

turtle.exitonclick()                    # Close the window when we click on it