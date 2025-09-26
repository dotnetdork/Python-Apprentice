"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(2)                          # Set the speed of the turtle

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

tina.penup()                           # Lift the pen to move without drawing
tina.goto(-100, 0)                     # Move to a new location
tina.pendown()                         # Put the pen down to start drawing
tina.fillcolor("white")                  # Change the fill color to red
tina.begin_fill()                      # Start filling in the shape
tina.circle(50)                        # Draw a circle with a radius of 50
tina.end_fill()                        # End filling in the shape

tina.penup()                           # Lift the pen to move without drawing
tina.goto(-100, 0)                     # Move to a new location
tina.pendown()                         # Put the pen down to start drawing
tina.fillcolor("black")                 # Change the fill color to blue
tina.begin_fill()                      # Start filling in the shape
tina.circle(30)                        # Draw a circle with a radius of 30
tina.end_fill()                        # End filling in the shape

tina.penup()                           # Lift the pen to move without drawing
tina.goto(100, 0)                     # Move to a new location
tina.pendown()                         # Put the pen down to start drawing
tina.fillcolor("white")                  # Change the fill color to red
tina.begin_fill()                      # Start filling in the shape
tina.circle(50)                        # Draw a circle with a radius of 50
tina.end_fill()                        # End filling in the shape

tina.penup()                           # Lift the pen to move without drawing
tina.goto(100, 0)                     # Move to a new location
tina.pendown()                         # Put the pen down to start drawing
tina.fillcolor("black")                 # Change the fill color to blue
tina.begin_fill()                      # Start filling in the shape
tina.circle(30)                        # Draw a circle with a radius of 30
tina.end_fill()                        # End filling in the shape

tina.penup()                           # Lift the pen to move without drawing
tina.goto(-100, -100)                     # Move to a new location
tina.pendown()                         # Put the pen down to start drawing
tina.fillcolor("red")                  # Change the fill color to red
tina.begin_fill()                      # Start filling in the shape
# Draw a rectangle
for _ in range(1):
    tina.forward(200)                   # Move tina forward
    tina.left(90)                       # Turn tina left
    tina.left(90)                       # Turn tina left

turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!