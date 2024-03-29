#User function Template for python3
def levelOrder(root):
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
            curr_lvl.append(curr.data)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        bfs.append(curr_lvl)
    return bfs

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        a=levelOrder(root1)
        b=levelOrder(root2)
        #print(a,b)
        if a==b:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3



#Contributed by Sudarshan Sharma
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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        head1=buildTree(s1)
        head2=buildTree(s2)
        if Solution().isIdentical(head1, head2):
            print("Yes")
        else:
            print("No")
        
        

# } Driver Code Ends