"""
question:

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

my solution:

the question essentially wants us to determine whether there is trouble or not. 
if t is True, then the parrot is talking. we'll check the hours to see if there is any trouble.
if t is False, the parrot is silent. regardless of hour, there is no trouble.
"""

def parrot_trouble(t, a):
  if t:
    if a<7 or a>20:
        return True
    else:
      return False
  elif not t:
    return False
