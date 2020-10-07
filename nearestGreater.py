def nearestGreater(a):
    n = len(a)
    left_ = [0] * n
    right_ = [0] * n

    st = []
    for i in range(n):
        while len(st) > 0 and a[st[-1]] <= a[i]:
            st.pop()
        if len(st) == 0:
            left_[i] = -1
        else:
            left_[i] = st[-1]
        st.append(i)
    # print(left_)
    for i in range(n - 1, -1, -1):
        while len(st) > 0 and a[st[-1]] <= a[i]:
            st.pop()
        if len(st) == 0:
            right_[i] = -1
        else:
            right_[i] = st[-1]
        st.append(i)
    # print(right_)
    st = []
    res = [0] * n
    for i in range(n):
        if left_[i] == -1 and right_[i] == -1:
            res[i] = -1
        elif left_[i] == -1 and right_[i] != -1:
            res[i] = right_[i]
        elif left_[i] != -1 and right_[i] == -1:
            res[i] = left_[i]
        else:
            if i - left_[i] <= right_[i] - i:
                res[i] = left_[i]
            else:
                res[i] = right_[i]
    return res
