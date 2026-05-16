# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS last node of the level.
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if _ == level_size - 1:
                        result.append(node.val)
        return result
                    
