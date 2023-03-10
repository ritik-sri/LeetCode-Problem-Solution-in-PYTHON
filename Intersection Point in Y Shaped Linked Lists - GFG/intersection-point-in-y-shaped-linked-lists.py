def getLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersetPoint(head1,head2):
    if head1 == None or head2 == None:
        return -1
    
    len1 = getLength(head1)
    len2 = getLength(head2)
    
    ptr1 = head1
    ptr2 = head2
    
    # Move the longer list's pointer ahead
    if len1 > len2:
        for i in range(len1 - len2):
            ptr1 = ptr1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            ptr2 = ptr2.next
    
    # Iterate over both lists in parallel until intersection point is found
    while ptr1 and ptr2:
        if ptr1 == ptr2:
            return ptr1.data
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))

# } Driver Code Ends