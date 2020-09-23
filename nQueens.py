def nQueens(n):
    res = []

    def isValid(offset, cur):
        for i in range(offset):
            diff = abs(cur[offset] - cur[i])
            if diff == 0 or diff == offset - i:
                return False
        return True

    def helper(offset, cur):
        if offset == n:
            res.append(cur.copy())
            return

        for i in range(1, n + 1):
            cur[offset] = i
            if isValid(offset, cur):
                helper(offset + 1, cur)
            cur[offset] = 0

    cur = [0] * n
    helper(0, cur)
    return res