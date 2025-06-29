# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:07:15 2022

@author: Teacher
"""

def name_of(num):
    if num == 1:
        return "One"
    elif num == 2:
        return "Two"
    elif num == 3:
        return "Three"
    elif num == 4:
        return "Four"
    elif num == 5:
        return "Five"
    elif num == 6:
        return "Six"
    else:
        return "Error"
    
def updateFrequency(freq_dict, roll):
    freq_dict[name_of(roll)] += 1    
    # Note that: In this function we assume all possible keys (name_of(roll)) 
    # exists in the dictionary


# --- Create dictionary with all possible keys with the initial value 0 ---
# fDict = { "One": 0, "Two": 0, "Three": 0, 
#           "Four": 0, "Five": 0, "Six": 0,
#           "Error": 0}

fDict = {}
for i in range(1, 7):
    fDict[name_of(i)] = 0
fDict["Error"] = 0
# print(fDict)   

# --- Enter data -----------------
roll = int(input("Enter roll (-1 to stop): "))
while roll != -1:
    updateFrequency(fDict, roll)      
    roll = int(input("Enter roll (-1 to stop): "))

# --- Display the results --------
print('Face Value: Frequency')
for key in fDict:
    print(key, "\t\t", fDict[key])