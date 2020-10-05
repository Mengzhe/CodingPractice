class myStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        if len(self.st) == 0:
            self.st.append((x, x))
        else:
            if x < self.st[-1][1]:
                self.st.append((x, x))
            else:
                self.st.append((x, self.st[-1][1]))

    def min_(self):
        return self.st[-1][1]

    def pop(self):
        self.st.pop()


def minimumOnStack(operations):
    st = myStack()
    res = []
    for op in operations:
        op = op.split()
        if op[0] == 'push':
            st.push(int(op[1]))
        elif op[0] == 'pop':
            st.pop()
        else:
            res.append(st.min_())
    return res