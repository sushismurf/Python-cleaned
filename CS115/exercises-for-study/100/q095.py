# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:53:59 2024.

q: Define a class Person and its two child classes: Male and Female. All
classes have a method "getGender" which can print "Male" for Male class and
"Female" for Female class.

@author: sushismurf
"""

class Person(object):
    pass
class Female(Person):
    def getGender(self):
        return "Female"
class Male(Person):
    def getGender(self):
        return "Male"
