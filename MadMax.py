## https://binarysearch.com/problems/Mad-Max
from collections import deque
class Solution:
    def solve(self, nums, k):
        q = deque()
        dq = deque()
        res = []
        for i, x in enumerate(nums):
            q.append(x)
            while len(dq) > 0 and dq[-1] < x:
                dq.pop()
            dq.append(x)
            if len(q) == k:
                res.append(dq[0])
                v = q.popleft()
                if v == dq[0]:
                    dq.popleft()
            # print(i, dq)
        return res