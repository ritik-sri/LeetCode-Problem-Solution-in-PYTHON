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
        queue = deque([(root, 1)])
        while queue:
            node,current_depth=queue.popleft()
            if current_depth==depth-1:
                leftchild=TreeNode(val)
                rightchild=TreeNode(val)
                leftchild.left=node.left
                rightchild.right=node.right
                node.left=leftchild
                node.right=rightchild
            else:
                if node.left:
                    queue.append((node.left, current_depth + 1))
                if node.right:
                    queue.append((node.right, current_depth + 1))
        return root
