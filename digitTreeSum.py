#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    res = 0

    def helper(node, cur):
        nonlocal res
        if node.left is None and node.right is None:
            res += cur * 10 + node.value
            return

        if node.left:
            helper(node.left, cur * 10 + node.value)
        if node.right:
            helper(node.right, cur * 10 + node.value)

    helper(t, 0)
    return res
