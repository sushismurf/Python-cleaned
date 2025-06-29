# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:05:37 2024.

q: Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

@author: billypatty
"""

class somethin(object):
    def __init__(self, i):
        self.__idk = i
    def getString(self):
        self.__idk = input("say something: ")
    def printString(self):
        print(self.__idk.upper())


var = somethin("")
var.getString()
var.printString()
