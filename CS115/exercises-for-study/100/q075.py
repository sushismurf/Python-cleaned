# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:07:31 2024.

q: Use random.random() to generate a random float in [0,1].

@author: sushismurf
"""

import random
a = random.random()*10
while a > 1 or a < 0:
    a = random.random()*10
print(a)
