def get_different_number(arr):
  #(ARR) 4, 6
  arr = sorted(arr)
  if arr[0] != 0:
    return 0
  l_o_m = []
  for I in range(len(arr)-1):
    if arr[I+1] == arr[I] + 1: # 1 == 1
      continue 
    else:
      l_o_m.append(arr[I] +1)
      
  if len(l_o_m) == 0:
    return arr[-1] + 1
  else:
    return min(l_o_m)
