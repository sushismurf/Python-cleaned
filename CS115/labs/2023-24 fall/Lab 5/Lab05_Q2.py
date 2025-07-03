#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:32:14 2023

"""

def select_tuples(t):
    result = ()
    for e in t:
        if type(e) == tuple:    
            result +=  (e, )
    return result

tuples = ( (5, 'ab', (1, 4), 4.3, 'xyz', (2, 'a')),
           (5, 'ab', (1, 4, (3, 5)), 4.3, 'xyz', (2, 'a', [2, 7])),
           (5, 'ab', [1, 4, (3, 5)], 4.3, 'xyz', (2, 'a', (2, 7))),
           (5, 'ab')
          )
for tup in tuples:
    print('input tuple:', tup)
    print('tuples in input tuple: ', select_tuples(tup))

