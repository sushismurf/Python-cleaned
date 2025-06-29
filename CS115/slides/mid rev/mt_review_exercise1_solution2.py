# -*- coding: utf-8 -*-

"""
    As an alternative:
    to hold the frequency of the invalid entries (errors) 
    assuming that the first item of the freq list always holds the errors.    
"""

ERROR = 0   # constant value: index for the error in the freq list.

def updateFrequency(fList, roll):
    try:
        fList[roll] += 1
        return True
    except:
        print("Roll not valid")
        fList[0] += 1
        return False

freq = [0, 0, 0, 0, 0, 0, 0]

roll = int(input("Enter roll (-1 to stop): "))
while roll != -1:
    updated = updateFrequency(freq, roll)
    if updated:        # This line can also be writen as --->  if updated == True:
        print("Frequencies updated.")
    roll = int(input("Enter roll (-1 to stop): "))
    
print('Face Value: Frequency')
for i in range(1, 7):
    print(i, "\t\t", freq[i])
    
print("Errors: \t\t", freq[ERROR])  # instead of writing freq[0]
    

