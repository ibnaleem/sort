def my_sort(arr: list) -> list:
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  left = [i for i in arr[1:] if i <= pivot]
  right = [i for i in arr[1:] if pivot < i]
  
  return my_sort(left) + [pivot] + my_sort(right)
