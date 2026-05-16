# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level_obj = []
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_obj.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_obj: result.append(level_obj)
        return result