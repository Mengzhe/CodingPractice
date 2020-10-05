def nextLarger(a):
    n = len(a)
    st = []
    res = [None] * n
    for i in range(n - 1, -1, -1):
        while len(st) > 0 and st[-1] < a[i]:
            st.pop()

        if len(st) == 0:
            res[i] = -1
        else:
            res[i] = st[-1]

        st.append(a[i])

    return res