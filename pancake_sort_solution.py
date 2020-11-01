def pancake_sort(arr):
  
  for i in arr:
    k = arr.index(min(arr))
    new_arr = flip(arr,k)
  
  return new_arr


def flip(arr, k):
  rev = arr[:k:]
  rev.reverse()
  return rev + arr[k:]

arr = [1, 5, 4, 3, 2]
print(pancake_sort(arr))
