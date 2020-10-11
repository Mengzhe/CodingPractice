# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    dummy = ListNode(-1)
    prev = dummy
    while l1 or l2:
        v1 = l1.value if l1 else float('inf')
        v2 = l2.value if l2 else float('inf')
        if v1 <= v2:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    return dummy.next

