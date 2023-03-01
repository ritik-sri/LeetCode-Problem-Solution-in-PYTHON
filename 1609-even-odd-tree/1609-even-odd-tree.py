# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
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
        print(bfs)
        c=1
        flag=0
        if bfs[0][0] %2!=0:
            flag=1
        for arr in bfs[1:]:
            if c%2==0:
                if len(arr)==1:
                    if(arr[0]%2==0):
                        return False
                if len(arr)==2:
                    if(arr[-1]%2==0):
                        return False
                if len(arr)==3:
                    if arr[-1]%2==0:
                        return False
                for j in range(len(arr)-1):
                    if(arr[j]%2!=0 and arr[j]<arr[j+1]):
                        continue
                    else:
                        return False
            else:
                if len(arr)==1:
                    if(arr[0]%2!=0):
                        return False
                if len(arr)==2:
                    if(arr[-1]%2!=0):
                        return False
                for j in range(len(arr)-1):
                    if(arr[j]%2==0 and arr[j]>arr[j+1]):
                        continue
                    else:
                        return False
            c+=1
        if flag==1:
            return True
        else:
            return False