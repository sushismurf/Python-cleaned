"""
question:

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

my solution:
"""

def monkey_trouble(a, b):
  if a:
    if b:
      return True
    elif not b:
      return False
  elif not a:
    if not b:
        return True
    else:
      return False
