class Solution:
    def ladoos(self, root, home, k):
        pMap = {}
        self.fillParentMap(pMap, None, root)
        targetNode = self.searchNode(root, home)
        return self.bfsTraversal(set(), pMap, targetNode, k)
    def fillParentMap(self, pMap, parent, root):
        if root is None:
            return
        pMap[root] = parent
        self.fillParentMap(pMap, root, root.left)
        self.fillParentMap(pMap, root, root.right)
    def searchNode(self, root, target):
        if root is None or root.data == target:
            return root
        left = self.searchNode(root.left, target)
        if left is not None:
            return left
        return self.searchNode(root.right, target)
    def bfsTraversal(self, vis, pMap, root, k):
        sum = 0
        q = []
        q.append(root)
        vis.add(root)
        while len(q) > 0 and k >= 0:
            size = len(q)
            while size > 0:
                curr = q.pop(0)
                par = pMap.get(curr)
                left = curr.left
                right = curr.right
                sum += curr.data
                if par is not None and par not in vis:
                    vis.add(par)
                    q.append(par)
                if left is not None and left not in vis:
                    vis.add(left)
                    q.append(left)
                if right is not None and right not in vis:
                    vis.add(right)
                    q.append(right)
                size -= 1
            k -= 1
        return sum
#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        home=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.ladoos(root,home,k))


# } Driver Code Ends