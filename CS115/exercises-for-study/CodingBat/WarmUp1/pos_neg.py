"""
question:

Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.

my solution:
"""

def pos_neg(a, b, negative):
  if negative == False:
    if a < 0 and b < 0: 
      return False
    elif a<0 or b<0:  
      return True
    else:  
      return False
  elif negative == True:
    if a <0 and b<0: 
      return True
    else:
      return False

