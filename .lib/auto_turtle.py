#!/usr/bin/env python
"""
auto_turtle.py

This script automatically sets up the ipyturtle3 environment
for use in a Jupyter Notebook.

When used with %run, it will:
1. Import all necessary modules (turtle, Canvas, TurtleScreen, Turtle, display).
2. Create and display a default Canvas named 'myCanvas'.
3. Define a custom Turtle class that remaps the coordinate system so that
   the student's (0, 0) is at (start_x, start_y) on the canvas.
4. Display the Canvas in the notebook.
5. Wait a moment to ensure the canvas is rendered.
6. Create a TurtleScreen for the canvas named 'myTS'.
"""

# --- Configuration ---
canvas_width = 750         # Width of the turtle canvas
canvas_height = 250        # Height of the turtle canvas
start_x = -300             # Starting X position of the canvas
start_y = -50              # Starting Y position of the canvas
# ---------------------

import time # Might not be necessary, but used for sleep

try:
    # 1. Import the main library and necessary classes
    import ipyturtle3 as turtle
    from ipyturtle3 import Canvas, TurtleScreen, Turtle
    from IPython.display import display

    # 2. Define a NEW Turtle class that overrides the original for custom behavior
    class turtle(Turtle):
            """
            Custom Turtle class that remaps the coordinate system.
            The student's (0, 0) is now our (start_x, start_y).
            """
            def __init__(self, screen=None, *args, **kwargs):
                # Store the new "origin"
                self._origin_x = start_x
                self._origin_y = start_y

                # Call the original __init__ to create the turtle
                super().__init__(screen, *args, **kwargs)
                
                # --- Set the default starting position ---
                # We use super().goto() to move to the *absolute* start
                self.penup()
                super().goto(self._origin_x, self._origin_y)
                self.pendown()

            ### --- OVERRIDDEN METHODS (Coordinate Remapping) --- ###

            def goto(self, x, y):
                """Moves the turtle to a (student) coordinate."""
                # Translate student's (x, y) to absolute (real_x, real_y)
                real_x = x + self._origin_x
                real_y = y + self._origin_y
                # Call the original goto
                super().goto(real_x, real_y)
            
            # setposition is an alias for goto
            def setposition(self, x, y=None):
                self.goto(x, y)

            def setx(self, x):
                """Sets the turtle's (student) x coordinate."""
                real_x = x + self._origin_x
                super().setx(real_x)

            def sety(self, y):
                """Sets the turtle's (student) y coordinate."""
                real_y = y + self._origin_y
                super().sety(real_y)

            def position(self):
                """Returns the turtle's (student) position."""
                # Get the *absolute* position
                abs_x, abs_y = super().position()
                # Translate to student's *relative* position
                rel_x = abs_x - self._origin_x
                rel_y = abs_y - self._origin_y
                return (rel_x, rel_y)
            
            # pos is an alias for position
            def pos(self):
                return self.position()

            def xcor(self):
                """Returns the turtle's (student) x coordinate."""
                return self.position()[0]

            def ycor(self):
                """Returns the turtle's (student) y coordinate."""
                return self.position()[1]
        
    # 3. Create a Canvas for the turtle to draw on
    myCanvas = Canvas(width=canvas_width, height=canvas_height)

    # 4. Display the Canvas in the Jupyter notebook
    display(myCanvas)

    # 5. Wait a moment to ensure the canvas is fully rendered
    time.sleep(1) 

    # 6. Create a TurtleScreen
    myTS = TurtleScreen(myCanvas)
    myTS.clear()  # Clear the screen to start fresh
    
# Handle import errors gracefully
except ImportError:
    print("❌ Error: 'ipyturtle3' or 'IPython' not found.")
    print("Please make sure you are in a Jupyter environment and have")
    print("ipyturtle3 installed (e.g., `pip install ipyturtle3`).")
# Handle any other exceptions
except Exception as e:
    print(f"An error occurred during auto_turtle setup: {e}")