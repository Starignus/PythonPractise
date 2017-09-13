#!/usr/bin/env python

# Area of a circle = pi * r**2

# Library Numpy
import numpy as np


def area_circle(radius):
    'Function that calculates the area of a circle'
    area = np.pi * radius ** 2
    return area

# List are called interables
list = [1, 2, 3, 4, 5, 6]

for radius in list:
    area = area_circle(radius)
    print "The area of a circle of radius ", radius
    print "cm is", area, "cm^2"
print "Finished to calculate the areas of circles"
