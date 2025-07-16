# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    first_char = str[0]
    last_char = str[-1]
    middle = str[1:-1]
    result = last_char + middle + first_char
    return result
