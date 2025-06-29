# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:34:47 2024.

q: Please write a program to randomly print a integer number between 7 and 15
inclusive.

@author: sushismurf
"""

import random
b = 0
while b > 15 or b < 7:
    b = random.choice(range(7, 16))
print(b)
