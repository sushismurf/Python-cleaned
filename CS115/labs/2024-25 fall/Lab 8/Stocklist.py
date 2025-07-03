# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:41:39 2020

@author: b
"""

from Stock import *

class Stocklist:
    def __init__(self, name, city):
        self.__stocklist_name = name
        self.__city = city
        self.__stock_list = []
           
    def add_stock(self, stock):
        self.__stock_list.append(stock)       
    
    def get_num_stocks(self):
        return len(self.__stock_list)
    
    def get_stock(self, index):
        return self.__stock_list[index]
    
    def bubbleSort(self):
        issorted = False;
        j = 0
        while(j < len(self.__stock_list)-1 and not issorted):
            issorted = True;
            for k in range(len(self.__stock_list)-j-1):
                if self.__stock_list[k] > self.__stock_list[k+1]:
                    issorted = False
                    (self.__stock_list[k], self.__stock_list[k + 1]) = (self.__stock_list[k+1], self.__stock_list[k])
            j = j + 1
         
    def linearSearch(self, begin):
        if begin == len(self.__stock_list):
            return
        elif self.__stock_list[begin].get_count() < self.__stock_list[begin].get_min_stock():
                print(self.__stock_list[begin].get_min_stock() - self.__stock_list[begin].get_count(), 'quantities of', self.__stock_list[begin].get_name(), 'must be ordered')
        return self.linearSearch(begin + 1)

    def __repr__(self):
        data = self.__stocklist_name + '\t' + self.__city + '\n\n'
        for i in self.__stock_list:
            data += str(i) + '\n'
        return data