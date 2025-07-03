#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:51:38 2024

"""

def remove_tuple_elements_containing_tuples(t):
    result = ()
    for e in t:
        if type(e) == tuple: 
            found = False
            for e2 in e:
                if type(e2) == tuple:
                    found = True
                    break
            if not found:
                result += (e, )
        else:
            result +=  (e, )
            
    return result

tuples = ( (5, 'ab', (1, 4), 4.3, 'xyz', (2, 'a')),
           (5, 'ab', (1, 4, (3, 5)), 4.3, 'xyz', (2, 'a', (2, 7))),
           (5, 'ab', [1, 4, (3, 5)], 4.3, 'xyz', (2, 'a', [2, (7)])),
           (5, 'ab', (1, 'xyz', (2, 3, (4, 5, [6, 7])))),
           (5, 'ab', (1, 'xyz', [2, 3, (4, 5, (6, 7))]))
          )

for tup in tuples:
    print('input tuple:', tup)
    print('tuple elements containing a tuple removed: ', remove_tuple_elements_containing_tuples(tup))

