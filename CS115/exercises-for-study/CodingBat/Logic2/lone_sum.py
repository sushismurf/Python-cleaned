"""
question:

Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, it does not count towards the sum.

my solution:
i tried a few things.
"""

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c

# # alternatively,
# def lone_sum(a, b, c):
#   someTuple = (a, b, c)
#   unique_values = set(someTuple)
#   if len(unique_values) == 1:
#       return 0
#   return sum(unique_values) - sum(someTuple) + sum(set(someTuple))

# # even more generally,
# def lone_sum(*args):
#   unique_values = set(args)
#   if len(unique_values) == 0:
#     return 0
#   return sum(unique_values) - sum(args) + sum(set(args))
