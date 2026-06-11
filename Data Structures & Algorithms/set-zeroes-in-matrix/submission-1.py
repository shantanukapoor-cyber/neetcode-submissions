class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # for (i, j) = 0
        # do all i, z and z, j 0.
        m, n = len(matrix), len(matrix[0])
        def zero(i, j):
            for z in range(n):
                if matrix[i][z] != 0:
                    matrix[i][z] = -1
            for z in range(m):
                if matrix[z][j] != 0:
                    matrix[z][j] = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero(i, j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

        