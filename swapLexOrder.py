## hints:

# 1. Realize that swapping is transitive. If you can swap position 1 with 3, and 3 with 4, then it's possible to swap
# 1 with 4.

# 2. Knowing this you can create a graph in the form of an adjacency list (basic theory, easy to look up). The
# adjacency list basically shows that if I'm on position 1, here's all the other positions I would eventually be able
# to swap to. Positions in the string are basically nodes in a graph that are connected -- in this case conceptually
# connected by swaps.

# 3. Since all pairs aren't guaranteed to be connected, we need to figure out what the connected components are (more
# basic theory, easy to look up). Using DFS or BFS to create connected components is straightforward.

# 4. Once you have the connected components, you can iterate through them, grab the indices and sort them,
# get the characters at those positions and sort those, then reinsert them in reverse sorted order into those
# positions.

from collections import defaultdict


def swapLexOrder(str, pairs):
    graph = defaultdict(list)
    for edge in pairs:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    n = len(str)

    def dfs(cur, cur_visited):
        for next_ in graph[cur]:
            if next_ not in cur_visited:
                cur_visited.add(next_)
                dfs(next_, cur_visited)

    res = [None] * n
    visited = set()
    for i in range(n):
        if i not in visited:
            cur_visited = set()
            cur_visited.add(i)
            dfs(i, cur_visited)

            ## process this connected componenet
            chars = []
            for x in cur_visited:
                chars.append(str[x])
            chars.sort()
            # print(chars)
            for x in sorted(list(cur_visited)):
                res[x] = chars[-1]
                chars.pop()

        # print(cur_visited)
        visited |= cur_visited
        # print(visited)
    return ''.join(res)