from heapq import heappush, heappop
from collections import defaultdict
def nightRoute(city):
    n = len(city)
    visited = set()
    pq = []
    heappush(pq, (0, 0))
    while len(pq)>0:
        cur_cost, node = heappop(pq)
        if node == n-1:
            return cur_cost
        if node in visited: continue
        visited.add(node)
        for next_ in range(n):
            if city[node][next_]==-1: continue
            heappush(pq, (cur_cost+city[node][next_], next_))
    return -1