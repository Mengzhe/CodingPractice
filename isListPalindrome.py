# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if not l:
        return True

    len_ = 0
    node = l
    while node:
        node = node.next
        len_ += 1

    if len_ == 1:
        return True

    # print("len_", len_)
    steps = (len_ - 1) // 2
    # print("steps",steps)
    node = l
    for _ in range(steps):
        node = node.next
    l2 = node.next
    node.next = None

    # print("l2", l2.value)
    def reverseList(head):
        cur = head
        prev = None
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        return prev

    rev_l2 = reverseList(l2)

    node1 = l
    node2 = rev_l2
    while node1 and node2:
        if node1.value != node2.value:
            return False
        node1 = node1.next
        node2 = node2.next
    return True


