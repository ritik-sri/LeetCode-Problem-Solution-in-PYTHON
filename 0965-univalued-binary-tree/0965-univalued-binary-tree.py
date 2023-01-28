# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def inorder(root):
            if root is None:
                return 0
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        if len(set(l))==1:
            return True
        else:
            return False