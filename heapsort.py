a = [2, 4, 1, 5, 0, 3]

def parent_index(n):  return (n - 1) / 2
def parent(heap, n):  return heap[parent_index(n)]
def left_index(n):    return 2 * n + 1
def left(heap, n):    return heap[left_index(n)]
def right_index(n):   return 2 * n + 2
def right(heap, n):   return heap[right_index(n)]
def swap(heap, n, m): heap[n], heap[m] = heap[m], heap[n]

def heapify(heap, n):
  if n == 0 or parent(heap, n) >= heap[n]: return
  swap(heap, n, parent_index(n))
  heapify(heap, parent_index(n))

# TODO: find a better method name.  
def unheapify(heap, n, last_index):
  if (left_index(n) > last_index or heap[n] >= left(heap, n)) and (right_index(n) > last_index or heap[n] >= right(heap, n)): return
  
  max_child = max(left(heap, n), right(heap, n))
  child_index = left_index(n) if max_child == left(heap, n) else right_index(n)
  swap(heap, n, child_index)
  unheapify(heap, child_index, last_index)

print(a)

for i in range(1, len(a)):
  heapify(a, i)
  
print(a)

for i in range(len(a) - 1):
  swap(a, 0, len(a) - 1 - i)
  unheapify(a, 0, (len(a) - i - 1) - 1)

print(a)
