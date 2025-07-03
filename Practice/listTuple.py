# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:20:53 2023.

@author: doga

Write an expression that evaluates to the mean of
a tuple of numbers. Use the function sum.
"""

numbers = []

while True:
    user_input = input("Enter a number (-1 to stop): ")
    if user_input == "-1":
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if len(numbers) > 0:
    numbers_tuple = tuple(numbers)
    mean = sum(numbers_tuple) / len(numbers_tuple)
    print(f"The mean of the numbers is {mean}")
