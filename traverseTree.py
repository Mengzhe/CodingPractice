#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque
def traverseTree(t):
    if not t:
        return []
    q = deque()
    q.append(t)
    res = []
    while len(q)>0:
        q_sz = len(q)
        for _ in range(q_sz):
            node = q.popleft()
            res.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res