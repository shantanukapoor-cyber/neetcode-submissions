class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # semiring is extend and boolean.
        # for each O, if all four sides reach X before the border.
        # change to x.
        # 
        if not board:
            return
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if board[r][c] != "O":
                return
            board[r][c] = "S"
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)

        # for each row
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        # for each column
        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m-1][i] == "O":
                dfs(m-1, i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
    
