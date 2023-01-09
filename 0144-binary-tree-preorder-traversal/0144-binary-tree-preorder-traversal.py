# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            def traverse(node):
                if not node:
                    return
                pre_order.append(node.val)
                traverse(node.left)
                traverse(node.right)
        
            pre_order = []
            traverse(root)
            return pre_order