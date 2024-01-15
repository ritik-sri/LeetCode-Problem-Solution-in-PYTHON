# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, node, maxSeen, minSeen):
        self.res = max(abs(node.val-maxSeen), self.res, abs(node.val-minSeen))
        maxSeen = max(maxSeen, node.val)
        minSeen = min(minSeen, node.val)

        if node.left:
            self.dfs(node.left, maxSeen, minSeen)
        if node.right:
            self.dfs(node.right, maxSeen, minSeen)
        