# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:09:17 2024.

q: Write a program, which will find all such numbers between 1000 and
3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line.

@author: doga
"""

outList = []
for i in range(1000,3001):
    if i[0] % 2 and i[1] % 2 and i[2] % 2 and i[3] % 2:
        outList.append(str(i))
print(', '.join(outList))
