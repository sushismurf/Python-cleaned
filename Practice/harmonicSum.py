# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:46:59 2023.

@author: billypatty
"""


def harmonic_sum(n):
    """
    Calculate the harmonic sum.

    Parameters
    ----------
    n : int
        a number the user inputs.

    Returns
    -------
    h, the harmonic sum.
    """
    h = 0
    for i in range(1, n+1):
        h += 1/i
    return h


userNum = input("enter an integer: ")

try:
    userNum = int(userNum)
    if userNum <= 0:
        print("please enter a positive integer.")
    else:
        print("the harmonic sum is", harmonic_sum(userNum))
except ValueError:
    print("thats not an integer.")
