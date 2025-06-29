# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:17:21 2024.

q: Write a program that calculates and prints the value according to:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.

@author: billypatty
"""

from math import sqrt
def seq():
    flag = 0
    while True:
        a = input("give a comma-separated sequence of integers"
                  " (example: 1,2,3): ")
        for i in a:
            if i.isdigit() or i == ',':
                pass
            else:
                flag = 1
                print('invalid input.')
                break
        if flag == 0:
            d = a.split(',')
            return d
        else:
            flag = 0
someList = seq()
outList = []
for k in someList:
    outList.append(str(round(sqrt((2 * 50 * int(k)) / 30))))
print(','.join(outList))
