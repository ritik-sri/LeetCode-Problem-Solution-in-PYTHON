class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val

        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            right = check(node.right)

            self.res = max(self.res, max(left, right, left+right) + node.val, node.val)

            return max(max(left, right) + node.val, node.val)

        check(root)

        return self.res