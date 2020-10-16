# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if n == 0:
        return l

    tail = l
    while tail.next:
        tail = tail.next
    # print("tail", tail.value)

    fast = l
    for _ in range(n + 1):
        if not fast:
            return l
        fast = fast.next

    slow = l
    while fast:
        fast = fast.next
        slow = slow.next

    # print("slow", slow.value)
    new_head = slow.next
    slow.next = None
    tail.next = l

    return new_head