"""
Programmable turtle graphics

Use what you've learned about lists, loop, cycle, slice and zip to draw a pattern
"""

t = ... # Create a turtle like in previous programs, like 04_Crazy_Tina.py

colors = ... # Make a list of colors

directions = [ # Create a list of directions and angles
    ( ), # Add an (angle, distance) tuple for each line
    ( ), 
]

# Zip the colors and directions together, then unpack them. There is a good example of this
# in 10_More_iterables.ipynb in the discussion of zip()

for ... in zip( ... , ...):
    t.color( ... )
    t.forward( ... )
    t.left( ... )

# Don't forget the special way to end a turtle program. 