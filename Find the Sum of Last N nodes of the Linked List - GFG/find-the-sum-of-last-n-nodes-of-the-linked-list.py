#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    c=1
    temp=head
    while temp:
        c+=1
        temp=temp.next
    r=c-n
    a=0
    l=[]
    temp=head
    while temp:
        a+=1
        if(a>=r):
            l.append(temp.data)
        temp=temp.next
    return sum(l)
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

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.insert(x)  # add to the end of the list
        print(sumOfLastN_Nodes(a.head,nth_node))


# } Driver Code Ends