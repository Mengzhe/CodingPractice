def climbingStaircase(n, k):
    res = []

    def helper(steps, cur):
        if steps < 0:
            return
        if steps == 0:
            res.append(cur.copy())
            return

        for i in range(1, k + 1):
            helper(steps - i, cur + [i])

    helper(n, [])
    return res