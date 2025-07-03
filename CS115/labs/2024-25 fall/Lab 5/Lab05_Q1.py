#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:16:07 2024

"""

def swap_pairs(alist):
    for i in range(0, len(alist) - 1, 2):
        alist[i], alist[i+1] = alist[i+1], alist[i]


# # alternative way
# def swap_pairs(alist):
#     for i in range(0, len(alist) - 1, 2):
#         temp = alist[i]
#         alist[i] = alist[i+1]
#         alist[i+1] = temp 
    

    
for L in ( [2, 8, 5, 9, 4, 7, 6], ['ab', (2, 4), True, 5, [9, 4], (7, (9, (3, 6))) ]):
    print('original list: ', L)
    swap_pairs(L)
    print('pairs swapped: ', L)