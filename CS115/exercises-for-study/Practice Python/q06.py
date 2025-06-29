# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:34:28 2023.

@author: billypatty

Ask for a string and print out whether this string is a palindrome.
"""

word = input("input a string: ")

if word == word[::-1]:
    print("yay")
else:
    print("nay")
