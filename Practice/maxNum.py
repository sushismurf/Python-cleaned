# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:43:32 2023.

@author: doga

Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.
"""

number = input("please enter an integer: ")

if number.isdecimal():
    number = int(number)
else:
    print("that doesnt seem like an integer to me...")

max_number = None

for i in range(1, 10):
    newNumber = input("please enter an integer: ")
    if newNumber.isdecimal():
        newNumber = int(newNumber)
    else:
        print("that doesnt seem like an integer to me...")
        break
    if newNumber % 2 == 1 and (max_number is None or newNumber >= max_number):
        max_number = newNumber
    else:
        continue

if max_number is None:
    print("neither of the numbers you entered were odd.")
else:
    print("out of all the numbers entered, the greatest odd one is",
          max_number)
