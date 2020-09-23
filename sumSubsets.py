def sumSubsets(arr, num):
    res = []

    def helper(offset, cur_sum, cur):
        if cur_sum > num:  ## All numbers (including num) will be positive integers.
            return
        if offset == len(arr) and cur_sum == num:
            res.append(cur.copy())
            return
        elif cur_sum == num:
            res.append(cur.copy())
            return

        visited = set()
        for i in range(offset, len(arr)):
            if arr[i] in visited: continue
            visited.add(arr[i])
            helper(i + 1, cur_sum + arr[i], cur + [arr[i]])

    helper(0, 0, [])
    return sorted(res)


