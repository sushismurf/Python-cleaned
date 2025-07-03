#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:07:03 2024

"""

import math

width = float(input('Enter the width of a rectangle: '))
height = float(input('Enter the height of a rectangle: '))

area = width * height
perimeter = 2 * (width + height)

diagonal = (width ** 2 + height ** 2) ** 0.5

# alternative way
# diagonal = math.sqrt(width ** 2 + height ** 2)

print(f'area is {area:.3f}, perimeter is {perimeter:.2f}, diagonal is {diagonal:.4f}')

print('exact area is', area)
print('exact perimeter is', perimeter)
print('exact diagonal is', diagonal)
