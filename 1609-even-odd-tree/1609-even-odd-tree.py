class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        q = deque([])
        q.append(root)
        c = 0
        
        while q:
            lvl_size = len(q)
            prev = None
            
            for i in range(lvl_size):
                curr = q.popleft()
                
                # check if the current node value satisfies the Even-Odd conditions
                if c % 2 == 0:
                    if curr.val % 2 != 1 or (prev is not None and curr.val <= prev):
                        return False
                else:
                    if curr.val % 2 != 0 or (prev is not None and curr.val >= prev):
                        return False
                
                prev = curr.val
                
                # add the child nodes to the queue
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            
            c += 1
        
        return True
