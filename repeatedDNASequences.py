def repeatedDNASequences(s):
    ## roling hash
    if len(s) < 10:
        return []
    power = pow(26, 9)
    m = {}
    res = set()
    cur_hash = 0
    for i in range(9):
        cur_hash = cur_hash * 26 + ord(s[i]) - ord('A')

    for i in range(9, len(s)):
        cur_hash = cur_hash * 26 + ord(s[i]) - ord('A')
        if cur_hash in m:
            res.add(m[cur_hash])
        else:
            m[cur_hash] = s[i - 9:i + 1]
        cur_hash = cur_hash - (ord(s[i - 9]) - ord('A')) * power

    return sorted(list(res))