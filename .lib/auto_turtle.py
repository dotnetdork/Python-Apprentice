#!/usr/bin/env python
"""
auto_turtle.py

This script automatically sets up the ipyturtle3 environment
for use in a Jupyter Notebook.

When used with %run, it will:
1. Import all necessary modules (turtle, Canvas, TurtleScreen, Turtle, display).
2. Create and display a default Canvas named 'myCanvas'.
3. Display the Canvas in the notebook.
4. Wait a moment to ensure the canvas is rendered.
5. Create a TurtleScreen for the canvas named 'myTS'.
"""

# --- Configuration ---
canvas_width = 750          # Width of the turtle canvas
canvas_height = 250         # Height of the turtle canvas
# ---------------------

import time

try:
    # 1. Import the main library and necessary classes
    import ipyturtle3 as turtle
    from ipyturtle3 import Canvas, TurtleScreen, Turtle
    from IPython.display import display

    # 2. Create a Canvas for the turtle to draw on
    myCanvas = Canvas(width=canvas_width, height=canvas_height)

    # 3. Display the Canvas in the Jupyter notebook
    display(myCanvas)

    # 4. Wait a moment to ensure the canvas is fully rendered
    time.sleep(1) 

    # 5. Create a TurtleScreen
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