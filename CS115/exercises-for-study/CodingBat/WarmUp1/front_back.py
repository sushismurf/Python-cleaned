"""
question:

Given a string, return a new string where the first and last chars have been exchanged.

my solution:
"""

def front_back(s):
  if len(s) <= 1:
    return s
  else:
    copstr = '' 
    copstr += s[-1]
    for i in range(1, len(s) -1): 
      copstr += s[i] 
    copstr += s[0] 
    return copstr
