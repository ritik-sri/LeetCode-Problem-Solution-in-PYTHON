from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        q = deque([(root, 1)])
        while q:
            node, current_depth = q.popleft()
            if current_depth == depth - 1:
                left = TreeNode(val)
                right = TreeNode(val)
                left.left = node.left
                right.right = node.right
                node.left = left
                node.right = right
            else:
                if node.left:
                    q.append((node.left, current_depth + 1))
                if node.right:
                    q.append((node.right, current_depth + 1))
        return root
