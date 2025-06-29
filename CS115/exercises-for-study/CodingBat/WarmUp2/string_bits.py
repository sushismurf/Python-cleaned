"""
question:

Given a string, return a new string made of every other char starting with the first,
so "Hello" yields "Hlo".

my solution:
we should be careful about words with even number of letters.
"""

def string_bits(s):
  a = ''  
  for i in range(len(s)):  
    if i%2==0: 
      a += s[i]  
  return a
