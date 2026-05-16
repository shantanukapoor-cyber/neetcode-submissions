class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None       # store the complete word at end nodes

class Solution:
    def findWords(self, board, words):
        # Step 1: Build trie from word list
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word       # so we know which word we found

        # Step 2: Backtrack on board, carrying trie position
        m, n = len(board), len(board[0])
        result = []

        def backtrack(row, col, node):
            char = board[row][col]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.is_end:
                result.append(next_node.word)
                next_node.is_end = False   # avoid recording same word twice

            # Mark visited
            board[row][col] = '#'          # choose (in-place, avoids set overhead)

            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    backtrack(nr, nc, next_node)

            board[row][col] = char         # unchoose

        # Step 3: Start from every cell
        for i in range(m):
            for j in range(n):
                backtrack(i, j, root)

        return result