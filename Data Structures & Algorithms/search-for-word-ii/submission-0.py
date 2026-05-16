class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word  # end of word marker
        rows, cols = len(board), len(board[0])
        result = set()
        def backtrack(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            next_node = node[char]
            if '#' in next_node:
                result.add(next_node['#'])
            board[r][c] = '#'  # mark as visited
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                # check boundaries and if not visited
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    backtrack(nr, nc, next_node)
            board[r][c] = char  # unmark as visited
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie)
        return list(result)
    
        