"""
question:

Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged. 

my solution:
"""

def not_string(str):
  k = str.split(' ')  
  if k[0] == 'not':  
    return str
  else:
    return 'not ' + str  
