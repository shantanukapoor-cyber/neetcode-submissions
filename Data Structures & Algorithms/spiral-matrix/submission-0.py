class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        answer = []
        
        while top < bottom and left < right:
            # Go Right
            for col in range(left, right):
                answer.append(matrix[top][col])
            top += 1
            
            # Go Down
            for row in range(top, bottom):
                answer.append(matrix[row][right - 1])
            right -= 1
            
            # Make sure we still have valid rows before going Left
            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    answer.append(matrix[bottom - 1][col])
                bottom -= 1
                
            # Make sure we still have valid columns before going Up
            if left < right:
                for row in range(bottom - 1, top - 1, -1):
                    answer.append(matrix[row][left])
                left += 1
                
        return answer