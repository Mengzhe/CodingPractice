def bomber(field):
    m = len(field)
    if m == 0:
        return 0
    n = len(field[0])
    up = [[0 for j in range(n)] for i in range(m)]
    down = [[0 for j in range(n)] for i in range(m)]
    left = [[0 for j in range(n)] for i in range(m)]
    right = [[0 for j in range(n)] for i in range(m)]

    ## up
    for j in range(n):
        cur = 0
        for i in range(1, m):
            if field[i - 1][j] == 'E':
                cur += 1
            elif field[i - 1][j] == 'W':
                cur = 0
            up[i][j] = cur

    ## down
    for j in range(n):
        cur = 0
        for i in range(m - 2, -1, -1):
            if field[i + 1][j] == 'E':
                cur += 1
            elif field[i + 1][j] == 'W':
                cur = 0
            down[i][j] = cur

    ## left
    for i in range(m):
        cur = 0
        for j in range(1, n):
            if field[i][j - 1] == 'E':
                cur += 1
            elif field[i][j - 1] == 'W':
                cur = 0
            left[i][j] = cur

    ## right
    for i in range(m):
        cur = 0
        for j in range(n - 2, -1, -1):
            if field[i][j + 1] == 'E':
                cur += 1
            elif field[i][j + 1] == 'W':
                cur = 0
            right[i][j] = cur

    # for i in range(m):
    #     print(right[i])
    res = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == '0':
                res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])
    return res