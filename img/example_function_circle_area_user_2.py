#!/usr/bin/env python

# Usage instructions:
# ./example_function_circle_area_user_2.py "[1, 2, 3]"

# Area of a circle = pi * r**2

# Library Numpy
import numpy as np
# Library to Safely evaluate an expression node
# or a string containing a Python expression
import ast
# Module provides access to some variables
# used or maintained by the interpreter
import sys


list_raw = sys.argv[1]
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
