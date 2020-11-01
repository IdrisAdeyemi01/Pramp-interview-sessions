import numpy as np

def array_of_array_products(arr):
  
  if len(arr) <= 1:
    return []  
  i = 0
  li = []
  while i < len(arr):
    m = arr[0]
    print(m)
    arr.pop(0)
    n = np.prod(arr)
    
    arr.append(m)
    print(arr)
    li.append(n)
    print(li)
    i += 1
  return li


arr = [8, 10, 2]
print(array_of_array_products(arr))
