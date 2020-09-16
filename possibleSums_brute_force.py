## brute-force: TLE
def possibleSums(coins, quantity):
    n = len(coins)
    res = set()

    def helper(offset, cur_sum):
        if offset == n:
            res.add(cur_sum)
            return
            ## case 1: do not take coins[offset]
        helper(offset + 1, cur_sum)

        ## case 2: take coins[offset]
        if quantity[offset] > 0:
            for k in range(1, quantity[offset] + 1):
                quantity[offset] -= k
                cur_sum += coins[offset] * k
                helper(offset + 1, cur_sum)
                quantity[offset] += k
                cur_sum -= coins[offset] * k

    helper(0, 0)
    # print(res)
    return len(res) - 1  ##  exclude 0