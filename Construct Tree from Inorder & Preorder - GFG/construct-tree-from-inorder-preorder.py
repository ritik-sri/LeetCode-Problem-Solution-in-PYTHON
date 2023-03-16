# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def buildtree(self, inorder, preorder, n):
        if not preorder or not inorder:
            return None
        
        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildtree(inorder[:mid], preorder[1:mid+1], n)
        root.right = self.buildtree(inorder[mid+1:], preorder[mid+1:], n)
        return root



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends