# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def preorder(root):
            if not root:
                result.append('N')
                return None
            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        answer = ",".join(result)
        return answer
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(','))
        
        def dfs():
            val = next(tokens)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

