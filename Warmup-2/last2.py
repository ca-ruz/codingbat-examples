# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
  last2chars = str[-2:]
  pairs_list = []
  result = ""
  len_str = len(str)
  
  if len_str == 0:
    return 0
  else:
    for i in range(0, len_str):
      pair = str[i:i+2]
      pairs_list.append(pair)
      matching_items = [item for item in pairs_list if last2chars in item]
      result = len(matching_items) - 1
  
    return result
