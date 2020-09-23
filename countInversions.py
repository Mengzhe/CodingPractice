def countInversions(nums):
    ## same solution as countSmallerToTheRight.py
    ## based on merge sort
    M = 10 ** 9 + 7
    res = 0
    def merge(left_part, right_part):
        res = []
        i = 0
        j = 0
        while i < len(left_part) or j < len(right_part):
            v_l = left_part[i] if i < len(left_part) else float('inf')
            v_r = right_part[j] if j < len(right_part) else float('inf')
            if v_l <= v_r:
                res.append(v_l)
                i += 1
            else:
                res.append(v_r)
                j += 1
        return res

    def helper(nums):
        nonlocal res
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums

        left_part = helper(nums[:n // 2])
        right_part = helper(nums[n // 2:])

        i = 0
        j = 0
        while i < len(left_part):
            while j < len(right_part) and left_part[i] > right_part[j]:
                j += 1
            res += j
            i += 1

        nums = merge(left_part, right_part)
        return nums

    nums = helper(nums)
    # print(nums)
    return res % M

