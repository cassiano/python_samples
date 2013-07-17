# n = index of the last heap element.
# i = index of the current heap element.

def parent(i):        return (i - 1) / 2
def left(i, n):       return 2 * i + 1 if 2 * i + 1 <= n else None
def right(i, n):      return 2 * i + 2 if 2 * i + 2 <= n else None
def swap(heap, i, j): heap[i], heap[j] = heap[j], heap[i]

def heapify_up(heap, i):
  if i > 0 and heap[parent(i)] < heap[i]:
    swap(heap, i, parent(i))
    heapify_up(heap, parent(i))

def heapify_down(heap, i, n):
  largest = i
  
  if left(i, n)  and heap[left(i, n)]  > heap[largest]: largest = left(i, n)
  if right(i, n) and heap[right(i, n)] > heap[largest]: largest = right(i, n)
  
  if largest != i:
    swap(heap, i, largest)
    heapify_down(heap, largest, n)

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
  
  COUNT     = 10
  MAX_VALUE = 99

  a = []
  for _ in range(COUNT): a.append(random.randint(0, MAX_VALUE))

  print('-- Original Array -----------')
  print(a)

  heapsort(a)

  print('-- Sorted Array -----------')
  print(a)
