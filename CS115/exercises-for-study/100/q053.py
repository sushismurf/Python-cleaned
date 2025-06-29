# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:00:33 2024.

q: Define a class named Rectangle which can be constructed by a length and
width. The Rectangle class has a method which can compute the area.

@author: sushismurf
"""

class rectangle(object):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w
