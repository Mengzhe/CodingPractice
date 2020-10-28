from collections import defaultdict
from datetime import datetime

def dailyOHLC(timestamp, instrument, side, price, size):
    n = len(timestamp)
    m = defaultdict(lambda: defaultdict(list))
    for i in range(n):
        date = datetime.utcfromtimestamp(timestamp[i]).strftime('%Y-%m-%d')
        # print(date)
        company = instrument[i]
        m[company][date].append(price[i])

    # print(m)
    res = []
    for company in m:
        for date in m[company]:
            high, low = max(m[company][date]), min(m[company][date])
            open_, close_ = m[company][date][0], m[company][date][-1]
            res.append([date, company,
                        '{:0.2f}'.format(open_), '{:0.2f}'.format(high),
                        '{:0.2f}'.format(low), '{:0.2f}'.format(close_)])

    res.sort(key=lambda x: (x[0], x[1]))
    return res