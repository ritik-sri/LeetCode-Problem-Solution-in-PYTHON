# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric_helper(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return is_symmetric_helper(left.left, right.right) and is_symmetric_helper(left.right, right.left)
        
        if root is None:
            return True
        else:
            return is_symmetric_helper(root.left, root.right)
