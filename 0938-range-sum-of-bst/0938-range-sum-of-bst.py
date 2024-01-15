class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def calculate(root, low, high):
            if not root:
                return 0
            if low <= root.val <= high:
                return root.val + calculate(root.left, low, high) + calculate(root.right, low, high)
            elif root.val < low:
                return calculate(root.right, low, high)
            else:
                return calculate(root.left, low, high)

        return calculate(root, low, high)
