# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  part1 = str[:n]
  cut= n+1
  part2 = str[cut:]
  new_str = part1 +  part2
  return  new_str
