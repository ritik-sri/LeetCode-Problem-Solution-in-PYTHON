#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def countNodes(self, root):
        ans = 0
        def f(root):
            nonlocal ans
            if root is None:
                return 
            ans += 1
            f(root.left)
            f(root.right)
        f(root)
        return ans
        

#{ 
 # Driver Code Starts.
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def constructTree(idx, arr):
    if idx >= len(arr):
        return None
    root = Node(arr[idx])
    root.left = constructTree(2 * idx + 1, arr)
    root.right = constructTree(2 * idx + 2, arr)
    return root
        
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        v = list(map(int, input().split()))
        root = constructTree(0, v)
        obj = Solution()
        print(obj.countNodes(root))
# } Driver Code Ends