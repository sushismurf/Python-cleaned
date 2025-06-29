"""
question:

Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum()

my solution:
i didn't read the question at first. so i have two seperate solutions
"""

# # me being illiterate (no fix_teen function)
# def no_teen_sum(a, b, c):
#   teens = [x for x in range(13, 20) if x != 15 and x != 16]
#   if a in teens:
#     a = 0
#   if b in teens:
#     b = 0
#   if c in teens:
#     c = 0
#   return a + b + c
  
# after becoming literate
def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  return a + b + c

def fix_teen(a):
  if a in range(13, 20) and a != 15 and a != 16:
    a = 0
    return a
  else:
    return a
