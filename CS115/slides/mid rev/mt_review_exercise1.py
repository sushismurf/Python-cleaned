# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:25:50 2018

@author: b
"""

def updateFrequency(fList, roll):
    if roll > 0 and roll <= len(fList):
        fList[roll-1] += 1
        return True
    else:
        print('Roll not valid')
        return False
"""
def updateFrequency(fList, roll):
    try:
        fList[roll-1] += 1
        return True
    except:
        print('Roll not valid')
        return False
"""
freq = [0,0,0,0,0,0]
roll = int(input('Enter roll (-1 to quit): '))
while roll != -1:
    res = updateFrequency(freq, roll)
    if res:
        print('frequencies updated')
    roll = int(input('Enter roll (-1 to quit): '))

print('Face Value: Frequency')
for i in range(6):
    print(i+1,'\t\t',freq[i])
    
