# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:33:56 2023.

@author: billypatty

 Implement a function that meets the specification
 def get_min(d):
     d a dict mapping letters to ints
 returns the value in d with the key that occurs first
in the
 alphabet. E.g., if d = {x = 11, b = 12}, get_min
returns 12.
"""


def get_min(d):
    """
    Map letters to ints.

    Return
    ------
    The value in d with the key that occurs first
    in the alphabet.
    """
    mimi = None
    a = list(d.keys())
    a.sort()
    b = a[0]
    mimi = d[b]
    return mimi


d = {}
userKey = input("enter a key value (0000 to stop): ")
while userKey != '0000':
    userValue = input("enter its value: ")
    d[userKey] = userValue
    userKey = input("enter a key value (0000 to stop): ")
print("finished dictionary creation.")
if get_min(d) is not None:
    print(get_min(d), "is the smallest key's value.")
else:
    print("no min value.")

