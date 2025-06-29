# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:53:16 2024.

q: Define a class named Circle which can be constructed by a radius. The
Circle class has a method which can compute the area.

@author: sushismurf
"""

from math import pi
class circle(object):
    def __init__(self, c):
        self.c = c
    def area(self):
        return pi*(self.c**2)
