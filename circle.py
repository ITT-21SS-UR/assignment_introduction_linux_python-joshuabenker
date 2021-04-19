#!/usr/bin/python3

"""
**circle.py**: Takes a *radius* (int) as commandline parameter. 
Draws something resembling a circle with the given radius using the `turtle` module. 
The turtle should alternatively move forward or turn left/right so that 
it stays at about *radius* pixels from the center of the screen. 
Experiment with varying turning angles and movement distances. 
Do not use the `circle()` function - that would be too easy.
"""
import turtle
import sys
import math

def drawCircle():
    #set radius from input
    radius = float(sys.argv[1])
    turtle.penup()
    #set start position
    turtle.setposition(radius, 0.00)
    #set pen values
    turtle.pen(fillcolor="yellow", pencolor="green", pensize=10)
    #pen "on"
    turtle.pendown()
    turtle.left(90)
    #draw circle with one degree per step
    for i in range(0,360):
        turtle.forward(2 * math.pi * radius / 360)
        turtle.left(1)

if __name__ == "__main__":
    drawCircle()

    