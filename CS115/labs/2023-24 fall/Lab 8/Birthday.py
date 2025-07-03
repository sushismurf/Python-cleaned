# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:23:11 2021

@author: user
"""

class Birthday:
    
    def __init__(self, name, month, day):
        self.__name = name
        self.__bMonth = month
        self.__bDay = day
        
    def getName(self):
        return self.__name
         
    def getMonth(self):
        return self.__bMonth
    
    def getDay(self):
        return self.__bDay
    
    def __eq__(self, other):
        return self.__name == other.__name

    def __lt__(self,other):
        return self.__name < other.__name
        
    def __repr__( self ):
        return self.__name + ': ' + str(self.__bDay) + '/' + str(self.__bMonth)