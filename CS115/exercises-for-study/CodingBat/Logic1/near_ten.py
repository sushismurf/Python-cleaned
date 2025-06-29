"""
question:

Given a non-negative number "num", return True if num is within 2 of a multiple of 10.

my solution:

this is probably a bad solution.
"""

def near_ten(num):
  if  int(str(num)[-1]) in [0, 1, 2, 8, 9]:
    return True
  else:
    return False

# # another solution by using mod:
# def near_ten(num):
#   if  num % 10 >= 8 or num % 10 <= 2:
#     return True
#   else:
#     return False
# # could probably still be improved?
