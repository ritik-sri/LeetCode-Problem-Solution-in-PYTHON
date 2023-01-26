# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution545:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        outlist=[]
        st=1
        while queue:
            lvl_size=len(queue)
            count=1
            curr_lvl=[]
            for i in range(n):
                a=queue.pop(0)
                curr_lvl.append(a)
                if a.left:
                    queue.append(a.right)
                if a.right:
                    queue.append(a.left)
            if st==0:
                outlist.append(curr_lvl)
                st=1
            else:
                outlist.append(curr_lvl[::-1])
                st=0
        return outlist
class Solution:
    def zigzagLevelOrder(self, root):
        
        res = []
        if not root: return res
        zigzag = True
        
        q = collections.deque()
        q.append(root)
        
        while q:
            n = len(q)
            nodesOfThisLevel = []
            
            for i in range(n):
                node = q.popleft()
                nodesOfThisLevel.append(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            if zigzag:
                res.append(nodesOfThisLevel)
                zigzag = False
            else:
                res.append(nodesOfThisLevel[::-1])
                zigzag = True
        
        return res