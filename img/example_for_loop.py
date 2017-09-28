#!/usr/bin/env python

# Area of a circle = pi * r**2

# Library
import numpy as np

# List are called interables
list = [1, 2, 3, 4, 5, 6]

for radius in list:
    area = np.pi * radius ** 2
    print "The area of a circle of radius ", radius
    print "cm is", area, "cm^2"
print "Finished to calculate the areas of circles"
