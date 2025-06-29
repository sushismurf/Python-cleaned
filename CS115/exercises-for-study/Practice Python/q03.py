# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:22:31 2023.

@author: billypatty

Take a list and print out all the elements of the list that are less than 5.
"""

myList = []

while True:
    userIn = input("Enter an integer (q to stop): ")
    if userIn == 'q':
        break
    userNum = int(userIn)
    myList.append(userNum)

myCopy = list(myList)

for i in myCopy:
    if i > 5:
        myList.remove(i)

print(myList)
