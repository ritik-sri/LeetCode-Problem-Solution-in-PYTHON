# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def Pathsum(root,pathsum):
            if root is None:
                return 0
            pathsum=pathsum*2+root.val
            if root.left==None and root.right==None:
                return pathsum
            return Pathsum(root.left,pathsum)+Pathsum(root.right,pathsum)
        return Pathsum(root,0)