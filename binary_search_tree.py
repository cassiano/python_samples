from collections import deque

class Tree(object):
  def __init__(self, root, left = None, right = None):
    self.root  = root
    self.left  = left
    self.right = right
    
  def contains(self, searched_value):
    if searched_value == self.root:
      found = True
    elif searched_value <= self.root:
      found = self.left and self.left.contains(searched_value)
    else:    # searched_value > self.root
      found = self.right and self.right.contains(searched_value)
      
    return found
    
  def add(self, new_value):
    if new_value <= self.root:
      if not self.left:
        self.left = Tree(new_value)
      else:
        self.left.add(new_value)
    else:   # new_value > self.root
      if not self.right:
        self.right = Tree(new_value)
      else:
        self.right.add(new_value)

  def pprint(self, spaces = 0):
    # Print the root.
    print(' ' * spaces + 'Root: %d' % self.root)

    # Print the left subtree, if any.
    if self.left: 
      print(' ' * spaces + 'Left:')
      self.left.pprint(spaces + 2)

    # Print the right subtree, if any.
    if self.right: 
      print(' ' * spaces + 'Right:')
      self.right.pprint(spaces + 2)
  
  # OO __repr__
  # def __repr__(self):
  #   result = '(Root: %s' % self.root
  #   
  #   if self.left : result += ', Left:  %s' % self.left
  #   if self.right: result += ', Right: %s' % self.right
  #     
  #   result += ')'
  #   
  #   return result

  # Procedural __repr__
  def __repr__(self):
    def _repr(self):
      return '[%s %d %s]' % (_repr(self.left), self.root, _repr(self.right)) if self else ''
      
    return _repr(self)

  def gprint(self):
    def string_splice(str, start, end, value, fill_char = ' '):
      if len(str) < end: str = str + fill_char * (end - len(str))
      return str[:start] + value + str[(end+1):]
      
    NODE_LENGTH = 2

    queue = deque()
    queue.appendleft({ 'node': self, 'level': 1, 'inherited_padding': 0, 'parent_position': None })

    node_rows  = []
    arrow_rows = []

    while len(queue) > 0:
      current = queue.popleft()

      # TODO: check if Python supports destructuring assignments for hash objects, as does CoffeeScript (see the 'deeply nested properties' example in http://coffeescript.org/#destructuring).
      node              = current['node']
      level             = current['level']
      inherited_padding = current['inherited_padding']
      parent_position   = current['parent_position']

      # Calculate the relative (left) padding for the current node, based on the width (which equals its node count) of its left sub-tree, if any.
      relative_padding = node.left.count() if node.left else 0

      # Make room for new node and arrow rows, when applicable.
      if len(node_rows)  < level:     node_rows.append('')
      if len(arrow_rows) < level - 1: arrow_rows.append('')

      # Format the current node's root value.
      root = ('%0' + str(NODE_LENGTH) + 'd') % node.root

      # Calculate the necessary (left) padding for the current node, adding its inherited plus its own (left) padding.
      position = (inherited_padding + relative_padding) * NODE_LENGTH

      # Place the / or \ arrow for the current node, "pointing" to its parent.
      if parent_position == 'left':
        index      = position + NODE_LENGTH / 2 - 1
        arrow_char = '\\'
      elif parent_position == 'right':
        index      = position + NODE_LENGTH / 2
        arrow_char = '/'
      
      if parent_position: 
        arrow_rows[level - 2] = string_splice(arrow_rows[level - 2], index, index, arrow_char)
      
      # Add the current node to the current row, at the proper position.
      node_rows[level - 1] = string_splice(node_rows[level - 1], position, position + len(root) - 1, root)
      
      if node.left : queue.append({ 'node': node.left,  'level': level + 1, 'inherited_padding': inherited_padding,                         'parent_position': 'right'  })
      if node.right: queue.append({ 'node': node.right, 'level': level + 1, 'inherited_padding': inherited_padding + relative_padding + 1,  'parent_position': 'left'   })
    
    # Print the tree, prefixing each row with its level.
    for i, node_row in enumerate(node_rows):
      level_info = '(%2d)   ' % (i + 1)
      
      # Print the arrow row, starting with level 2.
      if i > 0: print(' ' * len(level_info) + '%s' % arrow_rows[i - 1])
      
      # Print the node row.
      print('%s%s' % (level_info, node_row))

  # Depth-first traversal.
  def traverse_depth_first(self, visitor, order = 'pre-order'):
    if order == 'pre-order': visitor(self)
    if self.left: self.left.traverse_depth_first(visitor, order)
    if order == 'in-order': visitor(self)
    if self.right: self.right.traverse_depth_first(visitor, order)
    if order == 'post-order': visitor(self)

  def traverse_breadth_first(self, visitor):
    queue = deque()
    queue.appendleft(self)
    
    while len(queue) > 0:
      node = queue.popleft()
      visitor(node)
      
      if node.left : queue.append(node.left)
      if node.right: queue.append(node.right)

  def is_leaf(self):
    return not self.left and not self.right

  def height(self):
    if self.is_leaf(): return 1
    
    left_height  = self.left.height()  if self.left  else 0
    right_height = self.right.height() if self.right else 0
    
    return max(left_height, right_height) + 1

  def procedural_height(self):
    def _procedural_height(tree):
      return 0 if not tree else max(_procedural_height(tree.left), _procedural_height(tree.right)) + 1
    
    return _procedural_height(self)

  def count(self):
    if self.is_leaf(): return 1

    left_count  = self.left.count()  if self.left  else 0
    right_count = self.right.count() if self.right else 0

    return left_count + right_count + 1

  def procedural_count(self):
    def _procedural_count(tree):
      return 0 if not tree else _procedural_count(tree.left) + _procedural_count(tree.right) + 1
    
    return _procedural_count(self)

  def procedural_max(self):
    def _procedural_max(tree):
      return -float('inf') if not tree else max(tree.root, _procedural_max(tree.left), _procedural_max(tree.right))
      
    return _procedural_max(self)

if __name__ == '__main__':
  import random
  import sys
  
  if sys.version_info < (3,): range = xrange
      
  TOTAL_NODES = 40
  MAX_VALUE   = 99
  
  # Populate the tree with TOTAL_NODES random integers (from 1 to MAX_VALUE).
  tree = Tree(random.randint(1, MAX_VALUE))
  for _ in range(TOTAL_NODES - 1): tree.add(random.randint(1, MAX_VALUE))

  # Populate the tree top-down. Check graphical versions in https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree.
  # tree = Tree(50)
  # for value in [17, 12, 9, 14, 23, 19, 72, 54, 67, 76]:
  #   tree.add(value)

  # Populate the tree bottom-up.
  # tree1  = Tree(1)
  # tree3  = Tree(3, tree1)
  # tree10 = Tree(10)
  # tree8  = Tree(8, right = tree10)
  # tree6  = Tree(6)
  # tree7  = Tree(7, tree6, tree8)
  # tree   = Tree(5, tree3, tree7)
  
  # Pretty print it (in pre-order). For tree traversal modes, see: http://en.wikipedia.org/wiki/Tree_traversal.
  print('-- Pretty Print -----------')
  tree.pprint()

  print('-- Using __repr__ -----------')
  print(tree)

  print('-- Searches -----------')
  for i in range(1, tree.procedural_max() + 1):
    print('%d: %s' % (i, '*' if tree.contains(i) else ''))

  def visitor(tree): 
    print(tree.root)

  print('-- Pre-order Depth-first Traversal -----------')
  tree.traverse_depth_first(visitor)
  print('-- In-order Depth-first Traversal -----------')
  tree.traverse_depth_first(visitor, 'in-order')
  print('-- Post-order Depth-first Traversal -----------')
  tree.traverse_depth_first(visitor, 'post-order')

  print('-- Breadth-first Traversal -----------')
  tree.traverse_breadth_first(visitor)

  print('-- Height -----------')
  print(tree.height())

  print('-- (Procedural) Height -----------')
  print(tree.procedural_height())

  print('-- Count -----------')
  print(tree.count())

  print('-- (Procedural) Count -----------')
  print(tree.procedural_count())

  print('-- (Procedural) Max -----------')
  print(tree.procedural_max())

  print('-- G(raphical) Print -----------')
  print(tree.gprint())
