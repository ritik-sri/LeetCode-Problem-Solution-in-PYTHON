# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter=0
    def findheight(self,root):
        if root==None:
            return 0
        left=self.findheight(root.left)
        right=self.findheight(root.right)
        currdiameter=left+right
        self.diameter=max(currdiameter,self.diameter)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findheight(root)
        return self.diameter