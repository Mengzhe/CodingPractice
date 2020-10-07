## https://leetcode.com/problems/verbal-arithmetic-puzzle/
def isSolvable(words, result):
    ## my own bactrack solution: TLE
    m = {}
    idx = 0
    for word in words:
        for c in word:
            if c not in m:
                m[c] = idx
                idx += 1

    for c in result:
        if c not in m:
            m[c] = idx
            idx += 1

    vec = [-1] * len(m)

    def helper(offset, vec, used):
        if offset == len(vec):
            sum_words = 0
            sum_res = 0
            for word in words:
                cur_word = 0
                for i in range(len(word)):
                    c = word[i]
                    if i == 0 and vec[m[c]] == 0:
                        return False
                    cur_word = cur_word * 10 + vec[m[c]]
                sum_words += cur_word

            for i in range(len(result)):
                c = result[i]
                if i == 0 and vec[m[c]] == 0:
                    return False
                sum_res = sum_res * 10 + vec[m[c]]
            if sum_words == sum_res:
                print(vec)
                return True
            else:
                return False

        for i in range(10):
            if i not in used:
                vec[offset] = i
                used.add(i)
                if helper(offset + 1, vec, used):
                    return True
                vec[offset] = -1
                used.remove(i)
        return False

    return helper(0, vec, set())

words = ["THIS", "IS", "TOO"]
result = "FUNNY"
res = isSolvable(words, result)
print("res:", res)
# ["SEND", "MORE"]
# "MONEY"
# ["SIX", "SEVEN", "SEVEN"]
# "TWENTY"
# ["THIS", "IS", "TOO"]
# "FUNNY"
# ["LEET", "CODE"]
# "POINT"
