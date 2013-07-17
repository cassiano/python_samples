# n = index of the last heap element.
# i = index of the current heap element.

def parent_index(i):  return (i - 1) / 2
def parent(heap, i):  return heap[parent_index(i)]

def left_index(i, n): return 2 * i + 1 if 2 * i + 1 <= n else None
def left(heap, i, n): return heap[left_index(i, n)] if left_index(i, n) else None

def right_index(i, n):  return 2 * i + 2 if 2 * i + 2 <= n else None
def right(heap, i, n):  return heap[right_index(i, n)] if right_index(i, n) else None

def swap(heap, i, j): heap[i], heap[j] = heap[j], heap[i]

def heapify_up(heap, i):
  if i == 0 or parent(heap, i) >= heap[i]: return
  swap(heap, i, parent_index(i))
  heapify_up(heap, parent_index(i))

def heapify_down(heap, i, n):
  # Return if no child is greater than the current element or if no children at all.
  if (not left(heap, i, n) or heap[i] >= left(heap, i, n)) and (not right(heap, i, n) or heap[i] >= right(heap, i, n)): return

  max_child = max(left(heap, i, n), right(heap, i, n))                                      # Locate the maximum child.
  child_index = left_index(i, n) if max_child == left(heap, i, n) else right_index(i, n)    # Locate its index.
  swap(heap, i, child_index)                                                                # Swap the current node with the above child.
  heapify_down(heap, child_index, n)                                                          # Heapify the swaped child.

def heapsort(collection):
  if len(collection) <= 1: return

  # Heapify the collection up, starting with index 2.
  for k in range(1, len(collection)):
    heapify_up(collection, k)
  
  print('-- After Heapification -----------')
  print(collection)

  # Heapify the collection down.
  for k in range(len(collection) - 1):
    swap(a, 0, len(collection) - k - 1)
    heapify_down(collection, 0, (len(collection) - k - 1) - 1)

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
