# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:25:50 2018

@author: b
"""

def getNumberAsString(num):
    if num == 1:
        return 'One'
    elif num == 2:
        return 'Two'
    elif num == 3:
        return 'Three'
    elif num == 4:
        return 'Four'
    elif num == 5:
        return 'Five'
    elif num == 6:
        return 'Six'
    else:
        return 'ERROR'

def updateFrequency(fDict, roll):
    sRoll = getNumberAsString(roll)
    if sRoll in fDict:
        fDict[sRoll] += 1 
    else:
        fDict[sRoll] = 1
        


fDict = {}
roll = int(input('Enter roll (-1 to quit): '))
while roll != -1:
    updateFrequency(fDict, roll)
    roll = int(input('Enter roll (-1 to quit): '))

print('Face Value: Frequency')
for i in range(1,7):
    sKey = getNumberAsString(i)
    if sKey in fDict: 
       print(sKey,'\t\t',fDict[sKey])
    else:
        print(sKey,'\t\t',0)
if 'ERROR' in fDict:
    print('ERRORS: ','\t',fDict['ERROR'])
else:
    print('No invalid rolls')
    
