def countClouds(skyMap):
    res = 0
    m = len(skyMap)
    if m == 0:
        return 0
    n = len(skyMap[0])
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def helper(x, y):
        for d in dirs:
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < m and 0 <= next_y < n and skyMap[next_x][next_y] == '1':
                skyMap[next_x][next_y] = '0'
                helper(next_x, next_y)

    for i in range(m):
        for j in range(n):
            if skyMap[i][j] == '1':
                res += 1
                helper(i, j)
    return res