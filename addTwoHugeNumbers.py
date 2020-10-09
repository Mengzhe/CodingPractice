# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    def reverseList(head):
        prev = None
        cur = head
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        return prev

    a = reverseList(a)
    b = reverseList(b)

    node1 = a
    node2 = b
    carry = 0
    dummy = ListNode(-1)
    prev = dummy
    while node1 or node2:
        v1 = node1.value if node1 else 0
        v2 = node2.value if node2 else 0
        v = (v1 + v2 + carry) % 10000
        carry = (v1 + v2 + carry) // 10000
        node = ListNode(v)
        prev.next = node
        prev = node
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    # print("carry", carry)

    if carry:
        node = ListNode(carry)
        prev.next = node
        prev = node

    node = dummy.next
    # while node:
    #     print(node.value, end=' ')
    #     node = node.next
    # print('')

    res = reverseList(dummy.next)
    return res

