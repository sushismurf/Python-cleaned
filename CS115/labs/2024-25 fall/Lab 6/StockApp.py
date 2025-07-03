#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:40:48 2020

@author: user
"""

from Stock import *
def getMinimumPrice(sList):
    price = sList[0].get_price()
    name = sList[0].get_name()
    for p in sList:
        if p.get_price() < price:
            price = p.get_price()
            name = p.get_name()
    return name

def getOrder(sList):
    new_list = []
    for p in sList:
        if p.get_count() < p.get_min_stock():
            new_list.append(p)
    return new_list
    
file = open('input.txt', 'r')
stocks = []
for line in file:
    stockData = line[:-1].split(';')
    name = stockData[0]
    count = int(stockData[1])
    price = float(stockData[2])
    mini = int(stockData[3])
    stock = Stock(name,count,price,mini)
    stocks.append(stock)
file.close()

orderList = getOrder(stocks)

# each Stocks's __repr__ method is invoked to get string representation      
print("Stocks which should be Ordered: ")
for p in orderList:
    print(p)
    
stock_min = getMinimumPrice(stocks)
print('The cheapest stock is "' + stock_min +'"')



