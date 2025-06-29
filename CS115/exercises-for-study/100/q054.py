# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:12:29 2024.

q: Define a class named Shape and its subclass Square. The Square class has an
init function which takes a length as argument. Both classes have a area
function which can print the area of the shape where Shape's area is 0
by default.

@author: sushismurf
"""

class shape(object):
    def __init__(self):
        pass
    def area(self):
        pass
class square(shape):
    def __init__(self, l):
        self.l = l
    def area(self):
        return self.l**2
