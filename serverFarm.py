from heapq import heappush, heappop
def serverFarm(jobs, servers):
    ls = [[time, index] for index, time in enumerate(jobs)]
    ls.sort(key=lambda x: (-x[0], x[1]))
    # print(ls)
    pq = []
    for i in range(servers):
        heappush(pq, (0, i))

    res = [[] for _ in range(servers)]
    for time, idx in ls:
        cum_time, server_id = heappop(pq)
        res[server_id].append(idx)
        cum_time += time
        heappush(pq, (cum_time, server_id))

    return res
