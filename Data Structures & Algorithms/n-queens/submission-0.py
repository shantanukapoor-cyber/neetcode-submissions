class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # each queen can attack in a up down left right diagonal.
        # so upon placing each queen some spots will become 
        # forcibly blank to maintain safety.
        # the remaining spots we will try placing the queen and moving forward.
        # if at any point the row contains no blank space it's a dead end.
        result = []
        # if queen is at i,j.
        # next row off limits are i+1, j and i + 1, j + 1
        # next to next are i+2, j, i+2, j+2.
        # so the addition is current row - queen row
        def isSafe(row, column, path):
            for i in range(len(path)):
                if path[i][column] == 'Q' or (column - (row - i) >= 0 and path[i][column - (row - i)] == 'Q') or (column + (row - i) < n and path[i][column + (row - i)] == 'Q'):
                    return False
            return True

        def queen_placement(row, path):
            if row == n:
                result.append(path[:])
                return
            for column in range(n):
                if isSafe(row, column, path): 
                    new_path = '.' * (column) + 'Q' + '.' * (n - column - 1)
                    path.append(new_path)
                    queen_placement(row + 1, path)
                    path.pop()
        queen_placement(0, [])
        return result