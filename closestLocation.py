def closestLocation(address, objects, names):
    candidates = set()
    n = len(address)
    address = address.lower()

    def differ_one(name):
        for i in range(n):
            # print(name[:i] + name[i+1:n], address[:i] + address[i+1:n])
            if name[:i] + name[i + 1:n] == address[:i] + address[i + 1:n]:
                return True
        return False

    # print(differ_one('aat'))

    def extra_one(name):
        for i in range(n):
            if name[:n - 1] == address[:i] + address[i + 1:n]:
                return True
        return False

    # print(extra_one('at avenue'))

    def missing_one(name):
        for i in range(n + 1):
            # print(name[:i] + name[i+1:n+1])
            if name[:i] + name[i + 1:n + 1] == address:
                return True
        return False

    # print(missing_one('csat exhibition'))

    def dist_points(p):
        return p[0] ** 2 + p[1] ** 2

    def dist_segment(seg):
        if seg[0] == seg[2]:
            if seg[1] <= 0 <= seg[3]:
                return seg[0] ** 2
            return min(dist_points(seg[:2]), dist_points(seg[2:]))
        else:
            if seg[0] <= 0 <= seg[2]:
                return seg[1] ** 2
            return min(dist_points(seg[:2]), dist_points(seg[2:]))

    for i, name in enumerate(names):
        name = name.lower()

        ## the typed in address is identical to the prefix of the object's address;
        if name[:n] == address:
            candidates.add(i)
        ## they differ only by one symbol;
        elif differ_one(name):
            candidates.add(i)
        ## user's input has one extra symbol;
        elif extra_one(name):
            candidates.add(i)
        ## user's input has one missing symbol.
        elif missing_one(name):
            candidates.add(i)
    # print(candidates)
    cur_dist = float('inf')
    res = None
    # for idx in candidates:
    for i in range(len(names)):
        if i not in candidates: continue
        if len(objects[i]) == 2:
            d = dist_points(objects[i])
        else:
            d = dist_segment(objects[i])

        if d < cur_dist:
            cur_dist = d
            res = i
    return names[res]





