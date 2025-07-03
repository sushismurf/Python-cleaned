# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:47:02 2023.

@author: doga

Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’
"""

birthday = input("enter your birthday as mm/dd/yyyy: ")
yearValue = ''

for char in birthday[-4:]:
    yearValue += char

print("you were born in year", yearValue)
