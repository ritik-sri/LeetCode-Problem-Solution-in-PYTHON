# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.mini=-1
        l=[]
        def maxDepth(root):
            if root==None:
                return 0
            left=maxDepth(root.left)
            l.append(root.val)
            right=maxDepth(root.right)
        maxDepth(root)
        if len(set(l))==1:
            return -1
        l=set(l)
        l.remove(min(l))
        if len(l)==0:
            return -1
        else:
            return min(l)