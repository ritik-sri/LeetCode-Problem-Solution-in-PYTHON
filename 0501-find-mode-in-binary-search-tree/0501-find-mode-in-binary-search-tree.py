from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
            
        l = []
        inorder(root)
        b = Counter(l)
        maxi = float("-inf")
        modes = []
        
        for i, j in b.items():
            if j > maxi:
                maxi = j
                modes = [i]
            elif j == maxi:
                modes.append(i)
        return modes
