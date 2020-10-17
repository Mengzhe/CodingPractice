#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque
def largestValuesInTreeRows(t):
    if not t:
        return []
    res = []
    q = deque()
    q.append(t)
    while len(q)>0:
        q_sz = len(q)
        cur_max = float('-inf')
        for _ in range(q_sz):
            node = q.popleft()
            cur_max = max(cur_max, node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(cur_max)
    return res
