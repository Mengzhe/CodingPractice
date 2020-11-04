from heapq import heappush, heappop
from collections import defaultdict


def computerNetwork(n, network):
    graph = defaultdict(lambda: defaultdict(int))
    for from_, to_, weight in network:
        graph[from_][to_] = weight
        graph[to_][from_] = weight

    pq = []
    heappush(pq, (0, 1))
    visited = set()
    while len(pq) > 0:
        cur_cost, node = heappop(pq)
        # print("cur_cost", cur_cost, "node", node)
        if node == n:
            return cur_cost
        if node in visited: continue
        visited.add(node)
        for next_ in graph[node]:
            heappush(pq, (cur_cost + graph[node][next_], next_))
    return -1