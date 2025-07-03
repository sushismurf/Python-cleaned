# -*- coding: utf-8 -*-
"""
Lab 3 q1 
"""

def sum_without_twenties(a, b, c):
    """
    Returns the sum of a, b, c ignoring the ones between [20-29]
    Parameters:
        a: int
           first number
        b: int
           second number
        c: int
           third number    
    Returns:
        total: int
           sum of a,b,c obeying the given condition
    """
    total = 0
    if a < 20 or a > 29:
        total += a
    if b < 20 or b > 29:
        total += b
    if c < 20 or c > 29:
        total += c
    return total


first = int(input('Enter first integer: '))
second = int(input('Enter second integer: '))
third = int(input('Enter third integer: '))

while first > 0 and second > 0 and third >0:
    result = sum_without_twenties(first, second, third)
    print('Sum of',first, second, third, 'without twenties is', result)
    first = int(input('Enter first integer: '))
    second = int(input('Enter second integer: '))
    third = int(input('Enter third integer: '))
    
    





