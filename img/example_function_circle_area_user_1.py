#!/usr/bin/env python

# Area of a circle = pi * r**2

# Library Numpy
import numpy as np
# Library to Safely evaluate an expression node
# or a string containing a Python expression
import ast

# List are called interables
list_raw = raw_input('Provide a list of radius in cm like \
[3, 2, 12, 6]: \n')
list = ast.literal_eval(list_raw)


def area_circle(radius):
    'Function that calculates the area of a circle'
    area = np.pi * radius ** 2
    return area


for radius in list:
    area = area_circle(radius)
    print "The area of a circle of radius ", radius
    print "cm is", area, "cm^2"
print "Finished to calculate the areas of circles"
