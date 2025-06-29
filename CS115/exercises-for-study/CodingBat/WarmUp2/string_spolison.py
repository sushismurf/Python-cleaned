"""
question:

Given a non-empty string like "Code" return a string like "CCoCodCode".

my solution:
"""

def string_splosion(s):
  a = '' 
  for i in range(len(s)):  
    for j in range(0,i):  
      a += s[j]  
  a += s 
  return a
