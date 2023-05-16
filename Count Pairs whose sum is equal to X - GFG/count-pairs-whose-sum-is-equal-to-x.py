#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
        


# } Driver Code Ends
#User function Template for python3
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        dic1={}
        dic2={}
        ans=[]
        while h1:
            if h1.data in dic1:
                dic1[h1.data]+=1
            else:
                dic1[h1.data]=1
            h1=h1.next
        
        while h2:
            if h2.data in dic2:
                dic2[h2.data]+=1
            else:
                dic2[h2.data]=1
            h2=h2.next
        for i in dic1:
            r=x-i
            if r in dic2:
                ans.append([i,r])
        return len(ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        X=int(input())
        
        
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,X))


# } Driver Code Ends