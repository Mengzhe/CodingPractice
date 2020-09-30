def combinationSum(a, sum):
    a = list(set(a))  ## remove duplicates; since elements can be used multiple times
    a.sort()
    res = []

    def helper(offset, cur, cur_sum):
        if cur_sum > sum:
            return
        if offset == len(a):
            if cur_sum == sum:
                res.append(cur.copy())
            return

        ## case 1
        helper(offset + 1, cur, cur_sum)

        ## case 2
        helper(offset, cur + [a[offset]], cur_sum + a[offset])

    helper(0, [], 0)
    # print(res)
    if len(res) == 0:
        return "Empty"
    else:
        res.sort()
        # print(res)
        ans = []
        for ls in res:
            ans.append('(' + ' '.join(map(str, ls)) + ')')
        return ''.join(ans)