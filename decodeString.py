def decodeString(s):
    def helper(s):
        # print(s)
        i = 0
        n = len(s)
        cur_num = 0
        res = []
        cur = ''
        while i < n:
            if s[i].isdigit():
                if len(cur) > 0:
                    res.append(cur)
                    cur = ''
                cur_num = cur_num * 10 + int(s[i])
                i += 1
            elif s[i] == '[':
                j = i
                cnt = 0
                while j < n:
                    if s[j] == '[':
                        cnt += 1
                    elif s[j] == ']':
                        cnt -= 1
                    if cnt == 0:
                        break
                    j += 1
                temp = helper(s[i + 1:j]) * cur_num
                res.append(temp)
                cur_num = 0
                i = j + 1
            else:
                cur += s[i]
                i += 1
        if len(cur):
            res.append(cur)
        # print(res, "cur_num", cur_num)
        if cur_num > 1:
            return ''.join(res) * cur_num
        else:
            return ''.join(res)

    return helper(s)



