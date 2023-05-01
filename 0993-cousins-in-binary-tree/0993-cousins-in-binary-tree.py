from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        bfs=[]
        if root is None:
            return bfs
        q=deque([])
        ans=[]
        q.append(root)
        lvl=1
        while q:
            lvl_size=len(q)
            curr_lvl=[]
            for i in range(lvl_size):
                curr=q.popleft()
                if curr.val==x or curr.val==y:
                    if root.val==curr.val:
                        ans.append([curr.val,-1,-1])
                curr_lvl.append(curr.val)
                if curr.left and (curr.left.val == x or curr.left.val == y):
                    ans.append([curr.left.val,curr.val,lvl]) 
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right and (curr.right.val == x or curr.right.val == y):
                    ans.append([curr.right.val,curr.val,lvl])
                if curr.right is not None:
                    q.append(curr.right)
            bfs.append(curr_lvl)
            lvl+=1
        a=ans.pop()
        b=ans.pop()
        if a[1]!=b[1] and a[2]==b[2]:
            return True
        else:
            return False
        
