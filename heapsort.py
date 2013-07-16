# n = index of the last heap element.
# i = index of the current heap element.

def parent_index(i):    return (i - 1) / 2
def parent(heap, i):    return heap[parent_index(i)]
def left_index(i, n):   return 2 * i + 1 if 2 * i + 1 <= n else None
def left(heap, i, n):   return heap[left_index(i, n)] if left_index(i, n) else None
def right_index(i, n):  return 2 * i + 2 if 2 * i + 2 <= n else None
def right(heap, i, n):  return heap[right_index(i, n)] if right_index(i, n) else None
def swap(heap, i, j):   heap[i], heap[j] = heap[j], heap[i]

def heapify_down(heap, i):
  if i == 0 or parent(heap, i) >= heap[i]: return
  swap(heap, i, parent_index(i))
  heapify_down(heap, parent_index(i))

def heapify_up(heap, i, n):
  left_idx    = left_index(i, n)
  left_value  = left(heap, i, n)
  right_idx   = right_index(i, n)
  right_value = right(heap, i, n)
  
  if (not left_idx or heap[i] >= left_value) and (not right_idx or heap[i] >= right_value): return
  
  max_child = max(left_value, right_value)
  child_idx = left_idx if max_child == left_value else right_idx
  swap(heap, i, child_idx)
  heapify_up(heap, child_idx, n)

def heapsort(collection):
  for k in range(1, len(collection)):
    heapify_down(collection, k)
  
  print('-- After Heapification -----------')
  print(collection)

  for k in range(len(collection) - 1):
    swap(a, 0, len(collection) - k - 1)
    heapify_up(collection, 0, (len(collection) - k - 1) - 1)

    # print('-- After pass %d -----------' % k)
    # print(collection)

if __name__ == '__main__':
  import random
  
  COUNT     = 50
  MAX_VALUE = 99

  a = []
  for _ in range(COUNT): a.append(random.randint(0, MAX_VALUE))

  print('-- Original Array -----------')
  print(a)

  heapsort(a)

  print('-- Sorted Array -----------')
  print(a)
