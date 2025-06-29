# -*- coding: utf-8 -*-
"""

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
    if name_of(roll) in freq_dict:
        freq_dict[name_of(roll)] += 1
    else:
        freq_dict[name_of(roll)] = 1
    
fDict = {}

roll = int(input("Enter roll (-1 to stop): "))
while roll != -1:
    updateFrequency(fDict, roll)
    roll = int(input("Enter roll (-1 to stop): "))
    
# Display the results 
print('Face Value: Frequency')
for i in range(1, 7):
    if name_of(i) in fDict:
        print(name_of(i), "\t\t", fDict[name_of(i)])
    else:
        print(name_of(i), "\t\t", 0)

if "Error" in fDict:
    print("Error \t\t", fDict["Error"])
else:
    print("Error \t\t", 0)


# ----- ALTERNATIVE Code to Display the results ---- 
# print('Face Value: Frequency')
# for i in range(1, 7):
#     print(name_of(i), "\t\t", fDict.get(name_of(i), 0))  
    
# print("Error \t\t", fDict.get("Error", 0))
    