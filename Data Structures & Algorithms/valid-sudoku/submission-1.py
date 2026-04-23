class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows + columns
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

        # boxes
        for boxRow in range(3):
            for boxCol in range(3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        r = boxRow * 3 + i
                        c = boxCol * 3 + j
                        if board[r][c] != '.':
                            if board[r][c] in box_set:
                                return False
                            box_set.add(board[r][c])

        return True