# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:07:01 2023.

@author: billypatty

Write a program that takes a list of numbers and makes a new list of only the
first and last elements of the given list.
"""


def firstLast(k):
    """
    Find the first and the last elements of a list.

    Parameters
    ----------
    k : list
        a list the user provides.

    Returns
    -------
    first : str
        the first element of the list.
    last : str
        the last element of the list.
    None: boolean
        if no valid value is provided.
    """
    if len(k) == 0:
        return None
    elif len(k) == 1:
        return 1, k[0]
    else:
        first = k[0]
        last = k[-1]
        return first, last


userList = []

while True:
    a = input("please enter anything to put in the list (stoplist to quit): ")
    if a.lower() == 'stoplist':
        break
    else:
        userList.append(a)

if firstLast(userList) is None:
    print("no valid input.")
elif firstLast(userList)[0] == 1:
    print("there is only one value, and that is", firstLast(userList)[1])
else:
    print("the first value is", firstLast(userList)[0])
    print("the last value is", firstLast(userList)[1])
