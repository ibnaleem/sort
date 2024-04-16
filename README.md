# sort
an array sorting algorithm in ascending order implemented in Python
```py
def my_sort(arr: list) -> list:
  if len(arr) <= 1:
    return arr
```
Empty and single element arrays cannot be sorted. The array requires at least two elements.
```py
pivot = arr[0]
```
Variable `pivot` stores the value of the first element. This algorithm must *pivot* the given array to the left (less than) or right (greater than) of the first element. For example, if `pivot = 5`, then all elements less than 5 must be pivoted to the left, else, they must be pivoted to the right.
```py
left = [i for i in arr[1:] if i <= pivot]
right = [i for i in arr[1:] if pivot < i]
```
All elements less than the first element are *pivoted* to the left, else, they are *pivoted* to the right.
```py
return my_sort(left) + [pivot] + my_sort(right)
```
Recursively sort the `left` and `right` arrays until they cannot be sorted, keep the `pivot` sandwiched between them (since all values to the `right` are greater than `pivot`, and all values to the `left` are less than or equal to `pivot`)
