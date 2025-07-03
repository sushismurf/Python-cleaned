# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:25:46 2024.

q: Define a custom exception class which takes a string message as attribute.

@author: doga
"""

class error(Exception):
    def __init__(self, a):
        self.a = a
e = error('what??')
