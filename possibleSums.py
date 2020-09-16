def possibleSums(coins, quantity):
    n = len(coins)
    dp = set([0])
    for i in range(n):
        coin = coins[i]
        cnt = quantity[i]
        for v in dp.copy():
            for k in range(cnt):
                dp.add(v + (k + 1) * coin)

    return len(dp) - 1