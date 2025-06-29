# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:22:47 2023.

@author: billypatty
"""


def find_root(number, power, epsilon):
    """
    Define function that calculates the root of an integer input ('number').

    It then tries to find a value ('answer') which is the root and an integer
    exponent ('power') that goes with it, so that answer ** power == number.

    Parameters
    ----------
    number (int): is the number that the user inputs.
    power (int): is the exponent of 'number'.
    epsilon (float): is a small value that helps calculations.

    Returns
    -------
    if 'number' is less than 0 and power % 2 == 0, returns None.
    else, returns a value 'answer' which is the root, and 'power' as
    its exponent.
    """
    if number < 0 and power % 2 == 0:
        print("no such combination exists.")
        return None

    low, high = min(-1, number), max(1, number)
    answer = (high + low) / 2

    while abs(answer ** power - number) >= epsilon:
        if answer ** power > number:
            high = answer
        elif answer ** power < number:
            low = answer
        else:
            print(answer)
        answer = (high + low) / 2
    return answer


# the following code makes the aforedefined function work.
"""
userNum = int(input("please input a number: "))
userPower = int(input("please input the exponent: "))
userEpsilon = float(input("please input an epsilon value: (the epsilon value \
helps the programme to be more precise. if you \
do not know what epsilon is, just type 0.01) "))

print(find_root(userNum, userPower, userEpsilon), f"to the power {userPower} \
is a close enough value to {userNum}.")
"""

# however, you might want to test the function before running it.


def try_find_root(tnumber, tpower, tepsilon):
    """
    Define the function that puts the aforedefined function find_root to test.

    Parameters
    ----------
    tnumber (int): is a number for testing purposes.
    tpower (int): is an exponent for testing purposes.
    tepsilon (float): is an epsilon value for testing purposes.

    *the 't' at each word's beginning stands for 'trial'.

    Returns
    -------
    'yay' or 'nay' depending on whether the function works or not.
    """
    for n in tnumber:
        for p in tpower:
            for e in tepsilon:
                result = find_root(n, p, e)
                if result is None:
                    val = 'no root'
                else:
                    if abs(result ** p - n) > e:
                        val = 'nay'
                    else:
                        val = 'yay'
                print(n, p, e, val)
                print(result)


# change the following numbers (note that some values are better for testing.)
tnumber = (0.25, 5, -4)
tepsilon = (0.01, 0.25, 1)
tpower = (1, 2, 4)

print(try_find_root(tnumber, tpower, tepsilon))
