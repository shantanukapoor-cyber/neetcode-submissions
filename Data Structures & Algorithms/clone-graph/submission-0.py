"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new_mapping = {}
        def dfs(originalNode):
            if originalNode in old_new_mapping:
                return old_new_mapping[originalNode]
            new_node = Node()
            new_node.val = originalNode.val
            old_new_mapping[originalNode] = new_node
            for childNode in originalNode.neighbors:
                new_node.neighbors.append(dfs(childNode))
            return new_node
        return dfs(node)
        