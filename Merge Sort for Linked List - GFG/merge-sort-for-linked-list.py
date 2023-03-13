class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mer(self,arr,mid,l,r):
        n1=mid-l+1
        n2=r-mid
        left=[]
        right=[]
        for i in range(n1):
            left.append(arr[l+i])
        for i in range(n2):
            right.append(arr[mid+1+i])
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<n1:
            arr[k]=left[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=right[j]
            j+=1
            k+=1
    def merge(self,arr,l,r):
        if l<r:
            mid=(l+r)//2
            self.merge(arr,l,mid)
            self.merge(arr,mid+1,r)
            self.mer(arr,mid,l,r)
    def mergeSort(self, head):
        li=[]
        temp=head
        while temp:
            li.append(temp.data)
            temp=temp.next
        #li.sort()
        self.merge(li,0,len(li)-1)
        l3=LinkedList()
        for i in li:
            l3.append(i)
        return l3.head


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
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
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends