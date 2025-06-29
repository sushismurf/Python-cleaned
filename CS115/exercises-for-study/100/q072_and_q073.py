# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:43:55 2024.

q: Please write a binary search function which searches an item in a sorted
list. The function should return the index of element to be searched in the
list.

@author: sushismurf
"""

# only works for sorted lists. not sure why or how anyone would use this if
# they had a non-sorted list.

def bS(a, e):
    l = 0
    h = len(a) - 1
    m = 0
    while l <= h:
        m = (h + l) // 2
        if a[m] < e:
            l = m + 1
        elif a[m] > e:
            h = m - 1
        else:
            return m
    return "couldnt find it"
