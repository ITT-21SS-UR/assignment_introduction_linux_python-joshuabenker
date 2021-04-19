#!/usr/bin/python3

"""
**circle.py**: Takes a *radius* (int) as commandline parameter.
Draws something resembling a circle with the given radius
using the `turtle` module.The turtle should alternative
move forward or turn left/right so that
it stays at about *radius* pixels from the center of the screen.
"""
import turtle
import sys
import math


def drawCircle():
    # set radius from input
    radius = float(sys.argv[1])
    # set background color
    turtle.bgcolor("blue")
    # new turtle "fred"
    fred = turtle.Turtle()
    # pen "off"
    fred.penup()
    # set start position
    fred.setposition(radius, 0.00)
    # set pen values
    fred.pen(pensize=10)
    # pen "on"
    fred.pendown()
    # set freds colors
    fred.color("yellow", "green")
    # new turtle "amy" joings
    amy = fred.clone()
    # set amys color
    amy.color("yellow", "pink")
    # start filling
    fred.begin_fill()
    amy.begin_fill()
    fred.left(90)
    amy.right(90)
    # draw circle with one degree per stepo
    # amy and fred draw together, each turtle a half one
    for i in range(0, 180):
        fred.forward(2 * math.pi * radius / 360)
        fred.left(1)
        amy.forward(2 * math.pi * radius / 360)
        amy.right(1)
    fred.end_fill()
    amy.end_fill()
    # exit screen via click
    turtle.Screen().exitonclick()


if __name__ == "__main__":
    drawCircle()
