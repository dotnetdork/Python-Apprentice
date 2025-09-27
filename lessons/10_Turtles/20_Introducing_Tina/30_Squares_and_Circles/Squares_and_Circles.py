"""
# Squares_and_Circles.py

This Turtle program demonstrates basic drawing and text output in Python.
It draws a colored square, places a filled circle inside it, and writes a message on the screen.
Lines starting with # are single-line comments, used to describe what each part of the code does.
Text enclosed in triple quotes (like this) is a docstring, which provides a multi-line explanation at the top of the file.

Review each section to see how the turtle is moved, how shapes are drawn, and how text is displayed.
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

##
## Move Tina to the Starting Position
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Square
##

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(90)                          # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(90)                          # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(200)
tina.right(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(200)
tina.right(90)

##
## Draw a Circle
##

tina.penup()     
tina.goto(0, -75)
tina.pendown()     

tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(75)
tina.end_fill()

##
## Write a Message
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-50, -150)
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick()                    # Close the window when we click on it  

# You're on your way, soon you'll be writing your own programs!
# But first, let's save your progress. Continue with 
# the next file, 40_Check_In_Your_Code.ipynb