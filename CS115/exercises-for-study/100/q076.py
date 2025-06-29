# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:10:13 2024.

q: Please write a program to output a random even number between 0 and 10
inclusive using random module and list comprehension.

@author: sushismurf
"""

import random
a = range(0, 11)
b = random.choice(a)
while b % 2 != 0:
    b = random.choice(a)
print(b)
