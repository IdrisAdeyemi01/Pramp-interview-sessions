def find_array_quadruplet(arr, target):
  if len(arr) < 4:
    return []
  
  arr.sort()
  if len(arr) == 4 and sum(arr) == target:
    return arr
  elif len(arr) == 4 and sum(arr) != target:
    return []
  
  arr = list(set(arr))
  
  arr2 = []
  for i in arr:
    for j in arr[arr.index(i)+1:]:    
      for k in arr[arr.index(j)+1:]:
        for l in arr[arr.index(k)+1:]:
          if i + j + k + l == target:
            arr2.append([i, j, k, l])
            
  
  if len(arr2) == 0:
    return []
  else:
    return arr2[0] # your code goes here
