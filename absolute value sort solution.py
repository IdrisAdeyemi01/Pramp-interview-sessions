def absSort(arr):
  arr.sort()
  
  arr2 = [abs(i) for i in arr]

  new_list = []
  for i in range(len(arr)):
    n = min(arr2)
   
    if -n in arr:
      new_list.append(arr[arr.index(-n)])
      arr.remove(-n)
    else:
      new_list.append(arr[arr.index(n)])
      arr.remove(n)
      
    arr2.remove(n)
    
    
    
  return new_list
