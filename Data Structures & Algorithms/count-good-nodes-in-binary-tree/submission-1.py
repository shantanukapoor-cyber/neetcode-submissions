# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 0
        def dfs(root, value):
            nonlocal good
            if not root:
                return value
            if root.val >= value:
                good += 1
                value = root.val
            left = dfs(root.left, value)
            right = dfs(root.right, value)
            return left or right 
        dfs(root, float('-inf'))
        return good
            