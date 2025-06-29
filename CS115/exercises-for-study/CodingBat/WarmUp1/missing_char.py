"""
question:

Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

my solution:
"""

def missing_char(s, n): 
  a = '' 
  b=[] 
  for i in s: 
    b.append(i) 
  c=b[n] 
  b.remove(c) 
  for j in b:
    a += str(j)
  return a
