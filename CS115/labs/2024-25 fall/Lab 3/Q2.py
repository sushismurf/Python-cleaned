# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:46:47 2024

@author: user
"""

def checkPrime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
    return True

def twinPrime(max_num):
    """
    Generates the pair of twin primes
    """
    for first_num in range(2, max_num):
        second_num = first_num + 2
        if (checkPrime(first_num) and checkPrime(second_num)):
            print(f'{first_num} and {second_num}')
            
            
num = int(input('Enter an integer number: '))
twinPrime(num)
            
            