## Trie-based solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isWord = True


def wordBoggle(board, words):
    dirs = [[0, 1], [0, -1], [1, 0], [1, -1], [1, 1], [-1, 0], [-1, 1], [-1, -1]]
    m = len(board)
    n = len(board[0])

    trie = Trie()
    for word in words:
        trie.add(word)

    def helper(x, y, node, cur_path):
        if node.isWord:
            res.add(''.join(cur_path))

        for d in dirs:
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < m and 0 <= next_y < n and board[next_x][next_y] in node.children:
                c = board[next_x][next_y]
                board[next_x][next_y] = '#'
                helper(next_x, next_y, node.children[c], cur_path + [c])
                board[next_x][next_y] = c

    res = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie.root.children:
                c = board[i][j]
                helper(i, j, trie.root.children[c], [c])
                board[i][j] = c
    return sorted(list(res))


