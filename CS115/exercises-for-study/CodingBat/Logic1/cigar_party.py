"""
question:

When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.

my solution:
"""

def cigar_party(cigars, is_weekend):
  if 40 <= cigars <= 60:
    return True
  else:
    if cigars >= 40:
      if is_weekend:
        return True
      else:
        return False
  return False
