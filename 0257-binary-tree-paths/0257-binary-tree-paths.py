# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def roottoleafpaths(root,path):
            if root is None:
                return None
            path.append(str(root.val))
            if root.left is None and root.right is None:
                ans.append("->".join(path))
            roottoleafpaths(root.left,path.copy())
            roottoleafpaths(root.right,path.copy())
        ans=[]
        path=[]
        roottoleafpaths(root,path)
        return ans