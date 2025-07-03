#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:39:54 2020

@author: user
"""

class Stock:
    def __init__(self,name,count,price, minimum):
        self.__name = name
        self.__count = count
        self.__price = price
        self.__min_stock = minimum
            
    def get_name(self):
        return self.__name 
    
    def get_count(self):
        return self.__count
    
    def get_price(self):
        return self.__price
    
    def get_min_stock(self):
        return self.__min_stock
    
    def set_count(self, count):
        self.__count = count
     
    def __str__(self):
        out = 'Name: ' + self.__name+'\n'
        out +='Count: '+ str(self.__count)+'\n'
        out +='Price: '+ str(self.__price)+'\n'
        out +='Minimum Stock Level: '+ str(self.__min_stock) +'\n'
        return out

    def __repr__(self):
        out = 'Name: '+ self.__name+'\n'
        out +='Count: '+ str(self.__count)+'\n'
        out +='Price: '+ str(self.__price)+'\n'
        out +='Minimum Stock Level: '+ str(self.__min_stock) +'\n'
        return out
