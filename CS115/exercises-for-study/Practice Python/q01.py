# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:38:42 2023.

@author: billypatty

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
"""

userAge = int(input("enter your age: "))
userName = input("enter your name: ")

print("In", 100-userAge, "years,", userName, "will turn 100 years old.")
