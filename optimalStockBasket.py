def optimalStockBasket(stocks, riskBudget):
    n = len(stocks)
    res = 0

    def helper(offset, cur_return, cur_risk):
        nonlocal res
        if cur_risk > riskBudget:
            return
        if offset == n:
            res = max(res, cur_return)
            return

        ## not take this stock
        helper(offset + 1, cur_return, cur_risk)

        ret, risk = stocks[offset]
        ## take this stock
        helper(offset + 1, cur_return + ret, cur_risk + risk)

    helper(0, 0, 0)
    return res
