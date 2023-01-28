# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(root,val):
            if not root:
                return
            if root.val==val:
                return root
            if root.val>val:
                return bst(root.left,val)
            else:
                return bst(root.right,val)
        return bst(root,val)