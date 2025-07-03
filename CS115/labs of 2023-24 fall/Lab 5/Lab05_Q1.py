#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:17:31 2023

"""

def pair_sum(alist):
    result = []
    for i in range(0, len(alist) - 1, 2):
        result.append(alist[i] + alist[i + 1])
    if len(alist) % 2 != 0:
        result.append(alist[-1])
    return result

mylist = [2, 8, 5, 9, 4, 7, 9, 3, 6]
newlist = pair_sum(mylist)

print('original list: ', mylist)
print('pair sum list: ', newlist)

mylist = [2, 8, 5, 9, 4, 7]
newlist = pair_sum(mylist)

print('original list: ', mylist)
print('pair sum list: ', newlist)


