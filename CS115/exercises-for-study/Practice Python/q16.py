# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:00:48 2023.

@author: doga

Write a password generator. Keep in mind that strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords
should be random, generating a new password every time the user asks for a new
one.
"""
import random


def passwordGenerator(n):
    """
    Generate a password with specified length.

    Parameters
    ----------
    n : int
        some number.

    Returns
    -------
    pasTry1 : str
        a randomly generated password.
    """
    alpLow = 'qwertyuopasdfghjklizxcvbnm'
    alpCap = 'QWERTYUOPASDFGHJKLIZXCVBNM'
    numbers = '0123456789'
    specChar = '!#$%*+-./:;?@_~'
    geb = [alpCap, alpLow, numbers, specChar]
    pasTry1 = ""
    pasTry1 += random.choice(alpCap)
    pasTry1 += random.choice(alpLow)
    pasTry1 += random.choice(numbers)
    pasTry1 += random.choice(specChar)
    for i in range(n-4):
        a = random.choice(geb)
        b = random.choice(a)
        pasTry1 += b
    pasTry1 = ''.join(random.sample(pasTry1, len(pasTry1)))
    return pasTry1


useRe = input("please enter how many digits you want the password to be: ")
try:
    useRe = int(useRe)
    if useRe >= 4:
        print(f"here is a randomly generated {useRe} digit password: " +
              passwordGenerator(useRe))
    else:
        print("the password can be 4 digits minimum.")
except ValueError:
    print("that is not an integer...")
