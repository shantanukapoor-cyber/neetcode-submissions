# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder -> left root right
        # preorder -> root left right
        # root = preorder[0]
        # if root = mid in inorder
        # inorder[:mid] is root.left, inorder[mid:1] is root.right
        # preorder[1:mid+1] is root.left, preorder[mid+1:] is root.right
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                mid = i
                break
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root