# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    dummy = ListNode(-1)
    dummy.next = l
    prev = dummy

    if k == 1:
        return l

    cur = tail = l
    while prev.next:
        tail = prev.next
        last = tail
        cur = tail.next
        for _ in range(k):
            if last is None:
                return dummy.next
            last = last.next

        while cur is not last:
            next_ = cur.next
            cur.next = prev.next
            prev.next = cur
            tail.next = next_
            cur = next_
        prev = tail

    return dummy.next