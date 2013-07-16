def qs(collection):
  if len(collection) <= 1:
    return collection
  
  pivot    = collection[0]
  lowest   = []
  greatest = []
  
  # Using a for loop (faster).
  # for element in collection[1:]:
  #   if element <= pivot:
  #     lowest.append(element)
  #   else:
  #     greatest.append(element)
  
  # Using list comprehensions (slower).
  lowest   = [element for element in collection[1:] if element <= pivot]
  greatest = [element for element in collection[1:] if element > pivot]
      
  return qs(lowest) + [pivot] + qs(greatest)
    
a = [3, 1, 4, 5, 0, 2, 1]
print(qs(a))
