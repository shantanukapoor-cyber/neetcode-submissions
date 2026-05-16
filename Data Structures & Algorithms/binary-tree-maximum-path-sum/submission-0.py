# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # track the best sum.
        # either it's current + left + right -> upside down V.
        # either it's partially done current + either left or right.
        best = float('-inf')
        
        def gain(node):
            nonlocal best
            if not node:
                return 0
            left_gain = max(gain(node.left),0)
            right_gain = max(gain(node.right),0)
            best = max(best, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)
        gain(root)
        return best