class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # word path can be either straight down or turn left or right or up.
        # if I am at word[0]. my current block must match word[0] and next v is word[1]
        # if I am at word[2]. my current match word[2] and next valid move is word[3]
        # if not return False.
        # if next path outside the board also return false.
        # if we are at last index and match happened then return True
        m, n = len(board), len(board[0])
        
        def search(index, row, column):
            # bounds check.
            if row > m-1 or row < 0 or column > n-1 or column < 0:
                return False
            if (row, column) in visited:
                return False
            # current element matches, then check surroundings.
            if board[row][column] == word[index]:
                visited.add((row, column))
                # if current is last means match
                if len(word) - 1 == index:
                    return True
                left = search(index + 1, row, column - 1)
                right = search(index + 1, row, column + 1)
                up = search(index + 1, row - 1, column)
                down = search(index + 1, row + 1, column)
                visited.remove((row, column))
                return left or right or up or down
                
        for i in range(m):
            for j in range(n):
                visited = set()
                if search(0, i, j):
                    return True
        return False
