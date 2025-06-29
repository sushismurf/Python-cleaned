"""
question:

Given a string, return the count of the number of times that a substring length 2 appears in the string 
and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).

my solution:
we're trying to find how many times the last two letters of a given word appears in the word
"""

def last2(s):
  count = 0
  if len(s) <= 2:  
    return 0
  else:  
    for i in range(len(s)-1):
      if i != len(s):
        if s[i] == s[-2]:
          if s[i+1] == s[-1]:
            count +=1
  return count -1
