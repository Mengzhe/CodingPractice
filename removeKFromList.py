# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    dummy = ListNode(-1)
    dummy.next = l
    prev = dummy
    node = l
    while node:
        while node and node.value == k:
            node = node.next
        prev.next = node
        prev = node
        if node:
            node = node.next
    return dummy.next
