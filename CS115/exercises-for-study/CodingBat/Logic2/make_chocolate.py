"""
question:

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

my solution:
"""

def make_chocolate(small, big, goal):
  if small + big*5 >= goal:
    if goal % 5 > small:
      return -1
    else:
      if 5*big <= goal:
        goal = goal - 5*big
      else:
        while big > 0 and goal // 5 != 0:
          big -= 1
          goal -= 5
      if goal <= small:
        return goal
      else:
        return -1
  else:
    return -1
