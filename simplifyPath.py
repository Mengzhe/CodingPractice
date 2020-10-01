def simplifyPath(path):
    cur = ''
    res = []
    n = len(path)
    i = 0
    while i<n:
        if path[i].isalpha():
            cur += path[i]
            i += 1
        elif path[i] == '.':
            if i+1<n and path[i+1] == '.':
                if len(res)>0:
                    res.pop()
            elif i+1<n and path[i+1].isalpha():
                cur += path[i]
            i += 1
        else:
            if len(cur)>0:
                res.append(cur)
            cur = ''
            i += 1
    # print(res)
    if len(cur)>0:
        res.append(cur)
    return '/'+'/'.join(res)