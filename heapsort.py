def parent_index(n):      return (n - 1) / 2
def parent(heap, n):      return heap[parent_index(n)]
def left_index(n, tail):  return 2 * n + 1 if 2 * n + 1 <= tail else None
def left(heap, n, tail):  return heap[left_index(n, tail)] if left_index(n, tail) else None
def right_index(n, tail): return 2 * n + 2 if 2 * n + 2 <= tail else None
def right(heap, n, tail): return heap[right_index(n, tail)] if right_index(n, tail) else None
def swap(heap, n, m):     heap[n], heap[m] = heap[m], heap[n]

def heapify_down(heap, n):
  if n == 0 or parent(heap, n) >= heap[n]: return
  swap(heap, n, parent_index(n))
  heapify_down(heap, parent_index(n))

def heapify_up(heap, n, tail):
  li = left_index(n, tail)
  l  = left(heap, n, tail)
  ri = right_index(n, tail)
  r  = right(heap, n, tail)
  
  if (not li or heap[n] >= l) and (not ri or heap[n] >= r): return
  
  max_child = max(l, r)
  child_index = li if max_child == l else ri
  swap(heap, n, child_index)
  heapify_up(heap, child_index, tail)

if __name__ == '__main__':
  import random
  
  COUNT     = 20
  MAX_VALUE = 99

  a = []
  for i in range(COUNT): a.append(random.randint(0, MAX_VALUE))

  print('-- Original Array -----------')
  print(a)

  for i in range(1, len(a)):
    heapify_down(a, i)
  
  print('-- After Heapification -----------')
  print(a)

  for i in range(len(a) - 1):
    swap(a, 0, len(a) - i - 1)
    heapify_up(a, 0, (len(a) - i - 1) - 1)

    # print('-- After pass %d -----------' % i)
    # print(a)

  print('-- Sorted Array -----------')
  print(a)
