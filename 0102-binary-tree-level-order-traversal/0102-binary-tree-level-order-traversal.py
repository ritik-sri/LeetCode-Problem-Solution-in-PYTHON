# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs=[]
        if root is None:
            return bfs
        q=deque([])
        q.append(root)
        while q:
            lvl_size=len(q)
            curr_lvl=[]
            for i in range(lvl_size):
                curr=q.popleft()
                curr_lvl.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            bfs.append(curr_lvl)
        return bfs