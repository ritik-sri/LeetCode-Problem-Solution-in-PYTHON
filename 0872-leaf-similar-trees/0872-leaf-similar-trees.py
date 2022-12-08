# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
            
            if node.left:
                traverse(node.left, leaves)
            if node.right:
                traverse(node.right,leaves)
        
        leaves1 = []
        leaves2 = []
        traverse(root1, leaves1)
        traverse(root2, leaves2)
        return leaves1 == leaves2