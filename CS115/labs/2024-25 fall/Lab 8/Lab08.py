# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:18:27 2020

@author: b
"""
from Stock import *
from Stocklist import *

def create_stocklist(fileName):
    dFile = open(fileName,'r')
    line = dFile.readline()
    parts = line.strip().split()
    stocklist = Stocklist(parts[0], parts[1])
    for line in dFile:
        data = line.strip().split(';')
        name = data[0]
        count = int(data[1])
        price = float(data[2])
        mini = int(data[3])
       
        stocklist.add_stock(Stock(name, count, price, mini))
    dFile.close()
    return stocklist

fname = 'input.txt'

stocklist = create_stocklist(fname)

stocklist.bubbleSort()

print('Bubble sorted stocklist:')
print(stocklist)

print('Stocks that must be ordered:')
stocklist.linearSearch(0)

