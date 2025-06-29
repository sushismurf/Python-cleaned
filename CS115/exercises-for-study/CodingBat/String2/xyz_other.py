"""




my solution:
below is what i think should be the correct answer
it says that the function should return True for 'abc.xyzxyz'
but one of the 'xyz's is preceeded by a '.'? doesn't make sense
"""

def xyz_there(s):
  if 'xyz' in s:
    if '.' not in s:
      return True
    else:
      for i in range(len(s)-3):
        if s[i] == '.':
          if s[i+1] == 'x':
            if s[i+2] == 'y':
              if s[i+3] == 'z':
                return False
      return True    
  else:
    return False

# # what an example 'correct' solution looks like
# def xyz_there(s):
#   for i in range(len(s) - 2):
#     if s[i:i+3] == "xyz" and (i == 0 or s[i-1] != '.'):
#       return True
#   return False
