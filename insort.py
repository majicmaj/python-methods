def insort(arr, num, left = 0, right = None):
  # insert num into arr, inserting it on the right if num already exists in arr.

  if right is None:
    right = len(arr)
    
  while left < right:
    middle = (left + right) // 2
    if num < arr[middle]:
      right = middle
    else:
      left = middle + 1
  arr.insert(left, num)
