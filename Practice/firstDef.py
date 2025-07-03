# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:38:57 2023.

@author: doga
"""


def maxValue(x, y):
    """
    Define the function that returns the greater number.

    Parameters
    ----------
    x : is a number the user tells.
    y : is another number the user tells.

    Returns
    -------
    the greater value among x and y.

    """
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print("the values are equal.")
        return x


userNum1 = int(input("please input a number (x): "))
userNum2 = int(input("please input a number (y): "))

print(maxValue(userNum1, userNum2))
