# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  result = ""
  count = 0
  if len(nums) < 4:
    list = nums
  else:
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    num4 = nums[3]
    list = [num1, num2, num3, num4]
  for num in list:
    if num == 9:
      count += 1
  if count >= 1:
      return True
  else:
      return False
