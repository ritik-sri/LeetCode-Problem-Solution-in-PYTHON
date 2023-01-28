# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_difference=True
        def maxDepth(root):
            if root==None:
                return 0
            left=maxDepth(root.left)
            right=maxDepth(root.right)
            self.max_difference = self.max_difference and abs(left - right)<=1
            return max(left,right)+1
        maxDepth(root)
        return self.max_difference