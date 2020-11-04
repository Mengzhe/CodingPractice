import math
def perfectCity(departure, destination):
    x1, y1 = departure
    x2, y2 = destination
    res = float('inf')

    if x1 == int(x1):
        opt1 = y1 - math.floor(y1)
        opt2 = math.ceil(y1) - y1
        if x2 == int(x2):
            res = min(opt1 + abs(x2 - x1) + abs(math.floor(y1) - y2),
                      opt2 + abs(x2 - x1) + abs(math.ceil(y1) - y2))
        else:
            opt3 = x2 - math.floor(x2)
            opt4 = math.ceil(x2) - x2
            res = min(opt1 + abs(x1 - math.floor(x2)) + abs(math.floor(y1) - y2) + opt3,
                      opt1 + abs(x1 - math.ceil(x2)) + abs(math.floor(y1) - y2) + opt4,
                      opt2 + abs(x1 - math.floor(x2)) + abs(math.ceil(y1) - y2) + opt3,
                      opt2 + abs(x1 - math.ceil(x2)) + abs(math.ceil(y1) - y2) + opt4,
                      )
    else:
        return perfectCity((departure[1], departure[0]), (destination[1], destination[0]))
    return res

## [2.4, 1], [5, 7.3]