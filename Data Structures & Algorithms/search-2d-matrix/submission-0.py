class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)*len(matrix[0])-1
        while left <= right:
            middle = left + (right - left)//2
            m1 = middle // len(matrix[0])
            m2 = middle % len(matrix[0])
            if matrix[m1][m2] < target:
                left = middle + 1
            elif matrix[m1][m2] > target:
                right = middle - 1
            else:
                return True
        return False 