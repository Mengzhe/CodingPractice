from collections import defaultdict
def areFollowingPatterns(strings, patterns):
    n = len(strings)

    m1 = defaultdict()
    m2 = defaultdict()
    for i in range(n):
        c = patterns[i]
        w = strings[i]
        if c in m1:
            if m1[c] != w:
                return False
        else:
            m1[c] = w
        if w in m2:
            if m2[w] != c:
                return False
        else:
            m2[w] = c
    return True