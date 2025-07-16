# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  result = ""
  n = 0
  new_str = ""
  
#  two_str = str[n]
#  str_len = len(str)
 
#  if len(str) < 1 or str_len == 1:
#    result = str
#  elif str_len == 2:
#    n = n + 1
#    result = two_str + two_str + str[n]
#  else:

  for i in str:
    new_str = new_str + str[n]
    result += new_str
    n = n + 1
    
  return result
