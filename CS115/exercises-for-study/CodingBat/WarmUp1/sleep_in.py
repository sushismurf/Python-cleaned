"""
question:

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

my solution:
"""

def sleep_in(w, v): 
  if not w:  
    return True  
  elif w:  
    return v 
