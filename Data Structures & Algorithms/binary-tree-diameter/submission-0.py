# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(root):
            nonlocal best
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            total_depth = 1 + max(left_depth, right_depth)
            best = max(best, left_depth + right_depth)
            return total_depth
        
        depth(root)
        return best