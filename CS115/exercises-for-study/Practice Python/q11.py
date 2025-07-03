# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:43:24 2023.

@author: doga

Ask the user for a number and determine whether the number is prime or not.
"""


def is_prime(n):
    """
    Determine whether the number is prime.

    Parameters
    ----------
    n : int
        the number that has been input by the user.

    Returns
    -------
    1 : int
        means the number is a prime.
    """
    divisorList = []

    for i in range(2, n):  # not including 1 or n.
        if n % i == 0:
            divisorList.append(int(i))

    if divisorList == []:  # no divisors
        return 1
    else:
        return divisorList


userN = input("please enter a positive integer: ")

try:
    userN = int(userN)
    if userN > 0:
        val = is_prime(userN)
        if val == 1:
            print("the number is prime indeed.")
        else:
            print("the number is not prime. It has the following divisors: ")
            resultList = val
            print(int(1), end=', ')
            for k in range(len(resultList)):
                print(int(resultList[k]), end=', ')
            print(int(userN))
    else:
        print("that's not positive.")
except ValueError:
    print("that's not an integer.")
