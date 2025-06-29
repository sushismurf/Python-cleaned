"""
question:

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

my solution:

i'll try to solve it both with and without loop(s).
"""

# no loop
def make_bricks(small, big, goal):
  if small + big*5 >= goal:
    if goal % 5 > small:
      return False
    else:
      return True
  else:
    return False

# # loop solution that doesn't work
# def make_bricks(small, big, goal):
#   while big > 0 and goal >= 0:
#     if goal == 0:
#       return True
#       break
#     else:
#       big -= 1
#       goal -= 5
#   while big == 0 and small >= 0 and goal >= 0:
#     if goal == 0:
#       return True
#       break
#     else:
#       small -= 1
#       goal -= 1
#   return False

# # another loop (gives a 'timed out' error on the website, but test runs i've done seem to work)
# def make_bricks(small, big, goal):
#   while goal >= 5 and big > 0:
#       goal -= 5
#       big -= 1
#   while goal > 0 and small > 0:
#       goal -= 1
#       small -= 1
#     return goal == 0
