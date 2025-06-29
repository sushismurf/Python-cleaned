# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:21:32 2024.

q: Write a function to compute 5/0 and use try/except to catch the exceptions.

@author: sushismurf
"""

try:
    a = 5/0
except ZeroDivisionError:
    print('dividing by zero??')
