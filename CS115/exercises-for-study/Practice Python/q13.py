# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:21:23 2023.

@author: billypatty

Ask the user how many Fibonnaci numbers to generate and do it.
"""


def fibogen(n):
    """
    Generate the given number of sigits of the Fibonacci sequence.

    Parameters
    ----------
    n : int
        the requested amount.

    Returns
    -------
    fibSeq : list
        for n > 2, the numbers in a list.
    3 : int
        if the value "n" is invalid.
    4: int
        for n = 1 or n = 2; 1 or 1, 1 respectively.

    """
    fibSeq = [1, 1]
    try:
        n = int(n)
        if n <= 0:
            return 3
        if n == 1:
            print(int(1))
            return 4
        elif n == 2:
            for i in range(len(fibSeq) - 1):
                print(int(fibSeq[i]), end=', ')
            print(int(fibSeq[-1]))
            return 4
        else:
            while True:
                if len(fibSeq) < n:
                    newVal = int(fibSeq[-1]) + int(fibSeq[-2])
                    fibSeq.append(newVal)
                else:
                    return fibSeq
                    break
    except ValueError:
        return None


userRequest = input("enter how many digits of Fibonacci you wish to see: ")

if fibogen(userRequest) is None:
    print("that's not an integer...")
elif fibogen(userRequest) == 3:
    print("well, that's not possible...")
else:
    print("the requested numbers are: ")
    for j in range(len(fibogen(userRequest)) - 1):
        print(int(fibogen(userRequest)[j]), end=', ')
    print(int(fibogen(userRequest)[-1]))
