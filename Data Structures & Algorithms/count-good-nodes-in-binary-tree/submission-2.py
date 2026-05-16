# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return 0
            if root.val >= value:
                good = 1
                value = root.val
            else:
                good = 0
            left = dfs(root.left, value)
            right = dfs(root.right, value)
            return good + left + right
        answer = dfs(root, float('-inf'))
        return answer
            